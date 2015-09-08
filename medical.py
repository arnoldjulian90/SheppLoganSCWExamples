import math
import numpy as np 
import scipy.interpolate
import scipy.misc
import scipy.ndimage.interpolation
import matplotlib.pyplot as plt

phantom = scipy.misc.imread("Phantom.jpg")
plt.imshow(phantom)
plt.show()
for x in range(0,180):
	rotatedImage = scipy.ndimage.interpolation.rotate(phantom,1,3, 
reshap=False, mode= 'constant', cval=0)




