#!/usr/bin/env python3

import requests
import os

home_directory = os.getcwd()
path = os.path.join(home_directory, 'supplier-data', 'images') #In Linux: ~/supplier-data/images

url = "http://34.68.149.2/upload/" # This URL was provided in the project material.

for file in os.listdir(path):
  if (file.find('.jpeg') != -1): # Making sure that only files with '.jpeg' extention's are opened 
        with open(os.path.join(path,file),'rb') as opened:
            response = requests.post(url, files={'file': opened}) # uploading files with '.jpeg' extention.
