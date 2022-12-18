import albumentations as A
from os import listdir, remove
from Dataprepare import build_imgcls_dict
from PIL import Image
import numpy as np

NUMCLS = 3
NUM_ITER = 10000/NUMCLS
IMAGESIZE = (400, 400)
IMAGEPATH = ''
LABELPATH = ''
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

    A.VerticalFlip(
        p=.55
    ),

    A.RandomCrop(
        height= int(IMAGESIZE[0] * 0.2),
        width = int(IMAGESIZE[1] * 0.2),
        p=.55
    ),

    A.RandomScale(
        scale_limit=.2,
        p=.55),

    A.Rotate(
        limit = 45,
        p=.55
    )
])



imgdict = build_imgcls_dict()

def agumentation(im, lpath, spath):

    img_files = listdir(ipath)

    for img in img_files:
        with open(lpath + '/' + img[:-4] + '.txt', 'r') as fp:
            cls_bbox = fp.read()
        if cls_bbox.split[0] == '23' or cls_bbox.splt[0] == '14':
            remove(lpath + '/' + img[:-4] + '.txt')
            remove(ipath  + '/' + img[:-4])
        else:
            cls_bbox = [line.split() for line in cls_bbox.splitlines()]
            cls = [int(b[0], 10) for b in cls_bbox]
            bbox = [[float(cord) for cord in b[1:]] for b in cls_bbox]

            im = np.array(Image.open(ipath + '/' + img))
            transformed = transform(image = im, bboxes = bbox, class_labels = cls)
            # list of list.

            # save transformed image
            Image.fromarray(transformed['image']).save(spath + '/' + 'images' + '/' + img)


            with open(lpath + '/' + 'labels' + '/' + img[:-4] + '.txt', 'w') as fp:
                fp.write()
