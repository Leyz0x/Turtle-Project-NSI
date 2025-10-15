print("""

 ▄████▄   ▄▄▄       ██▓     ▄████▄   █    ██  ██▓    ▄▄▄     ▄▄▄█████▓ ██▀███   ██▓ ▄████▄  ▓█████ 
▒██▀ ▀█  ▒████▄    ▓██▒    ▒██▀ ▀█   ██  ▓██▒▓██▒   ▒████▄   ▓  ██▒ ▓▒▓██ ▒ ██▒▓██▒▒██▀ ▀█  ▓█   ▀ 
▒▓█    ▄ ▒██  ▀█▄  ▒██░    ▒▓█    ▄ ▓██  ▒██░▒██░   ▒██  ▀█▄ ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██▒▒▓█    ▄ ▒███   
▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░    ▒▓▓▄ ▄██▒▓▓█  ░██░▒██░   ░██▄▄▄▄██░ ▓██▓ ░ ▒██▀▀█▄  ░██░▒▓▓▄ ▄██▒▒▓█  ▄ 
▒ ▓███▀ ░ ▓█   ▓██▒░██████▒▒ ▓███▀ ░▒▒█████▓ ░██████▒▓█   ▓██▒ ▒██▒ ░ ░██▓ ▒██▒░██░▒ ▓███▀ ░░▒████▒
░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒▒   ▓▒█░ ▒ ░░   ░ ▒▓ ░▒▓░░▓  ░ ░▒ ▒  ░░░ ▒░ ░
  ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░  ░  ▒   ░░▒░ ░ ░ ░ ░ ▒  ░ ▒   ▒▒ ░   ░      ░▒ ░ ▒░ ▒ ░  ░  ▒    ░ ░  ░
░          ░   ▒     ░ ░   ░         ░░░ ░ ░   ░ ░    ░   ▒    ░        ░░   ░  ▒ ░░           ░   
░ ░            ░  ░    ░  ░░ ░         ░         ░  ░     ░  ░           ░      ░  ░ ░         ░  ░
░                          ░                                                       ░               
      """)

user = int(input("Bonjour cliquez sur :\n\n1 : Pour multiplier\n2 : Pour Diviser\n3 : Pour Additionner\n4 : Pour Soustraire\n"))

if user == 1:
    nb1 = int(input("\nDonne ton 1er nombre :"))
    nb2 = int(input("Donne ton 2eme nombre :"))
    calcul1 = nb1 * nb2 
    print("\nResultat =", calcul1)

elif user == 2:
    nb1 = int(input("\nDonne ton 1er nombre :"))
    nb2 = int(input("Donne ton 2eme nombre :"))
    calcul2 = nb1 / nb2 
    print("\nResultat =", calcul2)

elif user == 3:
    nb1 = int(input("\nDonne ton 1er nombre :"))
    nb2 = int(input("Donne ton 2eme nombre :"))
    calcul3 = nb1 + nb2 
    print("\nResultat =", calcul3)

elif user == 4:
    nb1 = int(input("\nDonne ton 1er nombre :"))
    nb2 = int(input("Donne ton 2eme nombre :"))
    calcul4 = nb1 - nb2 
    print("\nResultat =", calcul4)

else:
    print("Erreur de syntaxe!")


