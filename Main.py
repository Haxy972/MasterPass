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
    print("\nListe des mots de passe enregistrés\n")
    if len(passwordManager.get_all_applications()) != 0:
        for application in passwordManager.get_all_applications():
            print("- " + application)
    else:
        print("- Aucun mot de passe enregistré")
    print("\n")


def delete_application():
    application = str(input("Vous souhaitez supprimer quel application: ")).lower()
    if passwordManager.contain_app(application):
        if passwordManager.get_password(application) is not None:
            passwordManager.remove_application(application)
    else:
        print("Cette application n'existe pas")


def see_password():
    application = str(input("Vous souhaitez voir le mot de passe de quelle application: ")).lower()
    if passwordManager.contain_app(application):
        if passwordManager.get_password(application) is not None:
            print(application + ": " + passwordManager.get_password(application))
        else:
            print("Une erreur est survenue")
    else:
        print("Cette application n'existe pas")


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
        see_password()
    elif choice == "3":
        delete_application()
    elif choice == "4":
        print("Au revoir !")
        loop = False

    else:
        print("Vous n'avez pas choisis un bon chiffre veuillez réessayer !")
