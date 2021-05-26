from matplotlib import pyplot as plt
import numpy as np
from io import StringIO
from PIL import Image
import Hologram
import holo
import struct
import math

# z = 0.06

ImageArraySize = np.array([1024, 1024])
# ImageArraySize = np.array([2048, 2048])
nx, ny = ImageArraySize


# Lecture fichier .
img_infile = open('GaborTarget_SingleImage_XY_D_2048_2048_8bit_e.raw', 'rb')
img_array = np.fromfile(img_infile, dtype=np.uint8, count=nx*ny)
img = Image.frombuffer("I", [nx, ny],
                            img_array.astype('I'),
                            'raw','I', 0, 1)


# img = holo.FileReader('Mire_negative_position_.holo').get_all_frames()

data = holo.FileReader('Mire_negative_position_80.holo').get_all_frames() #ici tu mets le nom du fichier que tu veux ouvrir
data_reshape_1 = np.reshape(data[:, 0], (1024, 1024), order='C') #dans data[:, 0] ça veut dire que tu prends la première image du film (correspond à l'indice 0)
                                                              #(1024, 1024) c'est les dimensions des images, attention il faut les choisir intelligement les dimensions sont écrits dans le header normalement
# plt.imshow(np.rot90(np.flipud(data_reshape_1), 4), aspect='auto', interpolation='none', origin='lower') #ça c'est juste pour afficher
# plt.show()

data_reshape_2 = np.reshape(data[:, 1], (1024, 1024), order='C')
data_reshape_3 = np.reshape(data[:, 2], (1024, 1024), order='C')
data_reshape_4 = np.reshape(data[:, 3], (1024, 1024), order='C')
data_reshape_1 = data_reshape_1.astype("complex128")
data_reshape_2 = data_reshape_2.astype("complex128")
data_reshape_3 = data_reshape_3.astype("complex128")
data_reshape_4 = data_reshape_4.astype("complex128")
# plt.imshow(data_reshape)
# plt.title('interferogram')
# plt.show()

image = np.reshape(data[:, 0], (1024, 1024), order='C')


# Démodulation temporelle
I0 = 1/4 * (data_reshape_1 + data_reshape_2 + data_reshape_3 + data_reshape_4)
I1 = 1/4 * 1j * (data_reshape_3 - data_reshape_1) + 1/4 * (data_reshape_4 - data_reshape_2)
I2 = 1/4 * (-data_reshape_1 + data_reshape_2 - data_reshape_3 + data_reshape_4)
I3 = 1/4 * 1j * (data_reshape_1 - data_reshape_3) + 1/4 * (data_reshape_4 - data_reshape_2)

# # Pour Mire_negative_position_80
for z in np.linspace(-0.010, -0.013, 10):

# # Pour Mire_negative_position_160
# for z in np.linspace(-0.045, -0.048, 10):

# # Pour Mire_negative_position_199
# for z in np.linspace(-0.047 -0.051, 10):
#     OutputField = Hologram.hologram1FFT(I3, nx, ny, 5.5e-6, 5.5e-6, 658e-9, z)
    OutputField = Hologram.hologram2FFT(I3, nx, ny, 5.5e-6, 5.5e-6, 658e-9, z)
    DisplayedImage = np.absolute(OutputField)
    plt.imshow(DisplayedImage)
    plt.title('reconstructed hologram')
    plt.pause(1)


# plt.imshow(np.log(np.abs(np.fft.fftshift(np.fft.fft2(img)))))
# plt.title('Fourier plane')
# plt.show()

