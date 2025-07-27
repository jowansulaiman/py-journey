# Aufgabe 2: Praktische Dateiverwaltung 
# Erstellen Sie ein Python-Skript, das die folgenden Schritte ausführt:

# 1. Notizen schreiben (3 Punkte): 
# Das Skript soll den Benutzer auffordern, drei Zeilen Text als Notizen einzugeben. 
# Jede eingegebene Notiz soll in eine neue Zeile in der Datei meine notizen.txt geschrieben werden. 
# Wenn die Datei bereits existiert, soll ihr Inhalt überschrieben werden.


#Variante 1: In jeder Zeile steht angepasste Aufforderung : 
import os
with open("meine notizen.txt", "w") as no: 
    z=0
    while z<3:
        zstring=str(3-z)
        Notiz=input("Gebe "+ zstring + " Zeilen Text als Notizen ein!:")
        no.write(Notiz+"\n") 
        z=z+1

#Variante 2: Nur in der 1.Zeile steht die Aufforderung : 
import os  
with open("meine notizen2.txt", "w") as no2: 
    print("Gebe 3 Zeilen Text als Notizen ein!:")
    a=0
    while a<3:
        Zeile = input()
        no2.write(Zeile+"\n") 
        a=a+1


# 2. Notizen lesen und nummerieren (2 Punkte): 
# Lesen Sie anschließend den Inhalt der gerade erstellten Datei meine notizen.txt zeilenweise aus. 
# Geben Sie jede Zeile mit einer vorangestellten Zeilennummer auf der Konsole aus (z.B. "1: Erste Notiz").
import os  
with open("meine notizen.txt", "r") as Notizlesen: 
    i=1
    for zeilei in Notizlesen: # Jede Zeile wird einzeln geladen
        print(str(i) + ": " +zeilei)
        i += 1    
    
# 3. Datei sicher löschen (2 Punkte): 
# Zum Schluss soll das Skript prüfen, ob die Datei meine notizen.txt existiert, und sie nur dann löschen. 
# Geben Sie eine Besta ̈tigungsmeldung aus, nachdem die Datei geloöscht wurde, oder eine Meldung, falls sie nicht gefunden wurde.

import os
filename123="meine notizen.txt"
if os.path.exists(filename123):
    os.remove(filename123)
    print("Die Datei "+ filename123+" wurde geloescht.")
else:
    print("Datei "+ filename123+" nicht gefunden")


# Aufgabe 3: Arbeiten mit JSON

produkt_daten = { "id": 101,
"name": "Laptop Pro X", "spezifikationen": {
"CPU": "Intel i7", "RAM": 16,
"Speicher": "512GB SSD"
},
"verfuegbar": True, "anhaengsel": None
}

# 1. In JSON-Datei schreiben (2 Punkte): 
# Konvertieren Sie dieses Python-Dictionary in einen JSON-String und speichern Sie es in einer Datei 
# namens produkt.json. Die JSON-Datei sollte "pretty-printed" sein, also mit einer Einrückung von 4 Leerzeichen formatiert werden.

import json
with open("produkt.json", "w") as f: json.dump(produkt_daten, f, indent=4)

# 2. Aus JSON-Datei lesen (2 Punkte): Lesen Sie die Daten aus der produkt.json- Datei zurück in ein neues Python-Objekt. 
# Greifen Sie auf den Wert des Schlüssels "RAM" innerhalb von "Spezifikationen" zu und geben Sie ihn auf der Konsole aus.

import json
with open("produkt.json", "r") as g:
    loaded_config = json.load(g) 
    print(loaded_config["spezifikationen"]["RAM"]) 
   


# Aufgabe 4: Reguläre Ausdrücke (4 Punkte)
# Gegeben sei der folgende Text-String in Python:
#text = "Kontakt: info@example.com, Support: support@test.org, Admin:
#admin@domain.net"

#1. E-Mail-Adressen extrahieren (4 Punkte): Schreiben Sie ein Python-Skript, das 
# die Funktion re.findall() verwendet, um alle E-Mail-Adressen aus dem gegebenen 
# text- String zu extrahieren. Geben Sie die gefundene Liste von E-Mail-Adressen auf der Konsole aus.

import re
text = "Kontakt: info@example.com, Support: support@test.org, Admin: admin@domain.net"
emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text)
print(emails) 


    