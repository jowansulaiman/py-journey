import json


produkt_daten = {

    "id": 101,
    "name": "Laptop Pro X",
    "spezifikationen": {
        "CPU": "Intel i7",
        "RAM": 16,
        "Speicher": "512 GB SSD"
    },
    "verfuegbar": True,
    "anhaengsel": None
}


## 1.

## Die Daten als Json String machen und dann printen
jsonstring = json.dumps(produkt_daten, indent=4)
print(jsonstring)

# Die Daten in einer Json Datei speichern
with open ("produkt.json","w") as f:
    json.dump(produkt_daten,f,indent=4)

## 2.
## Datei zurück in Python Datei
with open ("produkt.json","r") as f:
    py_text = json.load(f)
    print(py_text["spezifikationen"]["RAM"])