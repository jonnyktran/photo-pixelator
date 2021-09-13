from PIL import Image
from scipy.spatial.distance import cdist
import numpy as np

RESURRECT64_PALETTE = [(46, 34, 47),  # bastille
                       (62, 53, 70),  # ship gray
                       (98, 85, 101),  # salt box
                       (150, 108, 108),  # copper rose
                       (171, 148, 122),  # sandrift
                       (105, 79, 98),  # don juan
                       (127, 112, 138),  # mobster
                       (155, 171, 178),  # hit gray
                       (199, 220, 208),  # paris white
                       (255, 255, 255),  # white
                       (110, 39, 39),  # nutmeg
                       (179, 56, 49),  # well read
                       (234, 79, 54),  # cinnabar
                       (245, 125, 74),  # jaffa
                       (174, 35, 52),  # mexican red
                       (232, 59, 59),  # cinnabar
                       (251, 107, 29),  # orange
                       (247, 150, 23),  # tree poppy
                       (249, 194, 43),  # saffron
                       (122, 48, 69),  # solid pink
                       (158, 69, 57),  # el salva
                       (205, 104, 61),  # raw sienna
                       (230, 144, 78),  # burnt sienna
                       (251, 185, 84),  # saffron mango
                       (76, 62, 36),  # lisbon brown
                       (103, 102, 51),  # costa del sol
                       (162, 169, 71),  # husk
                       (213, 224, 75),  # wattle
                       (251, 255, 134),  # dolly
                       (22, 90, 76),  # green pea
                       (35, 144, 99),  # eucalyptus
                       (30, 188, 115),  # mountain meadow
                       (145, 219, 105),  # pastel green
                       (205, 223, 108),  # yellow green
                       (49, 54, 56),  # outer space
                       (55, 78, 74),  # mineral green
                       (84, 126, 100),  # como
                       (146, 169, 132),  # sage
                       (178, 186, 144),  # swamp green
                       (11, 94, 101),  # deep sea green
                       (11, 138, 143),  # blue chill
                       (14, 175, 155),  # niagara
                       (48, 225, 185),  # turquoise
                       (143, 248, 226),  # aquamarine
                       (50, 51, 83),  # martinique
                       (72, 74, 119),  # east bay
                       (77, 101, 180),  # san marino
                       (77, 155, 230),  # picton blue
                       (143, 211, 255),  # anakiwa
                       (69, 41, 63),  # livid brown
                       (107, 62, 117),  # affair
                       (144, 94, 169),  # wisteria
                       (168, 132, 243),  # portage
                       (234, 173, 237),  # french lilac
                       (117, 60, 84),  # cosmic
                       (162, 75, 111),  # cadillac
                       (207, 101, 127),  # charm
                       (237, 128, 153),  # carissma
                       (131, 28, 93),  # disco
                       (195, 36, 84),  # maroon flush
                       (240, 79, 120),  # french rose
                       (246, 129, 129),  # froly
                       (252, 167, 144),  # mona lisa
                       (253, 203, 176)]  # light apricot


# Convert image into a numpy array of RGB values
def load_img(filename):
    pil_img = Image.open(filename)
    return np.array(pil_img.getdata(), dtype=np.uint8).reshape(pil_img.height, pil_img.width, 3)


# Compute average RGB value from a list of RGB values
def average_color(rgb_list):
    length = len(rgb_list)
    r = [c[0] for c in rgb_list]
    g = [c[1] for c in rgb_list]
    b = [c[2] for c in rgb_list]
    return (sum(r) / length, sum(g) / length, sum(b) / length)


# Find closest color from the palette array
def closest_color(rgb_tuple, palette_arr):
    rgb_tuple_array = np.asarray(rgb_tuple).reshape(1, -1)
    return RESURRECT64_PALETTE[cdist(rgb_tuple_array, palette_arr).argmin()]


# Pixelate image based on a given pixel size
def pixelator(file_path, pixel_size):
    img_arr = load_img(file_path)
    palette_arr = np.asarray(RESURRECT64_PALETTE)

    height, width, pixel_size = len(img_arr), len(img_arr[0]), int(pixel_size)
    square_h, square_w = int(height / pixel_size)+1, int(width / pixel_size)+1

    for k in range(square_h):
        for m in range(square_w):
            index_list = [(k * pixel_size + i, m * pixel_size + j)
                          for j in range(pixel_size)
                          for i in range(pixel_size)
                          if (k * pixel_size + i) < height and (m * pixel_size + j) < width]

            rgb_list = [img_arr[index_tuple[0]][index_tuple[1]]
                        for index_tuple in index_list]

            if len(rgb_list) < 1:
                continue

            avg_color = average_color(rgb_list)
            color = closest_color(avg_color, palette_arr)

            for index_tuple in index_list:
                img_arr[index_tuple[0]][index_tuple[1]] = color

    return Image.fromarray(img_arr)
