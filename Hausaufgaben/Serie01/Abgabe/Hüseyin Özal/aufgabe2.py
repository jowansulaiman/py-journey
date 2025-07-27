import os

## 1.
## Datei schreiben mit User Input
with open ("meine_notizen.txt","w",encoding="utf-8") as f:
    for i in range(3):
        text = input (f"Gebe die {i+1}. Zeile ein: ")
        f.write(text + "\n")


## 2.
# Datei zeilenweise lesen
with open ("meine_notizen.txt","r",encoding="utf-8") as f:
    zeilennummer = 1
    for zeile in f:
        print(f"{zeilennummer}: {zeile.strip()}")
        zeilennummer+=1

## 3.
# Wenn datei existiert löschen
if os.path.isfile("meine_notizen.txt"):
    os.remove("meine_notizen.txt")
    print("Datei erfolgreich gelöscht")
else:
    print("Datei existiert nicht")
