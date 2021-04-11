from PIL import Image, ImageDraw

import math

def it_to_color(it, its):
    r = round(255 * it / its)
    # return 255, r, 0 # reds
    # return r, 0, r # purples
    # return 0, r, r # blues
    return 255, r, 0


def in_mandelbrot(x, y, its):
    c = complex(x, y)
    z = 0

    for i in range(its):
        if abs(z) > 2:
            return False, i
        z = z**2 + c
    
    return True, its  


def new_mandelbrot(its=50, zoom=200, x_move=-400, y_move=-400, width=800, height=800):
    img = Image.new('RGB', (width, height))
    pixels = img.load()

    for x in range(img.size[0]):
        print("{:.2f} %".format(x / width * 100.0))
        for y in range(img.size[1]):
            # state, it = in_mandelbrot((x+x_move)/zoom,(y+y_move)/zoom, its)
            state, it = in_mandelbrot(-2+x*4/width, 2-y*4/height, its)
            if state:
                pixels[x, y] = (0, 0, 0)
            else:
                pixels[x, y] = it_to_color(it, its)

    t = ImageDraw.Draw(img)
    t.text((20, 20), 'Mandelbrot set \ni={} \nz={} x={} y={}'.format(its, zoom, x_move, y_move), fill=(255,255,255))

    img.show()

# new_mandelbrot(*convert_coords(50, 269, 205, 98, 311, 200, -400, -400, 800, 800))
new_mandelbrot(its=30, zoom=200)


# del otro programa:
    # def new_mandelbrot(self):
    #     img = Image.new('RGB', (self.width, self.height))

    #     x_dif = self.width // 2
    #     y_dif = self.height // 2

    #     z_values = [[0]*self.width]*self.height

    #     for i in range(self.its):
    #         for x in range(self.width):
    #             for y in range(self.height):
    #                 if img.getpixel((x,y)) == (0,0,0):
    #                     # c = complex((x-x_dif)/200, (y-y_dif)/200)
    #                     # print(c)
    #                     c = complex(-2+x*4/self.width, 2-y*4/self.height)
    #                     z = z_values[y][x]
    #                     # print(z)
    #                     if abs(z) > 2:
    #                         img.putpixel((x, y), self.get_color(i))
    #                     else:
    #                         z_values[y][x] = z ** 2 + c  # A lo mejor el **2 se puede mejorar
    #         img.show()
    #         time.sleep(2)