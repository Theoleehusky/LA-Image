from PIL import Image
import numpy as np
import math

image = Image.open('images/0.jpg')
image = np.asarray(image)
out = image.copy()
color = {'R': 0, 'G': 1, 'B': 2}

def main():
    global out
    # a function of your choice
    Image.fromarray(out).save('out.jpg', 'JPEG')

def setValue(c, value):
    global out
    i = color[c]
    for row in out:
        for cell in row:
            cell[i] = value

def inverse():
    global out
    for row in out:
        for cell in row:
            for i in range(3):
                cell[i] = 255 - cell[i]

def gray():
    global out
    for row in out:
        for cell in row:
            cell[0] = cell[1] = cell[2] = sum(cell)/3

def blur():
    global out
    height, width = len(image), len(image[0])
    for h in range(height):
        for w in range(width):
            n = 1
            r, g, b = [int(i) for i in image[h][w]]

            if h != 0 and w != 0:
                n += 1
                r += image[h - 1][w - 1][0]
                g += image[h - 1][w - 1][1]
                b += image[h - 1][w - 1][2]
            if h != 0 and w != width - 1:
                n += 1
                r += image[h - 1][w + 1][0]
                g += image[h - 1][w + 1][1]
                b += image[h - 1][w + 1][2]
            if h != height - 1 and w != 0:
                n += 1
                r += image[h + 1][w - 1][0]
                g += image[h + 1][w - 1][1]
                b += image[h + 1][w - 1][2]
            if h != height - 1 and w != width - 1:
                n += 1
                r += image[h + 1][w + 1][0]
                g += image[h + 1][w + 1][1]
                b += image[h + 1][w + 1][2]
            if h != 0:
                n += 1
                r += image[h - 1][w][0]
                g += image[h - 1][w][1]
                b += image[h - 1][w][2]
            if h != height - 1:
                n += 1
                r += image[h + 1][w][0]
                g += image[h + 1][w][1]
                b += image[h + 1][w][2]
            if w != 0:
                n += 1
                r += image[h][w - 1][0]
                g += image[h][w - 1][1]
                b += image[h][w - 1][2]
            if w != width - 1:
                n += 1
                r += image[h][w + 1][0]
                g += image[h][w + 1][1]
                b += image[h][w + 1][2]
            out[h][w][0] = round(r/n)
            out[h][w][1] = round(g/n)
            out[h][w][2] = round(b/n)

def edges():
    global out
    height, width = len(image), len(image[0])
    for h in range(height):
        for w in range(width):
            bx = gx = rx = by = gy = ry = 0
            if h != 0 and w != 0:
                rx += -1 * image[h - 1][w - 1][0]
                ry += -1 * image[h - 1][w - 1][0]
                gx += -1 * image[h - 1][w - 1][1]
                gy += -1 * image[h - 1][w - 1][1]
                bx += -1 * image[h - 1][w - 1][2]
                by += -1 * image[h - 1][w - 1][2]
            if h != 0 and w != width - 1:
                rx += image[h - 1][w + 1][0]
                ry += -1 * image[h - 1][w + 1][0]
                gx += image[h - 1][w + 1][1]
                gy += -1 * image[h - 1][w + 1][1]
                bx += image[h - 1][w + 1][2]
                by += -1 * image[h - 1][w + 1][2]
            if h != height - 1 and w != 0:
                rx += -1 * image[h + 1][w - 1][0]
                ry += image[h + 1][w - 1][0]
                gx += -1 * image[h + 1][w - 1][1]
                gy += image[h + 1][w - 1][1]
                bx += -1 * image[h + 1][w - 1][2]
                by += image[h + 1][w - 1][2]
            if h != height - 1 and w != width - 1:
                rx += image[h + 1][w + 1][0]
                ry += image[h + 1][w + 1][0]
                gx += image[h + 1][w + 1][1]
                gy += image[h + 1][w + 1][1]
                bx += image[h + 1][w + 1][2]
                by += image[h + 1][w + 1][2]
            if h != 0:
                ry += -2 * image[h - 1][w][0]
                gy += -2 * image[h - 1][w][1]
                by += -2 * image[h - 1][w][2]
            if h != height - 1:
                ry += 2 * image[h + 1][w][0]
                gy += 2 * image[h + 1][w][1]
                by += 2 * image[h + 1][w][2]
            if w != 0:
                rx += -2 * image[h][w - 1][0]
                gx += -2 * image[h][w - 1][1]
                bx += -2 * image[h][w - 1][2]
            if w != width - 1:
                rx += 2 * image[h][w + 1][0]
                gx += 2 * image[h][w + 1][1]
                bx += 2 * image[h][w + 1][2]

            out[h][w][0] = min(round(math.sqrt(rx ** 2 + ry ** 2)), 255)
            out[h][w][1] = min(round(math.sqrt(gx ** 2 + gy ** 2)), 255)
            out[h][w][2] = min(round(math.sqrt(bx ** 2 + by ** 2)), 255)

if __name__ == '__main__':
    main()