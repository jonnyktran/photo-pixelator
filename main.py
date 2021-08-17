
from PIL import Image
import numpy as np
import math


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


basic_palette = [(92,39,94), # purple
                 (177,62,83), # red
                 (239,125,88), # orange
                 (255,205,117), # yellow
                 (167,240,111), # light green
                 (38,113,122), # teal
                 (41,54,111), # navy
                 (60,93,201), # dark blue
                 (66,166,246), # light blue
                 (116,239,247), # cyan
                 (244,244,244), # white
                 (148,176,194), # light gray
                 (85,108,134), # dark gray
                 (51,60,87), # blue gray
                 (254,255,255)] # white

horizon_palette = [(109,247,193), # mint
                   (14,173,193), # teal
                   (95,108,129), # gray
                   (58,52,87), # navy purple
                   (161,229,90), # yellow green
                   (247,228,118), # yellow
                   (249,147,81), # orange
                   (203,77,103), # violet red
                   (106,56,113), # purple
                   (202,37,100), # magenta
                   (244,140,182), # pink
                   (246,182,158)] # salmon

pico_palette = [(0,0,0), # black
                (29,43,83), # navy
                (126,38,82), # burgundy
                (171,82,54), # light brown
                (97,86,79), # pine cone
                (192,195,199), # silver
                (255,241,232), # beige
                (255,0,77), # red
                (255,163,1), # orange
                (255,236,36), # yellow
                (0,228,55), # light green
                (42,172,255), # sky blue
                (132,118,156), # faded purple
                (254,119,168), # pink
                (255,204,171)] # tan

pokemon_palette = [(130,200,214), # aqua blue
                   (189,32,32), # blood red
                   (180,99,34), # cafe brown
                   (207,131,43), # light brown
                   (255,238,168), # cream yellow
                   (98,150,161), # teal
                   (199,199,199), # silver
                   (6,86,120), # darker blue
                   (118,228,255), # sky blue
                   (82,228,129), # mint green
                   (217,255,156), # yellow green
                   (137,82,2), # medium dark brown
                   (195,162,111), # white brown
                   (255,235,1), # vibrant yellow
                   (255,44,1), # fire red
                   (248,133,12), # fire orange
                   (147,147,147), # gray
                   (81,81,81), # dark gray
                   (46,108,107), # dark teal
                   (3,121,255), # royal blue
                   (210,17,38), # vampire red
                   (0,0,0), # black
                   (255, 255, 255), # white
                   (216,165,102), # tan
                   (48,171,154), # aqua green
                   (108,109,81), # camoflage green
                   (175,133,95), # mocha brown
                   (121,112,177), # ghostly purple
                   (126,162,210), # purple blue
                   (179,177,209), # light purple
                   (67,63,62), # gray black
                   (168,55,176), # royal purple
                   (196,106,209), # purple
                   (245,197,236), # light pink
                   (97,208,225), # cerulean
                   (37,195,167), # pastel green
                   (97,208,225), # blue
                   (165,156,141), # tan
                   (255,154,176), # hot pink
                   (255,1,139), # magenta
                   (255,176,3), # gold
                   (167,255,217), # bright mint
                   (165,253,255), # bright blue
                   (135,45,47), # red brown
                   (246,239,193), # beige
                   (245,209,69), # pikachu yellow
                   (224,94,70), # pikachu salmon
                   (103,166,200), # pikachu blue
                   (115,187,152), # dark mint
                   (105,26,43), # dark red
                   (13,66,95), # screen blue
                   (209,175,84), # mustard
                   (31,119,35)] # shaded green

all_palette = basic_palette + horizon_palette + pico_palette + pokemon_palette


def closest_color(avg):
    d = -1 # error
    color = () # color tuple

    for c in all_palette:
        tuple_subtract = (avg[0] - c[0], avg[1] - c[1], avg[2] - c[2])

        error = (tuple_subtract[0] ** 2) + (tuple_subtract[1] ** 2) +  (tuple_subtract[2] ** 2)
        error = math.sqrt(error)

        if (d == -1 or error < d):
            d = error
            color = c

    return color


def pixelator(file_path, pixel_size):
    img = load_img(file_path)
    pixel_size = int(pixel_size)

    height, width = len(img), len(img[0])

    square = int(height / pixel_size)
    square2 = int(width / pixel_size)

    for k in range(square + 1):
        for m in range(square2 + 1):
            list_tuple = []
            for i in range(pixel_size):
                for j in range(pixel_size):
                    if (k * pixel_size + i) < height and (m * pixel_size + j) < width:
                        list_tuple.append(img[k * pixel_size + i][m * pixel_size + j])
            if len(list_tuple) < 1:
                continue
            avg_tuple = average_list(list_tuple)
            color = closest_color(avg_tuple)
            for i in range(pixel_size):
                for j in range(pixel_size):
                    if (k * pixel_size + i) < height and (m * pixel_size + j) < width:
                        img[k * pixel_size + i][m * pixel_size + j] = color

    arr = np.asarray(img, dtype=np.uint8)
    final_img = Image.fromarray(arr)
    return final_img

