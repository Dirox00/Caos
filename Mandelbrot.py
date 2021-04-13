from PIL import Image, ImageDraw

import math

import time


class Mandelbrot:
    def __init__(self, region):  #region = (-2.25, 1.5, 3, 3) 
        self.its = 50
        self.size = (600, 600)
        self.region = region
        # self.region = (-2, 2, 2, -2)
        # self.coords = (0, 0, 800, 800)

        # self.x_interval = abs(self.region[0]) + abs(self.region[2])
        # self.y_interval = abs(self.region[1]) + abs(self.region[3])

    def zoom(self, coords):
        """
        coords: (x0, y0, +x, +y)
        """
        new_x0 = self.region[0] + coords[0]*self.region[2]/self.size[0]
        new_y0 = self.region[1] - coords[1]*self.region[3]/self.size[1]
        new_x_interval = coords[2]*self.region[2]/self.size[0]
        new_y_interval = coords[3]*self.region[3]/self.size[1]

        # return (new_x0, new_y0, new_x_interval, new_y_interval)
        self.region = (new_x0, new_y0, new_x_interval, new_y_interval)
        
    
    def get_color(self, it):
        r = round(255 * it / self.its)
        
        return 255, r, 0

    def in_mandelbrot(self, x, y):
        c = complex(x, y)
        z = 0

        for i in range(self.its):
            if abs(z) > 2:
                return False, i
            z = z**2 + c
        
        return True, self.its  

    def new_mandelbrot(self):   #def show(self):
        width, height = self.size

        img = Image.new('RGB', self.size)

        for x in range(width):
            for y in range(height):
                state, it = self.in_mandelbrot(self.region[0]+x*self.region[2]/width, self.region[1]-y*self.region[3]/height)
                if state:
                    img.putpixel((x, y), (0, 0, 0))
                else:
                    img.putpixel((x, y), self.get_color(it))
        
        img.show()
                
"""
        def reset(self):
            self.its = 50
            self.size = (600, 600)
            self.region = (-2.25, 1.5, 3, 3)
"""       
        
    
"""
        def save(self, name):
            width, height = self.size

            img = Image.new('RGB', self.size)

            for x in range(width):
                for y in range(height):
                    state, it = self.in_mandelbrot(self.region[0]+x*self.region[2]/width, self.region[1]-y*self.region[3]/height)
                    if state:
                        img.putpixel((x, y), (0, 0, 0))
                        # pixels[x, y] = (0, 0, 0)
                    else:
                        img.putpixel((x, y), self.get_color(it))
                        # pixels[x, y] = self.get_color(it)
        
        img.save(name+".png")
"""


mand = Mandelbrot((-2, 2, 4, 4))
mand.new_mandelbrot()

mand.zoom((180, 350, 14, 14))
# mand.new_mandelbrot()

mand.zoom((450, 147, 29, 29))
# mand.new_mandelbrot()
# print(new)
# m2 = Mandelbrot(new)

# new2 = m2.zoom((375, 103, 40, 40))
# print(new2)
# m3 = Mandelbrot(new2)
# m3.new_mandelbrot()
