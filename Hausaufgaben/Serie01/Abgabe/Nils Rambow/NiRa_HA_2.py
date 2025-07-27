import os
i = 0
n = 1
q = False
            

while q == False:
    print("\nDies ist dein Notizblock!")
    print("Möchtest du: \n")
    print("[a] - Den Notizblock anzeigen")
    print("[h] - Etwas hinzufügen")
    print("[d] - Alles löschen")
    print("[q] - Das Programm beenden\n")
    x = input(">>>")
    if x == "a":
        if os.path.exists("meine_notizen.txt"):
            with open ("meine_notizen.txt", "r") as f:
                content= f.read()
                print(content if content else "\nKeine Notizen vorhanden.")
        else:
            print("\nKeine Notizen vorhanden.")
    elif x == "h":
        print("Gib ein, was du hinzufügen möchtest:")
        try:
            with open ("meine_notizen.txt", "r") as f:
                existing_notes = f.readlines()
                note_num = len(existing_notes) +1
        except FileNotFoundError:
            note_num = 1
        for i in range(3):
            y = input(f"\nNotiz {note_num}: ")
            with open("meine_notizen.txt", "a") as f:
                f.write(f"{note_num}. {y}\n")
            note_num +=1    
    elif x == "d":
        print("Sicher, dass Sie ALLES löschen wollen? (j/n)")
        del_confirm = input("\n>>> ")
        if del_confirm.lower() == "j":
            if os.path.exists("meine_notizen.txt"):
                os.remove("meine_notizen.txt")
                print("Alle Notizen wurden gelöscht!")
            else:
                print("Keine Notizen zum Löschen vorhanden.")      
        
    elif x == "q":
        q = True
        print("\nProgramm beendet. Bis bald!")
    else:
        print("\n ungültige eingabe, try again! \n")