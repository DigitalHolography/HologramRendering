from matplotlib import pyplot as plt
import numpy as np
from io import StringIO
from PIL import Image
import Hologram
import holo
import struct



# z = 0.06

ImageArraySize = np.array([1024, 1024])
nx, ny = ImageArraySize


# Lecture fichier .
# img_infile = open('GaborTarget_SingleImage_XY_D_2048_2048_8bit_e.raw', 'rb')
# img_array = np.fromfile(img_infile, dtype=np.uint8, count=nx*ny)
# img = Image.frombuffer("I", [nx, ny],
#                             img_array.astype('I'),
#                             'raw','I', 0, 1)

#img = holo.FileReader('Mire_negative_position_73.holo').get_all_frames()

data = holo.FileReader('Mire_negative_position_160.holo').get_all_frames() #ici tu mets le nom du fichier que tu veux ouvrir
data_reshape = np.reshape(data[:,0], (1024, 1024), order = 'C') #dans data[:, 0] ça veut dire que tu prends la première image du film (correspond à l'indice 0)
                                                              #(1024, 1024) c'est les dimensions des images, attention il faut les choisir intelligement les dimensions sont écrits dans le header normalement
# plt.imshow(np.rot90(np.flipud(data_reshape), 4), aspect='auto', interpolation='none', origin='lower') #ça c'est juste pour afficher
# plt.show()


# plt.imshow(data_reshape)
# plt.title('interferogram')
# plt.show()


for z in np.linspace(0.01, 0.3, 10):
    OutputField = Hologram.hologram1FFT(data_reshape, nx, ny, 5.5e-6, 5e-6, 658e-9, -z)
    # OutputField = Hologram.hologram1FFT(img, nx, ny, 5.5e-6, 5.5e-6, 658e-9, -z)
    DisplayedImage = np.absolute(OutputField)
    plt.imshow(DisplayedImage)
    plt.title('reconstructed hologram')
    plt.pause(0.01)


#
# plt.imshow(np.log(np.abs(np.fft.fftshift(np.fft.fft2(img)))))
# plt.title('Fourier plane')
# plt.show()

