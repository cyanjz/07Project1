from os import listdir
from PIL import Image
import numpy as np

biinpath = r'D:\Workspace\SW_academy\Project1\Data\1bed_img'
blinpath = r'D:\Workspace\SW_academy\Project1\Data\1bed_label'
bioutpath = r'D:\Workspace\SW_academy\Project1\Data\clean_bed_img'
bloutpath = r'D:\Workspace\SW_academy\Project1\Data\clean_bed_label'

ciinpath = r'D:\Workspace\SW_academy\Project1\Data\1chair_img'
clinpath = r'D:\Workspace\SW_academy\Project1\Data\1chair_label'
cioutpath = r'D:\Workspace\SW_academy\Project1\Data\clean_chair_img'
cloutpath = r'D:\Workspace\SW_academy\Project1\Data\clean_chair_label'

def remove_unlabeled(img_path, label_path, out_path):
    imgs = [p[:-4] for p in listdir(img_path)]
    labels = [p[:-4] for p in listdir(label_path)]
    labeled = [img for img in imgs if img in labels]
    for labeled_img in labeled:
        try:
            im = Image.open(img_path + '/' + labeled_img + '.jpg')
            im.save(out_path + '/' + labeled_img + '.jpg')
        except:
            print("failed to save image.")

def remove_trash_labels(img_path, label_path, out_path):
    imgs = [p[:-4] for p in listdir(img_path)]
    labels = [p[:-4] for p in listdir(label_path)]
    has_img = [lab for lab in labels if lab in imgs]
    for lab in has_img:
        # try:
        with open(label_path + '\\' + lab + '.txt', 'r') as fp:
            cls_bbox = fp.read()

        cls_bbox_list = [line.split() for line in cls_bbox.splitlines()]
        cls = [int(b[0], 10) for b in cls_bbox_list]
        bbox = [[float(cord) for cord in b[1:]] for b in cls_bbox_list]
        correct_cords = True
        for b in bbox:
            # x_max, y_max, x_min, y_min
            cords = [b[0] + b[2] / 2, b[1] + b[3] / 2, b[0] - b[2] / 2, b[1] - b[3] / 2]
            for cord in cords:
                if not 0<=cord<=1 and not np.isclose(cord, 1, atol=1e-02) and not np.isclose(cord, 0, atol=1e-02):
                    print(cords)
                    print('corrupted file detected! Skips corresponding files...')
                    correct_cords = False
                    break

        if correct_cords:
            with open(out_path + '\\' + lab + '.txt', 'w') as fp:
                fp.write(cls_bbox)
        # except:
        #     print("failed to save the label.")


remove_trash_labels(biinpath, blinpath, bloutpath)
remove_unlabeled(biinpath, bloutpath, bioutpath)
remove_trash_labels(ciinpath, clinpath, cloutpath)
remove_unlabeled(ciinpath, cloutpath, cioutpath)

