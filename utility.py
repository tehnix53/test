import cv2
import numpy as np
from PIL import Image, ImageOps


def add_colored_dilate(image, mask_image, dilate_image):
    mask_image_gray = cv2.cvtColor(mask_image, cv2.COLOR_BGR2GRAY)
    dilate_image_gray = cv2.cvtColor(dilate_image, cv2.COLOR_BGR2GRAY)

    mask = cv2.bitwise_and(mask_image, mask_image, mask=mask_image_gray)
    dilate = cv2.bitwise_and(dilate_image, dilate_image, mask=dilate_image_gray)

    mask_coord = np.where(mask != [0, 0, 0])
    dilate_coord = np.where(dilate != [0, 0, 0])

    mask[mask_coord[0], mask_coord[1], :] = [255, 0, 0]
    dilate[dilate_coord[0], dilate_coord[1], :] = [0, 0, 255]

    ret = cv2.addWeighted(image, 0.7, dilate, 0.3, 0)
    ret = cv2.addWeighted(ret, 0.7, mask, 0.3, 0)

    return ret


def add_colored_mask(image, mask_image):
    image = cv2.imread(image)
    mask_image = cv2.imread(mask_image)
    mask_image_gray = cv2.cvtColor(mask_image, cv2.COLOR_BGR2GRAY)

    mask = cv2.bitwise_and(mask_image, mask_image, mask=mask_image_gray)

    mask_coord = np.where(mask != [0, 0, 0])

    mask[mask_coord[0], mask_coord[1], :] = [255, 0, 0]

    ret = cv2.addWeighted(image, 0.7, mask, 0.3, 0)

    return ret


def diff_mask(ref_image, mask_image):
    ref_image = cv2.imread(ref_image)
    mask_image = cv2.imread(mask_image)

    mask_image_gray = cv2.cvtColor(mask_image, cv2.COLOR_BGR2GRAY)

    mask = cv2.bitwise_and(mask_image, mask_image, mask=mask_image_gray)

    mask_coord = np.where(mask != [0, 0, 0])

    mask[mask_coord[0], mask_coord[1], :] = [250, 0, 0]

    ret = cv2.addWeighted(ref_image, 0.7, mask, 0.3, 0)
    return ret


def add_colored_plt(path_to_image, path_to_small_plt):
    def drop_empty_background(some_dim):
        arr = np.asarray(some_dim)
        empty_val = arr[0][0]
        clean_arr = np.where(arr == empty_val, 0, arr)
        return Image.fromarray(clean_arr)

    shapes = np.asarray(Image.open(path_to_image)).shape
    plot = Image.open(path_to_small_plt)
    plot = plot.resize(shapes, Image.ANTIALIAS)

    r, g, b, a = plot.split()

    r_clean = drop_empty_background(r)
    g_clean = drop_empty_background(g)
    b_clean = drop_empty_background(b)

    img = Image.open(path_to_image)
    img = ImageOps.invert(img)

    merge = Image.merge('RGBA', (r_clean, g_clean, b_clean, img))

    background = Image.new("RGB", merge.size, (255, 255, 255))

    background.paste(merge, mask=merge.split()[3])

    return background
