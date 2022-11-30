from os import listdir, mkdir
from PIL import Image


# modification function
def chair_cls_p24(temp):
    modified = list()
    for t in temp.splitlines():
        p = t.split()
        p[0] = str(int(p[0], 10) + 24)
        modified.append(" ".join(p))
    result = "\n".join(modified)
    return result

# stratify train/val/test split
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
        temp = temp.splitlines()[0]
        target = temp.split()[0]
        label_dict[label[:-4]] = target
    img_dict = dict()
    for i in listdir(imgp):
        target = label_dict[i[:-4]]
        if target not in [k for k in img_dict]:
            img_dict[target] = list()
        img_dict[target].append(i)
    return img_dict


def save_imgd_labeld(imgs, label_path, img_path, save_root, cat="train", modification=None):
    if cat not in listdir(save_root):
        mkdir(save_root + '\\' + cat)
    if 'images' not in listdir(save_root + '\\' + cat):
        mkdir(save_root + '\\' + cat + '\\' + 'images')
    if 'labels' not in listdir(save_root + '\\' + cat):
        mkdir(save_root + '\\' + cat + '\\' + 'labels')

    for img in imgs:
        try:
            temp = Image.open(img_path + '\\' + img)
            temp.save(save_root + '\\' + cat + '\\' + 'images' + '\\' + img)
        except:
            print('failed to save/open image')

        train_label = label_path + '\\' + img[:-4] + '.txt'
        with open(train_label, 'r') as fp:
            temp = fp.read()

        if modification is not None:
            temp = modification(temp)

        with open(save_root + '\\' + cat + '\\' + 'labels' + '\\' + img[:-4] + '.txt', 'w') as fp:
            fp.write(temp)


def save_img_dict(save_root, img_dict, img_path, label_path, fraction, modification):
    for k, v in img_dict.items():
        train = v[:int(len(v) * fraction[0])]  # train set
        val = v[int(len(v) * fraction[0]): int(len(v) * fraction[0]) + int(len(v) * fraction[1])]
        test = v[int(len(v) * fraction[0]) + int(len(v) * fraction[1]):]
        save_imgd_labeld(train, label_path, img_path, save_root, cat="train", modification=modification)
        save_imgd_labeld(val, label_path, img_path, save_root, cat="val", modification=modification)
        save_imgd_labeld(test, label_path, img_path, save_root, cat="test", modification=modification)


def bed_chair_together(bed_imgp: str, chair_imgp: str, bed_labelp: str, chair_labelp: str,
                       save_root: str, bf=None, cf=None, fraction=(.7, 0.2)):
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

    # save imgs
    bid = build_imgcls_dict(bed_imgp, bed_labelp)
    cid = build_imgcls_dict(chair_imgp, chair_labelp)

    save_img_dict(save_root, bid, bed_imgp, bed_labelp, fraction, bf)
    save_img_dict(save_root, cid, chair_imgp, chair_labelp, fraction, cf)

# Data Agumentation
def data_aug