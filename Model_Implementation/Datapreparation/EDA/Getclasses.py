import re
from os import listdir
import seaborn as sns


def chair_cls_p24(line):
    p = line.split()
    p[0] = str(int(p[0], 10) + 24)
    result = " ".join(p)
    return result


def get_label_dict(label_path):
    label_dict = dict()
    label_dict['classes'] = []
    label_dict['x_center'] = []
    label_dict['y_center'] = []
    label_dict['width'] = []
    label_dict['height'] = []

    modification = chair_cls_p24

    if not label_path.endswith('\\'):
        label_path = label_path + '\\'
    files = [label_path + p for p in listdir(label_path)]
    for fil in files:
        with open(fil, 'r') as fp:
            temp = fp.read()
            temp = temp.splitlines()
        for line in temp:
            dump = line.split()
            for i, k in enumerate(label_dict):
                label_dict[k].append(dump[i])
    #     with open(fil, 'r') as fp:
    #         cls_bbox = fp.read()
    #     dump = list()
    #     for line in cls_bbox.splitlines():
    #         if line.split()[0] == '6':
    #             dump.append(line)
    #             if modification is not None:
    #                 dump[-1] = modification(dump[-1])
    #     if len(dump) != 0:
    #         print(dump)
    return label_dict

get_label_dict(r'../../../Data/clean_chair_label')
