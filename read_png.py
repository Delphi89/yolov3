#import from scikit
import numpy as np
from skimage.io import imsave, imread
from skimage import data, io, filters

obj_number = 2
channels = 3

s = (obj_number, channels)
obj = np.zeros(s)

#define the colors for each object in RGB form 
obj[0,:] = [200, 30, 145]
obj[1,:] = [40, 210, 90] 
#(200, 200),(30,30),(145,145)
#(40, 40),(210,210),(90,90)

#read an image called 54.jpg
rgb_image = imread("54.png")

#print resolution and number of channels
print("Height, Width, RGB:")
print(rgb_image.shape) 

#read height, width, rgb in separate variables
height, width, rgb = rgb_image.shape
print(height, width, rgb)

#enable area counters
count = np.zeros(obj_number);

# for the number of objects defined, search for the colors defined  
for p in range(obj_number):
        for j in range(width):
            for k in range(height):
                for i in range(channels):
                    if (rgb_image[j,k,i] == obj[p,i]):
                        count[p] = count[p] + 1;

# print area (number of pixels that match the rule) of each object
for p in range(obj_number):
    print("object ", p, "  area: ",count[p]/3);
    
#show the image
io.imshow(rgb_image)
io.show()
                