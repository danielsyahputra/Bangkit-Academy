#!/usr/bin/env python3

import requests
import os

URL = "http://34.69.225.66/upload/"
DIR = "{}/supplier-data/images".format(os.getenv('HOME'))

images = os.listdir(DIR)
images = [image for image in images if image.endswith(".jpeg")]

for image in images:
    with open(os.path.join(DIR, image), 'rb') as opened:
        r = requests.post(URL, files={'file': opened})
        print(r.status_code)