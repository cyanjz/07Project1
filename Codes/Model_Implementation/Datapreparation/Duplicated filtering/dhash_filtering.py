from os import listdir, mkdir
import re
from PIL import Image


# To distribute work (labeling bbox & class) for each teammate.
NUM_PEOPLE = 5

# dhash & hamming distance from https://github.com/Rayraegah/dhash.git


class dhash(object):
    """
    usage:

    calculate the dhash value of an image
    hash = dhash.calculate_hash(image)

    calculate the hamming distance between two images
    hamming_distance = dhash.hamming_distance(image1, image2)

    calculate the hamming distance between two dhash values
    hamming_distance = dhash.hamming_distance(dhash1, dhash2)
    """
    @staticmethod
    def calculate_hash(image):
        """
        calculate the dhash of an image
        :param image: PIL.Image
        :return: dhash (str)
        """
        difference = dhash.__difference(image)
        # 1 => 8, 8 => 16
        decimal_value = 0
        hash_string = ""
        for index, value in enumerate(difference):
            if value:
                decimal_value += value * (2 ** (index % 8))
            if index % 8 == 7:
                # 0xf=>0x0f
                hash_string += str(hex(decimal_value)[2:].rjust(2, "0"))
                decimal_value = 0
        return hash_string

    @staticmethod
    def hamming_distance(first, second):
        """
        calculate hamming distance
        :param first: dhash (str)
        :param second: dhash (str)
        :return: hamming distance
        """
        if isinstance(first, str):
            return dhash.__hamming_distance_with_hash(first, second)

        hamming_distance = 0
        image1_difference = dhash.__difference(first)
        image2_difference = dhash.__difference(second)
        for index, img1_pix in enumerate(image1_difference):
            img2_pix = image2_difference[index]
            if img1_pix != img2_pix:
                hamming_distance += 1
        return hamming_distance

    @staticmethod
    def __difference(image):
        """
        find the difference with image
        :param image: PIL.Image
        :return: difference (int)
        """
        resize_width = 9
        resize_height = 8

        # resize enough to hide the details
        smaller_image = image.resize((resize_width, resize_height))

        # reduce color i.e. convert to grayscale
        grayscale_image = smaller_image.convert("L")

        # difference calculation
        pixels = list(grayscale_image.getdata())
        difference = []
        for row in range(resize_height):
            row_start_index = row * resize_width
            for col in range(resize_width - 1):
                left_pixel_index = row_start_index + col
                difference.append(
                    pixels[left_pixel_index] > pixels[left_pixel_index + 1])
        return difference

    @staticmethod
    def __hamming_distance_with_hash(dhash1, dhash2):
        """
        find difference using 2 dhash values
        :param dhash1: str
        :param dhash2: str
        :return: difference (int)
        """
        difference = (int(dhash1, 16)) ^ (int(dhash2, 16))
        return bin(difference).count("1")


# Own codes

def dhash_dup_filter(im_list):
    """
    :param im_list: image path list.
    :return: im_list with no duplicated images.
    """
    result = list()
    while len(im_list) != 0:
        im = im_list.pop()
        im_list = [i for i in im_list if dhash.hamming_distance(im[1], i[1]) > 10]
        result.append(im)
    return result


def dhash_dup_filter_new(im_list1, im_list2):
    """
    :param im_list1: original image path list. (labeled before additional scrapping.)
    :param im_list2: additionally scraped image path list.
    :return: im_list2 that has no same image compared to im_list1.
    """
    dump = im_list1.copy()
    while len(dump) != 0:
        im = dump.pop()
        im_list2 = [i for i in im_list2 if dhash.hamming_distance(im[1], i[1]) > 10]
    return im_list2


def save_imgs(D: list, root: str, labeled: bool):
    """
    :param D: label path list
    :param root: save root
    :param labeled: flag to identify whether an image has a corresponding label or not. (Filtering has done after some
    labeling.)
    :return: None
    """
    if labeled:
        if 'labeled' not in listdir(root):
            mkdir(root + '/' + 'labeled')
        root = root + '/' + 'labeled'
    for d in D:
        try:
            im = re.search(r'/([^/]+.jpg)$', d[0])[1]
            Image.open(d[0]).save(root + '/' + im)
        except:
            pass
    else:
        if 'unlabeled' not in listdir(root):
            mkdir(root + '/' + 'unlabeled')
            root = root + '/' + 'unlabeled'
        m = len(D)//NUM_PEOPLE
        for i in range(NUM_PEOPLE):
            if i == NUM_PEOPLE - 1:
                temp = D[i * m:]
            else:
                temp = D[i * m: (i+1) * m]
            if f'{i}' not in listdir(root):
                mkdir(root + '/' + f'{i}')
            temproot = root + '/' + f'{i}'
            for d in temp:
                try:
                    im = re.search(r'/([^/]+.jpg)$', d[0])[1]
                    Image.open(d[0]).save(temproot + '/' + im)
                except:
                    pass


def save_labels(D: list, img_names: list, root: str):
    """
    :param D: label path list
    :param img_names: list of image names (xxx(.jpg))
    :param root: save root path
    :return: None
    Img_names is required to check whether label has corresponding image file.
    """
    for label in D:
        lab = re.search(r'/([^/]+).txt$', label)[1]
        if lab in img_names:
            with open(label, 'r') as fp:
                l = fp.read()
            with open(root + '/' + lab + '.txt', 'w') as fp:
                fp.write(l)
