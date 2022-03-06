#!/usr/bin/env python3

from PIL import Image
import os

DIR = "{}/supplier-data/images".format(os.getenv('HOME'))


images = os.listdir(DIR)
images = [image for image in images if image.endswith(".tiff")]

for image in images:
    im = Image.open("{}/{}".format(DIR, image)).convert("RGB")
    out = im.resize((600, 400))
    image, ext = os.path.splitext(image)
    image += ".jpeg"
    img = out.save("{}/{}".format(DIR, image), "jpeg")