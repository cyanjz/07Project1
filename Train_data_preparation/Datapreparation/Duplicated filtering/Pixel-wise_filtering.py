import cv2
import numpy as np
from PIL import Image


# Originally considered pixel-wise filtering.
# Divide and conquer method is applied due to memory issue.
# Deprecated.
def im_diff_rate(im1, im2):
  '''
  Calculate ratio of different pixels
  '''
  if im1.shape != im2.shape:
    im1 = cv2.resize(im1, dsize=(50, 50), interpolation=cv2.INTER_CUBIC)
    im2 = cv2.resize(im2, dsize=(50, 50), interpolation=cv2.INTER_CUBIC)
  try:
    diffim = np.absolute(im1-im2)
    print(diffim)
  except:
    return -1
    print(-1)

  return (diffim > 2).sum()/im1.size

def im_diff_rate(im1, im2):
    '''
    Calculate ratio of different pixels
    Diff calculation changed into d-hash comparison for test
    '''
    try:
        diff = dhash.hamming_distance(im1, im2)
    except:
        diff = -1
    return diff


def div_filt_dups(D1: list, D2: list):
    '''
    modified filt_dups for divide & conquer.
    '''
    result1 = list()
    result2 = list()
    im_list1 = list()
    im_list2 = list()
    print(f'D1 is {D1}')
    print(f'D2 is {D2}')
    for d in D1:
        try:
            print(d)
            im_list1.append((d, Image.open(d)))
        except:
            print('unable to open image!')

    for d in D2:
        try:
            print(d)
            im_list2.append((d, Image.open(d)))
        except:
            print('unable to open image!')

    print('filtering started...')
    while len(im_list1) != 0:
        im = im_list1.pop()
        im_list1 = [i for i in im_list1 if im_diff_rate(im[1], i[1]) > 10]
        im_list2 = [i for i in im_list2 if im_diff_rate(im[1], i[1]) > 10]
        result1.append(im[0])

    while len(im_list2) != 0:
        im = im_list2.pop()
        im_list2 = [i for i in im_list2 if im_diff_rate(im[1], i[1]) > 10]
        result2.append(im[0])

    return result1, result2


def filt_dups(D1: list):
    '''
    Find all unique images
    return list of unique image's path [/xxx/xxx.jpg, /yyy/yyy.jpg]
    '''
    result1 = list()
    im_list1 = list()

    for d in D1:
        try:
            im_list1.append((d, Image.open(d)))
        except:
            print('unable to open image!')
    print('filtering started...')
    while len(im_list1) != 0:
        im = im_list1.pop()
        im_list1 = [i for i in im_list1 if im_diff_rate(im[1], i[1]) > 10]
        result1.append(im[0])

    return result1


def filt_new(D1, D2):
    '''
    modified filt_dups to filter new images
    '''
    result = list()
    im_list1 = list()
    im_list2 = list()

    for d in D1:
        try:
            im_list1.append((d, np.array(Image.open(d))))
        except:
            print('unable to open image!')

    for d in D2:
        try:
            im_list2.append((d, np.array(Image.open(d))))
        except:
            print('unable to open image!')
    print('filtering started...')
    while len(im_list2) != 0:
        im = im_list2.pop()
        im_list2 = [i for i in im_list2 if im_diff_rate(im[1], i[1]) > 10]
        result.append(im[0])
    return result


def div_filt(D):
    '''
    divide & conquer
    '''
    m = len(D) // BATCH_SIZE
    result = []
    temp = []
    for i in range(m + 1):
        temp.append(D[i * BATCH_SIZE: (i + 1) * BATCH_SIZE])
    for k in range(len(temp)):
        for l in range(len(temp)):
            if k < l:
                pass
            elif k == l:
                print(f'{k}, {l} batch filtering')
                temp[k] = filt_dups(temp[k])
            else:
                print(f'{k}, {l} batch filtering')
                temp[k], temp[l] = div_filt_dups(temp[k], temp[l])
    for t in temp:
        result.extend(t)
    return result


def div_filt_new(D1, D2):
    '''
    divide & conquer for filt new
    '''
    m1 = len(D1) // BATCH_SIZE
    m2 = len(D2) // BATCH_SIZE
    result = []
    temp1 = []
    temp2 = []
    for i in range(m1 + 1):
        temp1.append(D1[i * BATCH_SIZE: (i + 1) * BATCH_SIZE])
    for j in range(m2 + 1):
        temp2.append(D2[j * BATCH_SIZE: (j + 1) * BATCH_SIZE])
    for k in range(len(temp1)):
        for l in range(len(temp2)):
            print(f'{k}, {l} batch filtering')
            temp2[l] = filt_new(temp1[k], temp2[l])
    for t in temp2:
        result.extend(t)
    return result