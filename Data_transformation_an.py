# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:14:04 2022

@author: Anjaly
"""

import pymongo
import pandas as pd
import json
import numpy as np
import xml.etree.ElementTree as ETree

client = pymongo.MongoClient("mongodb://localhost:27017")
df22 = pd.read_csv("D:\\NCI Modules\\Sem 1\\DAP\\Project\\Dataset\\raw_data\\P10_EMPLOYEES.csv")


data22 = df22.to_dict(orient="records")

db = client["AirlineData"]

db.P10_EMPLOYEES.insert_many(data22)
