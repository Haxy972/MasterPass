import string
import random
import PasswordManager as passwordManager


def create_password():
    application = str(input("Vous voulez enregistrer un mot de passe pour quelle application: ")).lower()
    if not passwordManager.contain_app(application):
        password = passwordManager.get_random_password()
        passwordManager.register_password(application, password)
        print(application + ": " + password)
    else:
        print("Vous avez déjà enregistré un mot de passe pour cette application")


def see_all_applications():
    print("\nListe des mots de passe enregistrés")
    for application in passwordManager.get_all_applications():
        print("- " + application)
    print("\n")


print("\n[0] : Générer un nouveau mot de passe")
print("[1] : Voir tous les mots de passe")
print("[2] : Regarder un mot de passe")
print("[3] : Supprimer un mot de passe")
print("[4] : Quitter l'application\n")
password_file = passwordManager.get_password_file()
loop = True
while loop is True:
    choice = input("Sélection: ")
    if choice == "0":
        create_password()
    elif choice == "1":
        see_all_applications()
    elif choice == "2":
        print("\nBientôt")
    elif choice == "3":
        print("\nBientôt")
        # delete_password()
    elif choice == "4":
        print("Au revoir !")
        loop = False

    else:
        print("Vous n'avez pas choisis un bon chiffre veuillez réessayer !")
