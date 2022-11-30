import re
from os import listdir
import seaborn as sns


def get_label_dict(label_path):
    label_dict = dict()
    label_dict['classes'] = []
    label_dict['x_center'] = []
    label_dict['y_center'] = []
    label_dict['width'] = []
    label_dict['height'] = []

    if not label_path.endswith('/'):
        label_path = label_path + '/'
    files = [label_path + '\\' + p for p in listdir(label_path)]
    for fil in files:
        with open(fil, 'r') as fp:
            temp = fp.read()
            temp = temp.splitlines()
        for t in temp:
            dump = t.split()
            for i, k in enumerate(label_dict):
                label_dict[k].append(dump[i])
    return label_dict
