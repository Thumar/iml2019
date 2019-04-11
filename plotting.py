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


def rectangular_array(n=15):
    """ Return x,y coordinates for rectangular array with n^2 stations. """
    n0 = (n - 1) / 2
    return (np.mgrid[0:n, 0:n].astype(float) - n0)


def plot_footprint(footprint, axis, label=None):
    """Plot a map *footprint* for an detector array specified by *v_stations*. """
    xd, yd = rectangular_array(n=9)
    filter = footprint != 0
    # filter[5, 5] = True
    axis.scatter(xd[~filter], yd[~filter], c='grey', s=150, alpha=0.1, label="silent")
    circles = axis.scatter(xd[filter], yd[filter], c=footprint[filter], s=150, alpha=1, label="loud")
    cbar = plt.colorbar(circles, ax=axis)
    cbar.set_label('signal [a.u.]')
    axis.grid(True)
    if label != None:
        axis.text(0.95, 0.1, "Energy: %.1f EeV" % label, verticalalignment='top', horizontalalignment='right', transform=axis.transAxes, backgroundcolor='w')
    axis.set_aspect('equal')
    axis.set_xlim(-5, 5)
    axis.set_ylim(-5, 5)
    axis.set_xlabel('x [km]')
    axis.set_ylabel('y [km]')


def plot_multiple_footprints(footprint, fname=None, log_dir='.', title='', epoch='', nrows=2, ncols=2, labels=None):
    """ Plots the time and signal footprint in one figure """
    fig, sub = plt.subplots(nrows=nrows, ncols=ncols, figsize=(9, 7))
    for i in range(ncols):
        for j in range(nrows):
            idx = np.random.choice(np.arange(footprint.shape[0]))
            plot_footprint(np.squeeze(footprint[idx]), axis=sub[i, j], label=labels[idx] if labels is not None else None)
    plt.tight_layout()
    fig.subplots_adjust(left=0.02, top=0.95)
    plt.suptitle(title + ' ' + str(epoch), fontsize=12)
    plt.show()
