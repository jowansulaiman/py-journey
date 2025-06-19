# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 12:51:48 2025

@author: engin.bilir

1. In JSON-Datei schreiben (2 Punkte): Konvertieren Sie dieses Python-Dictionary
in einen JSON-String und speichern Sie es in einer Datei namens produkt.json. 
Die JSON-Datei sollte "pretty-printed" sein, also mit einer Einruckung von 4 
Leerzeichen formatiert werden.

2. Aus JSON-Datei lesen (2 Punkte): Lesen Sie die Daten aus der produkt.json
Datei zuruck in ein neues Python-Objekt. Greifen Sie auf den Wert des Schlüssels
"RAM" innerhalb von ßpezifikationen" zu und geben Sie ihn auf der Konsole aus.
"""

import json, os

filename = "produkt.json"
produkt_daten = {
    "id": 101,
    "name": "Laptop Pro X",
    "spezifikationen": {
        "CPU": "Intel i7",
        "RAM": 16,
        "Speicher": "512GB SSD"
    },
    "verfuegbar": True ,
    "anhaengsel": None
}

# JSON-Datei schreiben "produkt.json"
with open(filename, "w", encoding="utf-8") as fileJSON:
    json.dump(produkt_daten, fileJSON, indent=4)
    if os.path.exists(filename):
        print("Übung Nr 1:")
        print("Eine JSON-Datei wurde erstellt!")
    else:
        print("Die Datei wurde nicht erstellt!")

print("")

# JSON-Datei lesen
with open(filename, "r", encoding="utf-8") as readFileJSON:
    readIT = json.load(readFileJSON)
    print("Übung Nr 2:")
    print(f"RAM ist: {readIT['spezifikationen']['RAM']}")
    