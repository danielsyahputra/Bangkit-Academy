#!/usr/bin/env python3

import os
import requests

files = os.listdir("/data/feedback")
for file in files:
  with open(os.path.join("/data/feedback", file), "r") as f:
    lines = [line.replace('\n',"") for line in f]
    data = {"title":lines[0], "name":lines[1], "date":lines[2], "feedback":lines[3]}
    response = requests.post("http://35.222.187.239/feedback/", data=data)
    print(response.status_code)
    #print(data)