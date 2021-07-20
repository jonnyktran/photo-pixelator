from PIL import Image
import numpy as np
import sys


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def load_img(filename):
    pil_img = Image.open(filename)
    arr = np.array(pil_img.getdata(), dtype=np.uint8).reshape(pil_img.height, pil_img.width, 3)
    img = [[(p[0], p[1], p[2]) for p in row] for row in arr]
    return img


def save_img(img, filename):
    arr = np.asarray(img, dtype=np.uint8)
    pil_img = Image.fromarray(arr)
    pil_img.save(filename, format='jpeg')


def average(tuple1, tuple2):
    list_tuple = []
    for i in range(len(tuple1)):
        list_tuple.append((tuple1[i] + tuple2[i]) / 2)
    return tuple(list_tuple)


def average_list(tuple_list):
    length = len(tuple_list)
    a = [p[0] for p in tuple_list]
    b = [p[1] for p in tuple_list]
    c = [p[2] for p in tuple_list]
    avg_tuple = (sum(a) / length, sum(b) / length, sum(c) / length)
    return avg_tuple


def north(img, pixel, i, j):
    if i <= 0:
        return
    north_pixel = img[i - 1][j]
    change = average(pixel, north_pixel)
    img[i][j] = change


def south(img, pixel, i, j):
    if i >= len(img) - 1:
        return
    south_pixel = img[i + 1][j]
    change = average(pixel, south_pixel)
    img[i][j] = change


def east(img, pixel, i, j):
    if j >= len(img[i]) - 1:
        return
    east_pixel = img[i][j + 1]
    change = average(pixel, east_pixel)
    img[i][j] = change


def west(img, pixel, i, j):
    if j <= 0:
        return
    west_pixel = img[i][j - 1]
    change = average(pixel, west_pixel)
    img[i][j] = change


def main():
    args = sys.argv[1:]
    pixel_size = int(input('Enter pixel size: '))
    img = load_img(args[0])
    #for i in range(len(img)):
    #    for j in range(len(img[i])):
     #       pixel = img[i][j]
     #       north(img, pixel, i, j)
      #      south(img, pixel, i, j)
      #      east(img, pixel, i, j)
      #      west(img, pixel, i, j)

    height, width = len(img), len(img[0])
    square = int(height / pixel_size)
    square2 = int(width / pixel_size)

    for k in range(square):
        for l in range(square2):
            list_tuple = []
            for i in range(pixel_size):
                for j in range(pixel_size):
                    list_tuple.append(img[k * pixel_size + i][l * pixel_size + j])
            avg_tuple = average_list(list_tuple)
            for i in range(pixel_size):
                for j in range(pixel_size):
                    img[k * pixel_size + i][l * pixel_size + j] = avg_tuple

    name = input("Enter just the name of your file: ")
    filename = str(name) + '.jpeg'
    arr = np.asarray(img, dtype=np.uint8)
    pil_img = Image.fromarray(arr)
    pil_img.show()
    #save_img(img, filename)

main()
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print('Hi')
