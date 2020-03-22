import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import random_shapes


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
fig, axes = plt.subplots(nrows=2, ncols=2)
ax = axes.ravel()

# The generated images can be much more complex. For example, let's try many
# shapes of any color. If we want the colors to be particularly light, we can
# set the `intensity_range` to an upper subrange of (0,255).
#RED
image1, _ = random_shapes((height, width), max_shapes=1, min_size=60, max_size = 60, multichannel=True, num_channels=3, intensity_range=((255, 255),(0,0),(0,0)))

# YELLOW
image2, _ = random_shapes((height, width), max_shapes=1, min_size=60, max_size = 60,multichannel=True, num_channels=3, intensity_range=((255, 255),(255,255),(0,0)))


for i, image in enumerate([image1, image2], 0):
    ax[i].imshow(image)
    ax[i].set_title(f"Colored shapes, #{i}")

# These shapes are well suited to test segmentation algorithms. Often, we
# want shapes to overlap to test the algorithm. This is also possible:
image3, _ = random_shapes((height, width), min_shapes=2, max_shapes=2, intensity_range=((133, 255),(0,255),(0,133)), min_size=60, max_size = 60, allow_overlap=True)
image4, _ = random_shapes((height, width), min_shapes=2, max_shapes=2, intensity_range=((0, 255),(0,255),(0,255)), min_size=60, max_size = 60, allow_overlap=True)

ax[2].imshow(image3)
ax[2].set_title('Overlapping shapes 1')

print(image4[3,3,:])

for i in range(height):
    for j in range(width):
        if np.array_equal(image4[i,j,:], [255,255,255]):
            image4[i,j,:] = image3[i,j,:]

ax[3].imshow(image4)
ax[3].set_title('Overlapping shapes 2')


for a in ax:
    a.set_xticklabels([])
    a.set_yticklabels([])

plt.show()