from PIL import Image, ImageDraw

import math

from matplotlib import colors

class Mandelbrot:
    def __init__(self, region = (-2.25, 1.5, 3, 3)): 
        self.its = 50
        self.size = (600, 600)
        self.region = region
        self.states=[region]
        self.step=0
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
        self.states.append(self.region)
        self.step += 1
        
    
    def zoom_point(self, point, scale=40):
        width = self.size[0] // scale
        height = self.size[1] // scale
        return self.zoom((point[0]-width//2, point[1]-height//2, width, height))
        
    
    def step_back(self):
        self.step -= 1
        self.region=self.states[self.step]
        

    def step_forward(self):
        self.step += 1
        self.region=self.states[self.step]
        
        
    def get_color_rgb(self, it):
        r = round(255 * it / self.its)
        
        return 255, r, 0
    
    
    def get_color_hsv(self, it):
        r = round(255 * it / self.its)
        if it<self.its:
            value=255
        else:
            value=0
        
        return round((r*1)%255), 255, value    

    """
    def continuous_coloring(self, it, z):
        v = it - math.log2(math.log(z)/math.log(2))

        return colors.hsv_to_rgb(v)
    
    """
    
    def in_mandelbrot(self, x, y):
        c = complex(x, y)
        z = 0
        #z_abs = 0

        for i in range(self.its):
            #z_abs = abs(z)
            if abs(z) > 2:
                return False, i- math.log2(math.log(abs(z))/math.log(2))
            z = z**2 + c
        
        return True, self.its, #z_abs

    
    def show_hsv(self):   #def show(self):
        width, height = self.size

        img = Image.new('HSV', self.size)  # Image.new('RGB', self.size)

        for x in range(width):
            for y in range(height):
                state, it = self.in_mandelbrot(self.region[0]+x*self.region[2]/width, self.region[1]-y*self.region[3]/height)   #state, it, zi = ...
                if state:
                    img.putpixel((x, y), (0, 0, 0))
                else:
                    # img.putpixel((x, y), self.get_color(it))
                    img.putpixel((x, y), self.get_color_hsv(it))  #self.continuous_coloring(it, zi)
        
        img.show()
        
        
    def show_rgb(self):   #def show(self):
        width, height = self.size

        img = Image.new('RGB', self.size)  # Image.new('RGB', self.size)

        for x in range(width):
            for y in range(height):
                state, it = self.in_mandelbrot(self.region[0]+x*self.region[2]/width, self.region[1]-y*self.region[3]/height)   #state, it, zi = ...
                if state:
                    img.putpixel((x, y), (0, 0, 0))
                else:
                    # img.putpixel((x, y), self.get_color(it))
                    img.putpixel((x, y), self.get_color_rgb(it))  #self.continuous_coloring(it, zi)
        
        img.show()
                

    def reset(self):
        self.its = 50
        self.size = (600, 600)
        self.region = (-2.25, 1.5, 3, 3) 
        self.step=0
        
    
    def save_rgb(self, name):
        width, height = self.size

        img = Image.new('RGB', self.size)

        for x in range(width):
            for y in range(height):
                state, it = self.in_mandelbrot(self.region[0]+x*self.region[2]/width, self.region[1]-y*self.region[3]/height)
                if state:
                    img.putpixel((x, y), (0, 0, 0))
                    # pixels[x, y] = (0, 0, 0)
                else:
                    img.putpixel((x, y), self.get_color_rgb(it))
                    # pixels[x, y] = self.get_color(it)
        
        img.save(name+".png")
        
        
    def save_hsv(self, name):   
        width, height = self.size

        img = Image.new('HSV', self.size)

        for x in range(width):
            for y in range(height):
                state, it = self.in_mandelbrot(self.region[0]+x*self.region[2]/width, self.region[1]-y*self.region[3]/height)
                if state:
                    img.putpixel((x, y), (0, 0, 0))
                    # pixels[x, y] = (0, 0, 0)
                else:
                    img.putpixel((x, y), self.get_color_hsv(it))
                    # pixels[x, y] = self.get_color(it)
        
        img_rgb=img.convert("RGB")
        img_rgb.save(name+".png")  
        
         
    def save_state(self, name):
        saved_state = open(name+".txt", "w")
        for i in range (4):
            saved_state.write(str(self.region[i]) + "\n")
        saved_state.write(str(self.its))
        saved_state.close()
       

    def import_state(self, file):
        try:
            state = open(file, "r")
            coords = []
            for i in range (4):
                coords.append(float(state.readline()))
            self.region = coords
            self.its=int(state.readline())
            self.states.append(self.region)
            self.step += 1
            state.close()
        except:
            return False
        

if __name__ == "__main__":
    mand = Mandelbrot((-2, 2, 4, 4))
    # mand.show_hsv()
    mand.save_hsv("try2")

    # mand.zoom((180, 350, 14, 14))
    # # mand.new_mandelbrot()

    # mand.zoom((450, 147, 29, 29))
    # mand.new_mandelbrot()
    # print(new)
    # m2 = Mandelbrot(new)

    # new2 = m2.zoom((375, 103, 40, 40))
    # print(new2)
    # m3 = Mandelbrot(new2)
    # m3.new_mandelbrot()

    # mand.zoom_point((98,290))
    # mand.new_mandelbrot()
