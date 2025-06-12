#Clemens Geick

import json

# Vorgegebenes Dictionary:
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


# 1. In JSON-Datei schreiben

with open("produkt.json","w") as file:
    json.dump(produkt_daten,file,indent=4)
    print("Json-Datei erschaffen und gefüllt!")

print("")

# 2. Aus JSON-Datei lesen

with open("produkt.json","r") as file:
    json_daten = json.load(file)
    print(f"RAM: {json_daten["spezifikationen"]["RAM"]}")
