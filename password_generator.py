import tkinter.messagebox
from random import randint, choice
from tkinter import *
import string
def generate_password():
    password_min = 12
    password_max = 16
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = ""
    for x in range(randint(password_min, password_max)):
        password +=choice(all_chars)
    passwordEntry.delete(0, END)
    passwordEntry.insert(0, password)
    tkinter.messagebox.showinfo(title="Générateur de mot de passe", message="Votre mot de passe a été généré")



window = Tk()
window.title("MasterPass - Password Generator")
window.geometry("720x480")
window.iconbitmap("ressources/logo.ico")
window.config(background="#cc2146")

frame = Frame(window, bg= '#cc2146')


width = 300
height = 300
image = PhotoImage(file="ressources/R.png").zoom(10).subsample(32)
canvas = Canvas(frame, width=width,height=height, bg= '#cc2146', highlightthickness=0, bd=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row = 0, column=0, sticky=W)

right_frame = Frame(frame, bg='#cc2146')

labeltitle = Label(right_frame, text="Mot de Passe", font=("Helvetica", 20), bg='#cc2146', fg='white')
labeltitle.pack()

passwordEntry = Entry(right_frame, font=("Helvetica", 20), bg='white', fg='black', bd=5)
passwordEntry.pack(pady=20)

generate_password_button = Button(right_frame,font=("Arial",20), text="Générer un mot de passe", bg='white', fg='#cc2146', command=generate_password)
generate_password_button.pack(pady=20)


right_frame.grid(row = 0, column=1, sticky=E)

frame.pack(expand=YES)
menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label= "Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu = file_menu)
window.config(menu=menu_bar)

window.mainloop()