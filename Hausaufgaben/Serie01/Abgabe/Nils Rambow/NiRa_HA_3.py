# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 12:45:38 2025

@author: nils.rambow
"""
#3.1)
import json

produkt_daten = {
    "id": 101 ,
    " name ": " Laptop Pro X",
    "spezifikationen": {
            "CPU": " Intel i7",
            "RAM": 16 ,
            "Speicher ": "512 GB SSD"
} ,
    "verfuegbar ": True ,
    "anhaengsel ": None
}

with open("produkt_daten.json", "w") as f:
    json.dump(produkt_daten, f, indent = 4)
    print(produkt_daten)
    
#3.2)

with open("produkt_daten.json", "r") as f:
    py_text = json.load(f)
    print(py_text["spezifikationen"]["RAM"])