#!/usr/bin/env python3

from PIL import Image
import os

DIR_NAME = "{}/images".format(os.getenv("HOME"))
DEST_PATH = "/opt/icons".format(os.getenv("HOME"))

images = os.listdir(DIR_NAME)

for image in images:
  im = Image.open("{}/{}".format(DIR_NAME, image)).convert("RGB")
  out = im.rotate(270)
  out = out.resize((128,128))
  img = out.save("{}/{}".format(DEST_PATH, image), "jpeg")