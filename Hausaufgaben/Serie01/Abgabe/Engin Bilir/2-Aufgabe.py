# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 12:51:48 2025

@author: engin.bilir

1. Notizen schreiben (3 Punkte): Das Skript soll den Benutzer auffordern, drei Zeilen
Text als Notizen einzugeben. Jede eingegebene Notiz soll in eine neue Zeile in der Datei
"meine_notizen.txt" geschrieben werden. Wenn die Datei bereits existiert, soll ihr Inhalt
uberschrieben werden. ¨

2. Notizen lesen und nummerieren (2 Punkte): Lesen Sie anschließend den Inhalt
der gerade erstellten Datei meine notizen.txt zeilenweise aus. Geben Sie jede Zeile mit
einer vorangestellten Zeilennummer auf der Konsole aus (z.B. "1: Erste Notiz").

3. Datei sicher l¨oschen (2 Punkte): Zum Schluss soll das Skript prufen, ob die Datei ¨
meine notizen.txt existiert, und sie nur dann l¨oschen. Geben Sie eine Best¨atigungsmeldung
aus, nachdem die Datei gel¨oscht wurde, oder eine Meldung, falls sie nicht gefunden wurde.
"""

import os

filename = "meine_notizen.txt"

# 1. Notizen schreiben
with open(filename, "w", encoding="utf-8") as datei:
    for i in range(1, 4):
        zeile = input(f"Gib deine {i}. Notiz ein: ")
        datei.write(zeile + "\n")

# 2. Notizen lesen und nummerieren
with open(filename, "r", encoding="UTF-8") as datei:
    print("")
    print("Notizen Ausgabe:")
    for i in range (1, 4):
        auslese_zeile = datei.readline()
        print(f"{i}. " + auslese_zeile)

# 3. Datei sicher löschen
print("")
if os.path.exists(filename):
    os.remove(filename)
    print("Die Datei wurde gelöscht!")
else:
    print("Fehler! Die Datei wurde nicht gefunden!")