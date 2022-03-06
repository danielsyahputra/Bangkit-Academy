#!/usr/bin/env python3

import psutil
import shutil
import email.message
import os.path

def checkCPU():
    return psutil.cpu_percent()