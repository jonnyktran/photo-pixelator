from PIL import Image
from scipy.spatial.distance import cdist
import numpy as np

BASIC_PALETTE = [(92,39,94), # purple
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

HORIZON_PALETTE = [(109,247,193), # mint
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

PICO_PALETTE = [(0,0,0), # black
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

POKEMON_PALETTE = [(130,200,214), # aqua blue
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
                   (13,66,95), # Eastern blue
                   (209,175,84), # mustard
                   (31,119,35)] # shaded green

ALL_PALETTE = BASIC_PALETTE + HORIZON_PALETTE + PICO_PALETTE + POKEMON_PALETTE


def load_img(filename):
    pil_img = Image.open(filename)
    return np.array(pil_img.getdata(), dtype=np.uint8).reshape(pil_img.height, pil_img.width, 3)


def average_list(tuple_list):
    length = len(tuple_list)
    r = [p[0] for p in tuple_list]
    g = [p[1] for p in tuple_list]
    b = [p[2] for p in tuple_list]
    return (sum(r) / length, sum(g) / length, sum(b) / length)


def closest_color(avg_tuple, palette_arr):
    avg_tuple_array = np.asarray(avg_tuple).reshape(1, -1)
    return ALL_PALETTE[cdist(avg_tuple_array, palette_arr).argmin()]


def pixelator(file_path, pixel_size):
    img_arr = load_img(file_path)
    palette_arr = np.asarray(ALL_PALETTE)

    height, width, pixel_size = len(img_arr), len(img_arr[0]), int(pixel_size)
    square_h, square_w = int(height / pixel_size)+1, int(width / pixel_size)+1

    for k in range(square_h):
        for m in range(square_w):
            index_list = [(k * pixel_size + i, m * pixel_size + j)
                          for j in range(pixel_size)
                          for i in range(pixel_size)
                          if (k * pixel_size + i) < height and (m * pixel_size + j) < width]

            tuple_list = [img_arr[index_tuple[0]][index_tuple[1]]
                          for index_tuple in index_list
                          if index_tuple[0] < height and index_tuple[1] < width]

            if len(tuple_list) < 1:
                continue

            avg_tuple = average_list(tuple_list)
            color = closest_color(avg_tuple, palette_arr)

            for index_tuple in index_list:
                if index_tuple[0] < height and index_tuple[1] < width:
                    img_arr[index_tuple[0]][index_tuple[1]] = color

    return Image.fromarray(img_arr)
 