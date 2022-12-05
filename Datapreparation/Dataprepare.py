from os import listdir, mkdir, remove
from PIL import Image
import albumentations as A
import numpy as np
import pickle

IMAGESIZE = (400, 400)


# modification function
def chair_cls_p24(line):
    p = line.split()
    p[0] = str(int(p[0], 10) + 24)
    result = " ".join(p)
    return result

# stratified train/val/test split
def build_imgcls_dict(imgp: str, labelp: str):
    """
    :param imgp: path to image files
    :param labelp: path to label files
    :return: {class : [image_paths]}
    """
    # label dict 만들고, label : cls
    # image dict 만들기. cls : img
    label_list = listdir(labelp)
    label_dict = dict()
    for label in label_list:
        with open(labelp + '\\' + label, 'r') as fp:
            temp = fp.read()
        temp = temp.splitlines()
        target = [line.split()[0] for line in temp]
        label_dict[label[:-4]] = target # list of cls
    img_dict = dict()
    for i in listdir(imgp):
        target = label_dict[i[:-4]] # list of cls
        for cls in target:
            if cls not in [k for k in img_dict]:
                img_dict[cls] = list()
            img_dict[cls].append(i)
    maxfreq = max([len(v) for k, v in img_dict.items()])
    result = {k : (v, int(round(maxfreq/len(v), 0))) for k, v in img_dict.items() if round(maxfreq/len(v), 0) <= 128}

    # try:
    #     print(f'img_dict 17 : {len(img_dict["17"])}')
    # except KeyError:
    #     print('17 not found in img_dict')
    # try:
    #     print(f'img_dict 17 : {len(result["17"])}')
    # except KeyError:
    #     print('17 not found in result')

    return result


def save_imgd_labeld(imgs, label_path, img_path, save_root, vailed_labels, cat="train", modification=None):
    if cat not in listdir(save_root):
        mkdir(save_root + '\\' + cat)
    if 'images' not in listdir(save_root + '\\' + cat):
        mkdir(save_root + '\\' + cat + '\\' + 'images')
    if 'labels' not in listdir(save_root + '\\' + cat):
        mkdir(save_root + '\\' + cat + '\\' + 'labels')

    # ITER for data agumentation
    ITER = imgs[1]

    #image and label save begins
    for img in imgs[0]:

        # Read label
        with open(label_path + '\\' + img[:-4] + '.txt', 'r') as fp:
            cls_bbox = fp.read() # class x_cen y_cen w h
        dump = list()
        for line in cls_bbox.splitlines():
            if line.split()[0] in vailed_labels:
                dump.append(line)
                if modification is not None:
                    dump[-1] = modification(dump[-1])
        cls_bbox_str = "\n".join(dump)


        # key corruption test
        # test = [p.split()[0] for p in [line for line in cls_bbox_str.splitlines()]]
        # for test_label in test:
        #     assert test_label in vailed_labels, f'key corrputed -vailed_labels : {vailed_labels, type(vailed_labels)}, cls_bbox : ' \
        #                                           f'{cls_bbox}, test_type : {[type(d) for d in test]} | {test}!'
        # length test
        # assert len(cls_bbox_str) != 0, f'zero-length detected for {img} | {cls_bbox} | {vailed_labels} | {modification}'


        # Save label.
        with open(save_root + '\\' + cat + '\\' + 'labels' + '\\' + img[:-4] + '.txt', 'w') as fp:
            fp.write(cls_bbox_str)

        # Read image & save it.
        try:
            temp = Image.open(img_path + '\\' + img)
            temp.save(save_root + '\\' + cat + '\\' + 'images' + '\\' + img)
        except:
            print('failed to save/open image')

        # Data Agumentation for train set.
        if cat == 'train':
            cls_bbox_list = [line.split() for line in cls_bbox_str.splitlines()]
            cls = [int(b[0], 10) for b in cls_bbox_list]
            bbox = [[float(cord) for cord in b[1:]] for b in cls_bbox_list]
            # Compose transfrom
            transform = A.Compose([
                A.RandomBrightnessContrast(brightness_limit=(-.5, .2),
                                           contrast_limit=.2,
                                           brightness_by_max=True,
                                           always_apply=False,
                                           p=.55),

                # hue : base color / sat : intensity of color / val : how light or dark color is when hue held const.
                A.HueSaturationValue(
                    # hue_shift_limit=0,
                    # sat_shift_limit=(30, 30),
                    # val_shift_limit=0,
                    p=.55),

                A.GaussNoise(
                    p=.55
                ),

                A.HorizontalFlip(
                    p=.55
                ),

                A.RandomCrop(
                    height=int(np.array(temp).shape[0] * 0.8),
                    width=int(np.array(temp).shape[1] * 0.8),
                    p=.55
                ),

                A.RandomScale(
                    scale_limit=.2,
                    p=.55),

                A.Rotate(
                    limit=45,
                    p=.55
                )
            ], bbox_params=A.BboxParams(format='yolo', min_visibility=0.5, label_fields=['class_labels']))

            for k in range(ITER):
                transformed = transform(image = np.array(temp), bboxes = bbox, class_labels = cls)
                Image.fromarray(transformed['image']).save(save_root + '\\' + cat + '\\' + 'images' + '\\' + img[:-4] + '_' + str(k) + '.jpg')
                label = ""
                for b, c in zip(transformed['bboxes'], transformed['class_labels']):
                    if type(c) is list:  # for multi-class problem
                        c = [str(num) for num in c]
                        temp_cls = " ".join(c)
                    else:
                        temp_cls = str(c)
                    b = [str(num) for num in b]
                    temp_cords = " ".join(b)
                    label = label + temp_cls + " " + temp_cords + "\n"

                if len(label) == 0:
                    print(f'zero-length detected')
                    print(f'str : {cls_bbox_str}, cls_bbox_list : {cls_bbox_list}')

                with open(save_root + '\\' + cat + '\\' + 'labels' + '\\' + img[:-4] + '_' + str(k) + '.txt', 'w') as fp:
                    fp.write(label)


def save_img_dict(save_root, img_dict, img_path, label_path, fraction, modification):
    vailed_labels = [k for k in img_dict]
    for k, v in img_dict.items():
        # for num, i in enumerate(v[0]):
        #     with open(label_path + '\\' + i[:-4] + '.txt', 'r') as fp:
        #         temp = fp.read()
        #     # print(k, target)
        #     dump = [p.split()[0] for p in [line for line in temp.splitlines()]]
        #     assert k in dump, f'key corrputed - num : {num}, key : {type(k)}, temp : {temp}, dump_type : {[type(d) for d in dump]} | {dump}!'
        print(f'class : {k} | num clas : {len(v[0])}')
        train = (v[0][:int(len(v[0]) * fraction[0])], v[1])  # train set
        val = (v[0][int(len(v[0]) * fraction[0]) : int(len(v[0]) * fraction[0]) + int(len(v[0]) * fraction[1])], v[1])
        test = (v[0][int(len(v[0]) * fraction[0]) + int(len(v[0]) * fraction[1]):], v[1])
        print(f'train_size : {len(train[0])} | val_size : {len(val[0])} | test_size : {len(test[0])} | AUG_ITER : {v[1]}')
        save_imgd_labeld(train, label_path, img_path, save_root, vailed_labels, cat="train", modification=modification)
        save_imgd_labeld(val, label_path, img_path, save_root, vailed_labels, cat="val", modification=modification)
        save_imgd_labeld(test, label_path, img_path, save_root, vailed_labels, cat="test", modification=modification)

# 2^7 = 128배까지 가능.
# class 별로 분포를 보고 적은건 많이, 많은건 적게.
# 비율이 중요.
# 가장 많은 class를 기준으로 비율 계산. 128 * ratio 만큼 iteration 돌도록.

def bed_chair_together(bed_imgp: str, chair_imgp: str, bed_labelp: str, chair_labelp: str,
                       save_root: str, bf=None, cf=None, fraction=(.7, .2)):
    """
    :param bed_imgp: original path of bed images
    :param chair_imgp: original path of chair images
    :param bed_labelp: original path of bed labels
    :param chair_labelp: original path of chair labels
    :param save_root: target path to save bed/chair labels.
    :param bf: bed label modification function
    :param cf: chair label modification function
    :param fraction: [train_frac, val_frac, test_frac]
    :return: None. Only saves files.
    """
    # :bid:
    # :bld:  {label_path : class}

    # image dict
    bid = build_imgcls_dict(bed_imgp, bed_labelp)
    cid = build_imgcls_dict(chair_imgp, chair_labelp)
    # save imgs
    save_img_dict(save_root, bid, bed_imgp, bed_labelp, fraction, bf)
    save_img_dict(save_root, cid, chair_imgp, chair_labelp, fraction, cf)

# fix labelname for further works.


bed_chair_together(
    r'D:\Workspace\SW_academy\Project1\Data\clean_bed_img',
    r'D:\Workspace\SW_academy\Project1\Data\clean_chair_img',
    r'D:\Workspace\SW_academy\Project1\Data\clean_bed_label',
    r'D:\Workspace\SW_academy\Project1\Data\clean_chair_label',
    r'D:\Workspace\SW_academy\Project1\Src',
    cf=chair_cls_p24,
)

def update_labels(label_path, predefineds):
    classes = list()
    for label in listdir(label_path):
        with open(label_path + '\\' + label, 'r') as fp:
            cls_bbox = fp.read()
        for line in cls_bbox.splitlines():
            if len(line) != 0:
                classes.append(line.split()[0])
    classes = sorted([int(i) for i in set(classes)], reverse = False)
    predefined_classes = list()
    for predefined in predefineds:
        with open(predefined, 'r') as fp:
            pred = fp.read()
        predefined_classes.extend(pred.splitlines())
    predefined_all = {i : k for i, k in enumerate(predefined_classes)}
    actual_cls = [predefined_all[i] for i in classes]
    modified_labels_mapping = {str(k) : str(i) for i , k in enumerate(classes)} # maps : label -> modified label
    actual_cls_mapping = {str(k): str(v) for k, v in zip(modified_labels_mapping.values(), actual_cls)} # maps : modified label -> actual_label
    print(actual_cls, modified_labels_mapping, actual_cls_mapping)

    for label in listdir(label_path):
        dump = list()
        with open(label_path + '\\' + label, 'r') as fp:
            cls_bbox = fp.read()
        for line in cls_bbox.splitlines():
            temp = line.split()
            temp[0] = modified_labels_mapping[temp[0]]
            assert int(temp[0]) in range(len(predefined_all)), f'temp[0] out of range! | temp:{temp[0]}'
            dump.append(" ".join(temp))
        # print("\n".join(dump))
        # print('#####################################################################')

        with open(label_path + '\\' + label, 'w') as fp:
            fp.write("\n".join(dump))

    return actual_cls_mapping, modified_labels_mapping




actual_cls_mapping, modified_labels_mapping = update_labels(r'D:\Workspace\SW_academy\Project1\Src\train\labels',
                                   [r'D:\Workspace\SW_academy\Project1\bed_classes.txt', r'D:\Workspace\SW_academy\Project1\chair_classes.txt'])

with open(r'D:\Workspace\SW_academy\Project1\actual_cls_mapping', 'wb') as fp:
    pickle.dump(actual_cls_mapping, fp)

with open(r'D:\Workspace\SW_academy\Project1\modified_labels_mapping', 'wb') as fp:
    pickle.dump(modified_labels_mapping, fp)
