from os import listdir
from PIL import Image
import numpy as np

def im_diff_rate(im1, im2):
  if im1.shape != im2.shape:
    im1 = cv2.resize(im1, dsize=(50, 50), interpolation=cv2.INTER_CUBIC)
    im2 = cv2.resize(im2, dsize=(50, 50), interpolation=cv2.INTER_CUBIC)
  diffim = np.absolute(im1-im2)
  return (diffim > 2).sum()/im1.size


# filter images.
def filt_dups(path1 : list):
  result = list()
  im_list  = list()
  if type(path1) == list:
    D = list()
    for path in path1:
      D.extend([path + '/' + p for p in listdir(path)])
  else:
    D = [path1 + '/' + d for d in listdir(path1)]
  for d in D:
    try:
      im_list.append((d, np.array(Image.open(d))[..., :3]))
    except:
      print('non-jpg detected')
  while len(im_list) != 0:
    im = im_list.pop()

    # keeps images that half of the pixels are different.
    im_list = [tup for tup in im_list if im_diff_rate(tup[1], im[1]) > .5]
    result.append(im)
  return result

def save_result(root, result):
  for tup in result:
    Image.fromarray(tup[1]).save(root + re.search('/[^/]+/[^/]+.jpg$', tup[0])[0])