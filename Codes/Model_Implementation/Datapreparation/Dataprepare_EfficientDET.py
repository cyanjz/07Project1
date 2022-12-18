import pandas as pd
from os import listdir
from PIL import Image
import pickle


with open(r'/actual_cls_mapping', 'rb') as fp:
    mapper = pickle.load(fp)


def label2csv(image_path, label_path, mapper):
    label_df = pd.DataFrame(columns=['image_path', 'x1', 'y1', 'x2', 'y2', 'cls_name'])
    labels = listdir(label_path)
    for label in labels:
        with open(label_path + '\\' + label, 'r') as fp:
            cls_bbox = fp.read()

        im = Image.open(image_path + '\\' + label[:-4] + '.jpg')
        img_w, img_h = im.size

        for line in cls_bbox.splitlines():
            dump = [str(image_path + '\\' + label[:-4] + '.jpg')]
            cls_id, x_center, y_center, box_w, box_h = line.split()
            cls_id, x_center, y_center, box_w, box_h = int(cls_id), float(x_center), float(y_center), float(box_w), float(box_h)
            x1 = max(int(round((x_center - box_w/2) * img_w)), 0)
            x2 = min(int(round((x_center + box_w/2) * img_w)), img_w)
            y1 = max(int(round((y_center - box_h/2) * img_h)), 0)
            y2 = min(int(round((y_center + box_h/2) * img_h)), img_h)
            dump.extend([x1, y1, x2, y2, mapper[str(cls_id)]])
            dump_df = pd.DataFrame([dump], columns=['image_path', 'x1', 'y1', 'x2', 'y2', 'cls_name'])
            label_df = pd.concat([label_df, dump_df])
    return label_df


label_df = label2csv(r'/train/images',
                     r'D:\Workspace\SW_academy\Project1\Src\train\labels',
                     mapper)

label_df.to_csv(r'D:\Workspace\SW_academy\Project1\Src\EfficientDET.csv', index=False, header=False, encoding='cp949')

