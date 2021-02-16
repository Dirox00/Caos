from PIL import Image, ImageDraw

import math

def it_to_color(it, its):
    r = round(255 * it / its)
    return 0, r, r

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
            state, it = in_mandelbrot((x+x_move)/zoom,(y+y_move)/zoom, its)
            if state:
                pixels[x, y] = (0, 0, 0)
            else:
                pixels[x, y] = it_to_color(it, its)

    t = ImageDraw.Draw(img)
    t.text((20, 20), 'Mandelbrot set \ni={} \nz={} x={} y={}'.format(its, zoom, x_move, y_move), fill=(255,255,255))

    img.show()

# new_mandelbrot()
# new_mandelbrot(500, 10000, -1400, -9500)
new_mandelbrot(100, 300, -600, -500, width=1920, height=1080)
