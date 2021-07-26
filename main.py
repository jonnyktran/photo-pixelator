from PIL import Image, ImageDraw
import numpy as np
import sys


def load_img(filename):
    pil_img = Image.open(filename)
    arr = np.array(pil_img.getdata(), dtype=np.uint8).reshape(pil_img.height, pil_img.width, 3)
    img = [[(p[0], p[1], p[2]) for p in row] for row in arr]
    return img


def save_img(img, filename):
    arr = np.asarray(img, dtype=np.uint8)
    pil_img = Image.fromarray(arr)
    pil_img.save(filename, format='jpeg')


def average_list(tuple_list):
    length = len(tuple_list)
    a = [p[0] for p in tuple_list]
    b = [p[1] for p in tuple_list]
    c = [p[2] for p in tuple_list]
    avg_tuple = (sum(a) / length, sum(b) / length, sum(c) / length)
    return avg_tuple


def pixelator(file_path, pixel_size):
    img = load_img(file_path)

    pixel_size = int(pixel_size)

    height, width = len(img), len(img[0])
    square = int(height / pixel_size)
    square2 = int(width / pixel_size)

    for k in range(square):
        for m in range(square2):
            list_tuple = []
            for i in range(pixel_size):
                for j in range(pixel_size):
                    list_tuple.append(img[k * pixel_size + i][m * pixel_size + j])
            avg_tuple = average_list(list_tuple)
            for i in range(pixel_size):
                for j in range(pixel_size):
                    img[k * pixel_size + i][m * pixel_size + j] = avg_tuple


    arr = np.asarray(img, dtype=np.uint8)
    final_img = Image.fromarray(arr)
    return final_img

