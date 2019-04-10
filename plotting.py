import matplotlib
from matplotlib import pyplot as plt
import numpy as np


def is_interactive():
    try:
        __IPYTHON__
    except NameError:
        return False
    else:
        return True


def plot_images(images, labels=None, figsize=(8, 8), fname=None):
    """ Plot some images """
    n_examples = len(images)
    dim = np.ceil(np.sqrt(n_examples))
    plt.figure(figsize=figsize)
    class_names = ['airplane','automobile','bird','cat','deer', 'dog','frog','horse','ship','truck']
    for i, img in enumerate(images):
        plt.subplot(dim, dim, i + 1)
        if img.shape[-1] == 3:
            img = img.astype(np.uint8)
            plt.imshow(img)
            if labels is not None:
                plt.suptitle(class_names[i])
        else:
            img = np.squeeze(img)
            plt.imshow(img, cmap=plt.cm.Greys)
        plt.axis('off')
    plt.tight_layout()
    plt.show()

