import os


# 1. Notizen schreiben

with open("meine_notizen.txt","w",encoding="utf-8") as notice:
    print(f"Bitte gebe 3 Notizen ein.")
    for i in range(3):
        notice.write(input(f"Bitte gib die {i + 1}. Notiz ein: "))
    
    print("Danke für die 3 Notizen")

print("")
print("")
# 2. Notizen lesen und nummerieren

with open("meine_notizen.txt","r",encoding="utf-8") as notice:
    print("Ausgabe der Notizen: ")
    notizen = notice.readlines()
    cnt = 1
    for i in notizen:
        print(f"{cnt}. {i}")
        
    
    print("")
    print("Das waren die 3 Notizen.")
    print("")
    print("")

# 3. Datei sicher löschen

if os.path.exists("meine_notizen.txt"):
    os.remove("meine_notizen.txt")
    print("Die Notizen wurden gelöscht!")
else:
    print("FEHLER! - Notizen nicht gefunden!")