#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 21:59:05 2021

@author: hamimehrabi
"""


import json 
      
# Data to be written 
dictionary ={ 
  "Name": "hami", 
  "id": "96109996"
} 
      
# Serializing json  
json_object = json.dumps(dictionary, indent = 4) 


#Load Data

Ldictionary = json.loads(json_object)


import requests

r = requests.post(url = "https://www.toptal.com/developers/postbin/1643450056519-8855423310305", data = json_object)

print(r.status_code)



rGet = requests.get(url = "https://www.toptal.com/developers/postbin/1643450056519-8855423310305")

print(rGet.status_code)
print(rGet.content)