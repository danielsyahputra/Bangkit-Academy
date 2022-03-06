#! /usr/bin/env python3

import os
import requests

URL = "http://34.69.225.66/fruits/"
DIR = "{}/supplier-data/descriptions".format(os.getenv('HOME'))

files = os.listdir(DIR)

for file in files:
    with open(os.path.join(DIR, file), "r") as f:
        lines = [line.replace('\n',"") for line in f]
        name = lines[0]
        weight = int(lines[1].split()[0])
        description = lines[2]
        filename, ext = os.path.splitext(file)
        image_name = filename + ".jpeg"
        data = {"name": name, "weight": weight, "description": description, "image_name": image_name}
        response = requests.post(URL, data=data)
        print(response.status_code)