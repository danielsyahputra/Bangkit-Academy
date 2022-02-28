#!/usr/bin/env python3
from multiprocessing import Pool
import subprocess
import os

src = "{}/data/prod/".format(os.getenv("HOME"))

def run(folders):
    dest = "{}/data/prod_backup/".format(os.getenv("HOME"))
    subprocess.call(["rsync", "-arq", folders, dest])

if __name__ == "__main__":
    folders = []
    for dir in os.listdir(src):
        dir_path = os.path.join(src, dir)
        folders.append(dir_path)

    pool = Pool(len(folders))
    pool.map(run, folders)