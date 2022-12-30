
import string
import random

password_file = open("cache/password.yml")


def get_random_password(length : int = 16):
    result = ""
    main_list = string.ascii_letters + string.punctuation + string.digits
    for _ in range(length):
        index = random.randint(0,len(main_list) - 1)
        result += main_list[index]
    
    return result
    
def register_password(application_name : str,password : str):
    global password_file
    text = application_name +": \"" + password + "\""
    password_file.write(text)
    
    
application = str(input("Vous voulez enregistrer un mot de passe pour quelle application: "))
password =  get_random_password()
register_password(application, password)
print(application +": "+ password)