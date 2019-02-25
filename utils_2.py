import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from os import listdir


class ImageData:
    def __init__(self, direc, total_size, batch_size=64, resize=(224, 224)):
        self.dir = direc
        self.total_size = total_size
        self.total_batches = int(np.ceil(total_size/batch_size))
        self.bs = batch_size
        self.resize = resize
        self.current_pos = 1

    def get_sample_img(self, normalize_func=None):
        choice = np.random.randint(0, self.total_size)
        path = self.dir+"/img ({})".format(choice)+".jpg"
        sample = Image.open(path)
        sample = sample.resize(self.resize, Image.ANTIALIAS)
        sample = np.asarray(sample)
        if normalize_func:
            sample = normalize_func(sample)
        return sample

    def get_image(self, normalize_func=None):
        imgs = []
        lower = self.current_pos
        higher = lower+self.bs
        self.current_pos = higher
        if higher > self.total_size:
            higher = self.total_size
            self.current_pos = 1
        for i in range(lower, higher):
            path = self.dir+"/img ({})".format(str(i))+".jpg"
            sample = Image.open(path)
            sample = sample.resize(self.resize, Image.ANTIALIAS)
            sample = np.asarray(sample)
            if normalize_func:
                sample = normalize_func(sample)
            imgs.append(sample)
        imgs = np.asarray(imgs)
        return imgs


def save_image(direct, name, img, resize_size=(256, 256), de_normalize_func=None):
    if de_normalize_func:
        img = de_normalize_func(img)
    img = Image.fromarray(np.uint8(img))
    img = img.resize(resize_size, Image.ANTIALIAS)
    img.save(direct+"{}.png".format(name))


def save_image_multiple(direct, name, imgs, show=False, de_normalize_func=None, num_imgs_dim=6, figsize=[12, 12]):
    fig, axes = plt.subplots(num_imgs_dim, num_imgs_dim, figsize=figsize)
    axes = axes.reshape([-1])
    for i, ax in zip(imgs, axes):
        if de_normalize_func:
            i = de_normalize_func(i)
        ax.imshow(i)
        ax.axis('off')
    if show == False:
        fig.savefig(direct+"{}.png".format(name))
        plt.close(fig)
        plt.clf()
    return
