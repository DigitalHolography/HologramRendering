from matplotlib import pyplot as plt
import numpy as np
from io import StringIO
from PIL import *
import Hologram


z = 0.006
ImageArraySize = np.array([2048, 2048])
nx = ImageArraySize[0]
ny = ImageArraySize[1]


img_infile = open('GaborTarget_SingleImage_XY_D_2048_2048_8bit_e.raw','rb')
img_array = np.fromfile(img_infile, dtype=np.uint8, count=nx*ny)
img = Image.frombuffer("I", [nx, ny],
                            img_array.astype('I'),
                            'raw','I', 0, 1)
plt.imshow(img)
plt.show()

tab_z = np.linspace(0.01, 0.3, 10)
pp = np.zeros()
pp = np.arange(tab_z.size - 1)
z = tab_z[pp]
[OutputField] = Hologram.hologram2FFT(img, nx, ny, 5.5e-6, 5.5e-6, 658e-9, -z)
DisplayedImage = np.abs(OutputField)

plt.imshow(DisplayedImage)

plt.imshow(np.log(np.abs(np.fft.fftshift(np.fft.fft2(img)))))

