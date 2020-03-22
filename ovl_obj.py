import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import random_shapes
from skimage.io import imsave

height, width = 128, 128
channels = 3

# Let's start simple and generate a 128x128 image
# with a single grayscale rectangle.
result = random_shapes((height, width), max_shapes=1, shape='rectangle',
                       multichannel=False, random_seed=0)

# We get back a tuple consisting of (1) the image with the generated shapes
# and (2) a list of label tuples with the kind of shape (e.g. circle,
# rectangle) and ((r0, r1), (c0, c1)) coordinates.
image, labels = result
print(f"Image shape: {image.shape}\nLabels: {labels}")

# We can visualize the images.
fig, axes = plt.subplots(nrows=1, ncols=2)
ax = axes.ravel()

# These shapes are well suited to test segmentation algorithms. Often, we
# want shapes to overlap to test the algorithm. This is also possible:
image1, _ = random_shapes((height, width), min_shapes=1, max_shapes=1, intensity_range=((200, 200),(30,30),(145,145)), min_size=100, max_size = 100, allow_overlap=True)
image2, _ = random_shapes((height, width), min_shapes=1, max_shapes=1, intensity_range=((40, 40),(210,210),(90,90)), min_size=50, max_size = 50, allow_overlap=True)

ax[0].imshow(image1)
ax[0].set_title('Shape 1')

for i in range(height):
    for j in range(width):
        if np.array_equal(image2[i,j,:], [255,255,255]):
            image2[i,j,:] = image1[i,j,:]

ax[1].imshow(image2)
ax[1].set_title('Overlapping shapes')

#save a png file including the 2 overlapped objects
imsave("54.png", image2)


for a in ax:
    a.set_xticklabels([])
    a.set_yticklabels([])

plt.show()