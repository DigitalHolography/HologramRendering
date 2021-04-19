from matplotlib import pyplot as plt
import numpy as np


def hologram1FFT(E : np.ndarray, nx : float, ny: float, pasx: float, pasy: float, lambd: float, z: float):
    x = np.zeros(nx)
    y = np.zeros(ny)

    x = (np.arange(nx) - round(nx / 2)) * pasx
    y = (np.arange(ny) - round(ny / 2)) * pasy

    X, Y = np.meshgrid(x, y)

    phaseQ = np.exp(1j * np.pi / (lambd * z) * (X**2 + Y**2))
    C = E * phaseQ
    D = np.fft.fft2(np.fft.ifftshift(np.transpose(C)))
    OutputField = D * np.exp((-2 * 1j * np.pi * z / lambd) / (1j * lambd * z))

    return OutputField



def hologram2FFT(E : np.ndarray, nx : float, ny: float, pasx: float, pasy: float, lambd: float, z: float):

    pasu = 1/(nx*pasx)
    pasv = 1/(ny*pasy)

    u = (np.arange(nx) - round(nx / 2)) * pasu
    v = (np.arange(ny) - round(ny / 2)) * pasv

    U, V = np.meshgrid(np.fft.ifftshift(u), np.fft.ifftshift(v))
    H = np.exp(2 * 1j * np.pi * z / lambd * np.sqrt(1 - (lambd**2) * (U**2)-(lambd**2) * (V**2)) / (1j * lambd * z))

    # plt.imshow(np.fft.ifftshift(np.real(H)))
    C11 = np.fft.fft2(E) * H

    OutputField = np.fft.ifft2(C11)

    return OutputField









