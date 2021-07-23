from matplotlib import pyplot as plt
import numpy as np
from io import StringIO
from PIL import Image
import Hologram
import holo
import struct
import math
import scipy
from scipy.fftpack import fft
from scipy.fft import fftshift


ImageArraySize = np.array([512, 1024])  # taille de l'image
nx, ny = ImageArraySize

data = holo.FileReader('210211_BAE0275_OD-2_64img.holo').get_all_frames()

J = np.ones((524288, 64))
Jk = np.ones((64, nx, ny))
H = np.zeros((ny, nx))
M = np.ones((ny, nx))
SHr = np.ones((64, ny, nx))
SH = SHr.astype("complex128")

n = np.maximum(np.size(Jk, 1), np.size(Jk, 2))
img_r = np.zeros((n, n))
img = img_r.astype("complex128")
Hkr = np.zeros((np.size(Jk, 0), n, n))
Hk = Hkr.astype("complex128")

for i in range(64):
    J[:, i] = data[:, i]
    Jk[i, :, :] = np.reshape(data[:, i], (nx, ny))  #.astype("complex128") # Stockage de la démodulation temporelle dans un tableau 3D avec coordonnée de profondeur le temps
# plt.imshow(np.rot90(np.flipud(Jk[0, :, :])), aspect='auto', interpolation='none', origin='lower')
# plt.show()

for i in range(64):
    img[0:np.size(Jk, 1), 0:np.size(Jk, 2)] = Jk[i, :, :]
    Hk[i, :, :] = Hologram.hologram1FFT(img, np.size(img, 0), np.size(img, 1), 12e-6, 12e-6, 852e-9, 0.38) #Propagation via la méthode FFT1 sur chaque image, donc chaque tranche du cube

SH = fft(Hk, axis=-3)  # Transformée de Fourier temporelle, la prise en compte du temps est faite par une fft 1D sur l'axe 0 (l'axe de la profondeur de la matrice 3D)


resultat = plt.imshow(np.rot90(np.flipud(fftshift(np.mean(np.absolute(SH[4:60, :, :]), 0))), 56), cmap='gray')
plt.show()



# for z in np.linspace(0.35, 0.45, 10): #Test pour plusieurs distances z
#     for i in range(63):
#         J[:, i] = data[:, i+1] - data[:, i]  #Démodulation temporelle en différenciant les images successives
#         Jk[i, :, :] = (np.reshape(J[:, i], (ny, nx), order='C')).astype("complex128") # Stockage de la démodulation temporelle dans un tableau 3D avec coordonnée de profondeur le temps
#         Hk[i, :, :] = Hologram.hologram1FFT(Jk[i,:,:], nx, ny, 12e-6, 12e-6, 852e-9, z) #Propagation via la méthode FFT1 sur chaque image, donc chaque tranche du cube
#
#     for i in range(64):
#         H = H + (np.absolute(Hk[i, :, :]))
#
#     plt.imshow(np.fft.ifftshift(H))
#     plt.show()
#     plt.title('reconstructed hologram %1.3f' % z)
#     plt.pause(1)
