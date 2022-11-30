from os import listdir
from PIL import Image

bimgpath = r'C:\workplace\SW_academy\project1\Data\1bed_img_temp'
blabelpath = r'C:\workplace\SW_academy\project1\Data\1bed_label_temp'
bioutpath = r'C:\workplace\SW_academy\project1\Data\1bed_img'
bloutpath = r'C:\workplace\SW_academy\project1\Data\1bed_label'

cimgpath = r'C:\workplace\SW_academy\project1\Data\1chair_img_temp'
clabelpath = r'C:\workplace\SW_academy\project1\Data\1chair_label'
coutpath = r'C:\workplace\SW_academy\project1\Data\1chair_img'

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
        try:
            with open(label_path + '/' + lab + '.txt', 'r') as fp:
                temp = fp.read()
            with open(out_path + '/' + lab + '.txt', 'w') as fp:
                fp.write(temp)
        except:
            print("failed to save the label.")
# remove_unlabeled(bimgpath, blabelpath, bIoutpath)
remove_trash_labels(bimgpath, blabelpath, bloutpath)
# remove_unlabeled(cimgpath, clabelpath, coutpath)
