import re
from os import listdir
import xml.etree.ElementTree as ET

def xml2yolo(bbox, w, h):

    # bbox = [xmin, ymin, xmax, ymax]

    x_center = (bbox[2]+bbox[0])/2/w
    y_center = (bbox[3]+bbox[0])/2/h
    width = (bbox[2] - bbox[0])/w
    height = (bbox[3] - bbox[1])/h
    return str(x_center), str(y_center), str(width), str(height)

label_path = r'/xml'
save_path = r'C:\workplace\SW_academy\project1\Data\bed_label'
files = listdir(label_path)
class_dict = {'0000' : '0',
'0010' : '1',
'0020' : '2',
'0001' : '3',
'0011' : '4',
'0021' : '5',
'0100' : '6',
'0110' : '7',
'0120' : '8',
'0101' : '9',
'0111' : '10',
'0121' : '11',
'1000' : '12',
'1010' : '13',
'1020' : '14',
'1001' : '15',
'1011' : '16',
'1021' : '17',
'1100' : '18',
'1110' : '19',
'1120' : '20',
'1101' : '21',
'1111' : '22',
'1121' : '23'
}
for fil in files:
    if fil.endswith('xml'):
        X = ET.parse(label_path + '/' + fil)
        width = int(X.find("size").find("width").text)
        height = int(X.find("size").find("height").text)
        for obj in X.findall('object'):
            label = obj.find("name").text
            c = class_dict[str(label)]
            box = [int(cord.text) for cord in obj.find('bndbox')]
            yolo_box = xml2yolo(box, width, height)
            temp = " ".join(yolo_box)
            result = (f"{c} {temp}")
        with open(save_path + '/' + fil[:-4] + '.txt', 'w') as fp:
            fp.write(result)
