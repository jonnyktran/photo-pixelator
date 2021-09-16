from PIL import Image
import numpy as np
from numba import njit

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


# Convert image into numpy array of RGB values
def load_img(filename):
    pil_img = Image.open(filename)
    max_size = (1280, 1280)
    pil_img.thumbnail(max_size, Image.LANCZOS)
    return np.array(pil_img.getdata(), dtype=np.uint8).reshape(pil_img.height, pil_img.width, 3)


# Assign each pixel average color of its square and return True if no valid pixels
@njit(fastmath=True)
def assign_average_color(square_row, square_col, height, width, pixel_size, img_arr):
    row_start, col_start = square_row * pixel_size, square_col * pixel_size

    # Compute average RGB value of square
    r, g, b, num_pixels = 0, 0, 0, 0
    for row in range(pixel_size):
        if (row_start + row) >= height:
            break
        for col in range(pixel_size):
            if (col_start + col) >= width:
                break
            rgb = img_arr[row_start + row][col_start + col]
            r += rgb[0]
            g += rgb[1]
            b += rgb[2]
            num_pixels += 1

    if num_pixels < 1:
        return True

    avg_color = (r / num_pixels, g / num_pixels, b / num_pixels)

    # Assign average color to all pixels in square
    for row in range(pixel_size):
        if (row_start + row) >= height:
            break
        for col in range(pixel_size):
            if (col_start + col) >= width:
                break
            img_arr[row_start + row][col_start + col] = avg_color


# Pixelate image based on given pixel size
def pixelator(file_path, pixel_size):
    img_arr = load_img(file_path)
    height, width, pixel_size = len(img_arr), len(img_arr[0]), int(pixel_size)

    # Create PIL image in mode 'P' using color palette
    palette_list = list(sum(RESURRECT64_PALETTE, ()))
    palette_img = Image.new('P', (8, 8))
    palette_img.putpalette(palette_list)

    # Skip extra computation when pixel size is 1
    if pixel_size == 1:
        pixel_img = Image.fromarray(img_arr)
        pixel_img = pixel_img.quantize(palette=palette_img, dither=0)
        return pixel_img.convert('RGB')

    # Divide image into squares based on pixel size
    square_h, square_w = height//pixel_size + 1, width//pixel_size + 1
    for square_row in range(square_h):
        for square_col in range(square_w):
            # Assign each pixel average color of its square
            no_valid_pixels = assign_average_color(square_row, square_col, height, width, pixel_size, img_arr)
            if no_valid_pixels:
                break

    # Use PIL quantize to assign each pixel nearest color from palette
    pixel_img = Image.fromarray(img_arr)
    pixel_img = pixel_img.quantize(palette=palette_img, dither=0)
    return pixel_img.convert('RGB')
