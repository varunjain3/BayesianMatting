import os
from PIL import Image, ImageOps
import cv2
import numpy as np
import matplotlib.pyplot as plt

maskfolder = os.path.join("results")
imagefolder = os.path.join("data", "input_training_lowres")


for i in range(1, 28):
    name = "GT{}".format(str(i).zfill(2))
    img = np.array(Image.open(os.path.join(imagefolder, name + ".png")))
    mask = np.array(ImageOps.grayscale(Image.open(
        os.path.join(maskfolder, name + "_alpha.png"))))

    msk = np.zeros(mask.shape, dtype="uint8")
    msk[mask > 255/2] = 1

    img *= msk[:, :, np.newaxis]
    plt.imsave(os.path.join("results", name + ".png"), img)
    # plt.show()
