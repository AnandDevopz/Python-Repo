#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 21:08:37 2023

@author: saumyabm
"""

import requests




def check_connectivity():
    request = requests.get("http://www.google.com")
    response = request
    return response.status_code == 200


result=check_connectivity()

print(result)