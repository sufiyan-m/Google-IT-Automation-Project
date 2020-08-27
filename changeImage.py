#!/usr/bin/env python3

import os.path
from PIL import Image

home_directory = os.getcwd()
path = os.path.join(home_directory, 'supplier-data', 'images') #In Linux: ~/supplier-data/images

for file in os.listdir(path):
  im = Image.open(os.path.join(path, file))
  name = file.split('.')
  new_name = name[0] + '.jpeg' # Image format changed from .TIFF to .JPEG
  im.resize((600,400)).convert('RGB').save(os.path.join(path, new_name)) # Image resolution changed from 3000x2000 to 600x400 pixel
