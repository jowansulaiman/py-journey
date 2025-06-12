
q = False
while q == False:
    print("Dies ist dein Notizblock!")
    print("Möchtest du:")
    print("[a] - Den Notizblock anzeigen")
    print("[h] - Etwas hinzufügen")
    print("[q] - Das Programm beenden")
    x = input(">>>")
    if x == "a":
        with open ("meine_notizen.txt", "r") as f:
            content= f.read()
            print(content)
    elif x == "h":
        print("Gib ein, was du hinzufügen möchtest:")
        with open ("meine_notizen.txt", "a") as f:
            y = input(">>>")
            f.writelines(y)
            f.write("\n")
    elif x == "q":
        q = True
    else:
        print("ungültige eingabe, try again!")