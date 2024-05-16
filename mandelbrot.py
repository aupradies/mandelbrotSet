import matplotlib.pyplot as plt
import numpy as np


def mandelbrot(c, iter_count):
    z = 0
    for n in range(iter_count):
        if abs(z) > 2:
            return n
        z = z * z + c
    return iter_count


def draw_mandelbrot(xmin, xmax, ymin, ymax, width, height, iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    mset = np.zeros((height,width))
    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            mset[i][j] = mandelbrot(c, iter)
    return mset


def init_mandelbrot(width,height,iters):
    xmin, xmax, ymin, ymax = -2.0, 0.6, -1.2, 1.2
    image = draw_mandelbrot(xmin, xmax, ymin, ymax, width, height, iters)
    plt.imshow(image, extent=(xmin, xmax, ymin, ymax), cmap='twilight_shifted')
    plt.colorbar()
    plt.title('The Mandelbrot Set')
    plt.xlabel('Real numbers')
    plt.ylabel('Imaginary numbers')
    plt.show()


def burning_ship(c1, c2, iter_count):
    x, y = 0, 0
    for n in range(iter_count):
        x, y = x*x - y*y + c1, abs(2*x*y) + c2
        if x*x + y*y > 4:
            return n + 1
    return 0


def draw_burning_ship(xmin, xmax, ymin, ymax, width, height, iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    mset = np.zeros((height,width))
    for i in range(height):
        for j in range(width):
            c1 = x[j]
            c2 = y[i]
            mset[i][j] = burning_ship(c1, c2, iter)
    return mset


def init_burning_ship (width,height,iters):
    xmin, xmax, ymin, ymax = -2.0, 1.2, -1.8, 0.8
    image = draw_burning_ship(xmin, xmax, ymin, ymax, width, height, iters)
    plt.imshow(image, extent=(xmin, xmax, ymin, ymax), cmap='hot')
    plt.colorbar()
    plt.title('The Burning Ship')
    plt.xlabel('Real numbers')
    plt.ylabel('Imaginary numbers')
    plt.show()


width, height = 1000, 1000
iters = 150
init_mandelbrot(width, height, iters)
#init_burning_ship(width,height,iters)