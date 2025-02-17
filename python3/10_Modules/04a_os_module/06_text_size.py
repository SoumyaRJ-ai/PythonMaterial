#!/usr/bin/python
"""
Purpose: Display all text files with size
greater than 1kb i,e., 1024 bytes
"""
import os
import sys
from os.path import join

path = sys.exec_prefix

for dirname, dirs, files in os.walk(path):
    for filename in files:
        if filename.endswith(".txt"):
            _file = os.path.join(dirname, filename)
            if os.path.getsize(_file) > 1024:
                print(os.path.getsize(_file), _file)
