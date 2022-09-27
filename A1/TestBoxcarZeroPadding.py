import cv2
import matplotlib.pyplot as plt
import numpy as np


def BoxcarZeroPadding(image, k):
    imgs = cv2.blur(image, (k, k), borderType=cv2.BORDER_CONSTANT)
    return imgs


def BoxcarZeroPadding_(img, k):
    h, w, c = img.shape
    pad = k // 2
    images = np.zeros((h + 2 * pad, w + 2 * pad, c))
    images[pad:pad + h, pad:pad + w] = img.copy().astype(float)

    old = images.copy()
    for y in range(h):
        for x in range(w):
            for ci in range(c):
                images[pad + y, pad + x, ci] = np.mean(old[y:y + k, x:x + k, ci])

    images = images[pad:pad + h, pad:pad + w].astype(np.uint8)
    return images


if __name__ == '__main__':
    image = cv2.imread('characterTestPattern688.tif')
    out = BoxcarZeroPadding(image, 35)
    out2 = BoxcarZeroPadding_(image, 35)
    f, axes = plt.subplots(1, 3)
    ax = axes.ravel()
    ax[0].imshow(image)
    ax[0].set_title('Original')
    ax[0].axis('off')

    ax[1].imshow(out)
    ax[1].set_title('k=35')
    ax[1].axis('off')

    ax[2].imshow(out)
    ax[2].set_title('k=35(All self-impl)')
    ax[2].axis('off')

    plt.tight_layout()
    plt.show()


