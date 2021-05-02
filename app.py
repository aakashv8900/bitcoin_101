#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri April 09 08:02:27 2021

@author: Aakash
"""

import urllib.request as request
import json
import requests

while(True):
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/INR.json")
    data = response.json()

    def write_json(data, filename="data.json"):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    write_json(data)
