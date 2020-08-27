#!/usr/bin/env python3

import requests
import os

url = "http://34.68.149.2/fruits/" # URL was provided in the project material.

home_directory = os.getcwd()
image_path = os.path.join(home_directory, 'supplier-data', 'images') #In Linux: ~/supplier-data/images
description_path = os.path.join(home_directory, 'supplier-data', 'descriptions') #In Linux: ~/supplier-data/descriptions

dict_fruit = {'name': '', 'weight': '', 'description': '', 'image_name': ''} 

for file in os.listdir(description_path):
  with open(os.path.join(description_path, file)) as txt_file:
    k = txt_file.readlines()
    dict_fruit['name'] = k[0].strip()
    # Weight value of '500 lbs' is split into two separate strings '500' and 'lbs'  
    weight = k[1].strip().split()
    # The string is converted to an integer value
    number = int(weight[0])
    dict_fruit['weight'] = number
    dict_fruit['description'] = k[2].strip()
  file_split = file.split('.')
  file_number = file_split[0]
  image_file = file_number + '.jpeg'
  dict_fruit['image_name'] = image_file
  response = requests.post(url, json=dict_fruit) # Post description as JSON format to the web server
  
print(response.status_code) # Status code of 201 would mean that the descriptions were uploaded sucessfully.
