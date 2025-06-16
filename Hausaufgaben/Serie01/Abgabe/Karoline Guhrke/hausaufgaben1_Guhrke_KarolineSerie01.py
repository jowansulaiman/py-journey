#Schreibe ein Python-Skript, das als einfaches Notizbuch dient
# Das Programm soll den Benutzer fragen, ob er eine neue Notiz hinzufügen oder 
# alle Notizen anzeigen möchte.

import os
Wunsch=input("Möchtest du (a)eine neue Notiz hinzufuegen oder (b)alle Notizen anzeigen?")
if Wunsch== "a":
    file_object = open("Notizbuchnotiz.txt", "a")
    neunote=input("Gebe eine neue Notiz ein!:")
    file_object.writelines("\n"+ neunote)
    file_object.close()
elif Wunsch== "b":
    with open ("Notizbuchnotiz.txt", "r") as notizbuch:
        notizbucheintraege = notizbuch.readlines ()
        print(notizbucheintraege)
else: print("Antworte a oder b!")

# Notiz hinzufügen: Wenn der Benutzer eine Notiz hinzufügen möchte, 
# soll das Programm ihn nach der Notiz fragen (eine einzelne Zeile Text genügt). 
# Diese Notiz soll dann in einer Datei namens meine_notizen.txt gespeichert werden. 
# Jede neue Notiz soll in einer neuen Zeile angehängt werden.



#Aufgabe 1.2: Datei-Inspektor
#Schreibe ein Python-Skript, das den Benutzer nach einem Dateinamen fragt und dann versucht, 
# den Inhalt dieser Datei anzuzeigen.
#• Frage den Benutzer: "Welche Datei möchtest du anzeigen?"
#• Lies den Dateinamen ein.
#• Versuche, die Datei zu öffnen und ihren gesamten Inhalt auf der Konsole auszugeben.
#• Fehlerbehandlung: Wenn die Datei nicht gefunden wird, soll das Programm nicht abstürzen, 
# sondern eine freundliche Meldung ausgeben, z.B. "Datei ’[Dateiname]’ nicht gefunden."

gewDatei=input("Welche Datei möchtest du anzeigen?")
if os.path.exists(gewDatei):
    with open (gewDatei, "r") as gewuenschteDatei:
            gewdateieintraege = gewuenschteDatei.readlines ()
            print(gewdateieintraege)
else: print("Datei " +gewDatei+ " nicht gefunden")

#Aufgabe 1.2: mit try except
gewDatei2=input("Welche Datei möchtest du anzeigen?")
try:
    with open (gewDatei2, "r") as gewuenschteDatei2:
            gewdateieintraege2 = gewuenschteDatei2.readlines ()
            print(gewdateieintraege2)
except:
  print("Datei " +gewDatei2+ " nicht gefunden")



#Aufgabe 1.3: Ordner-Inhalt auflisten
#Schreibe ein Python-Skript, das alle Dateien und Ordner in einem vom Benutzer angegebenen 
# Verzeichnis auflistet.
#• Frage den Benutzer: "Welchen Ordner möchtest du auflisten?"
#• Lies den Pfad zum Ordner ein.
#• Verwende das os-Modul (insbesondere os.listdir()), um alle Einträge (Dateien und Unterordner) 
# in diesem Verzeichnis aufzulisten und ihre Namen auf der Konsole auszugeben.
#• Fehlerbehandlung: Gib eine Meldung aus, falls der angegebene Pfad kein gültiges Verzeichnis ist.

import os
dirname2=input("Welchen Ordner möchtest du auflisten?")
#dirname = '/Users/Karoline/Downloads/OneDrive_1_6.6.2025/'
# Aktuelles Arbeitsverzeichnis abrufen
aktuelles_verzeichnis = os.getcwd()
#kombi ist pfadangabe mit gewünschtem Ordnername hinten dran
kombi=aktuelles_verzeichnis+"/"+ dirname2
print(kombi)
print(f"Aktuelles Arbeitsverzeichnis: {aktuelles_verzeichnis}")
if os.path.exists(kombi):
    objects2 = os.listdir(kombi)
    objects2.sort()
    for objectname2 in objects2:    
        print(objectname2)
else: print("Das Verzeichnis existiert nicht")

