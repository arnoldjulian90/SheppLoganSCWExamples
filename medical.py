import math
import numpy as np 
import scipy.interpolate
import scipy.misc
import scipy.ndimage.interpolation
import matplotlib.pyplot as plt

phantom = scipy.misc.imread("Phantom.jpg")

#for x in range(0,180):
plt.imshow(phantom) 
plt.show()

#scipy.misc.imsave("Image.jpg",image)

