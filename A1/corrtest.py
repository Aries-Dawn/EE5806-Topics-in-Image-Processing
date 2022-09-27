from scipy import ndimage
from scipy.ndimage import correlate
import numpy as np
from skimage.filters import rank
import cv2


def test_correlate():
    matrix = np.array([[1, 5, 9, 13],
                       [2, 6, 10, 14],
                       [3, 7, 11, 15],
                       [4, 8, 12, 16]])
    molecule = np.array([[1, 2, 1],
                         [2, 4, 2],
                         [1, 2, 1]])
    output = ndimage.correlate(matrix, molecule)
    return output


if __name__ == '__main__':
    print(test_correlate())
