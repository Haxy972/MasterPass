import tkinter
from tkinter import messagebox, N, W, E, S

from Utils import YamlFile, Logs


class AppWindow:


    def on_closing(self):
        self.send_notification(1, "You will not have access to the entire application")
        self.logger.information("Quit confirmation message sent")
        if messagebox.askokcancel("Quitter", "You really want to quit ?"):
            self.close()

        return

    def __init__(self, window_name: str, size: str, can_close: bool, resizable: bool):
        self.window = tkinter.Tk()
        self.yaml_file = YamlFile("cache/settings.yaml")
        self.logger = Logs("latest.log")
        self.window.geometry(size)
        self.title = window_name
        self.window.title("MasterPass - " + window_name)
        self.window.config(background="#cc2146")
        self.frame = tkinter.Frame(self.window, background="#cc2146")
        text = tkinter.Label(self.window, text=window_name, font=("Helvetica", 20), bg='#cc2146', fg='white')
        text.pack(pady=30)
        self.frame.pack(expand=1)
        if not resizable:
            self.window.resizable(False, False)
        if not can_close:
            self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def execute_loop(self):
        self.logger.information("Window: " + self.title + " has been opened")
        self.window.mainloop()

    def get_window(self):
        return self.window

    def get_frame(self):
        return self.frame

    def send_notification(self, level: int, message: str):
        try:
            if level == 1:
                self.logger.information("Information message sent: " + message)
                tkinter.messagebox.showinfo(self.title, message)
            elif level == 2:
                self.logger.information("Warning message sent: " + message)
                tkinter.messagebox.showwarning(self.title, message)
            elif level == 3:
                self.logger.information("Error message sent: " + message)
                tkinter.messagebox.showerror(self.title, message)

        except Exception:
            self.logger.critical("Display:send_notification(level, message)(l.42): Error")

    def close(self):
        self.window.destroy()
        self.logger.information("Window with title: " + self.title + " terminated")


def get_check(check_var):
    return check_var.get()


class ConditionsWindow(AppWindow):

    def __init__(self, window_name: str, size: str, can_close: bool, resizable: bool):
        super().__init__(window_name, size, can_close, resizable)
        text_container = tkinter.Text(self.get_frame(), width=60)
        scroll = tkinter.Scrollbar(text_container, orient=tkinter.VERTICAL, command=text_container.yview)
        scroll.pack(side='right', ipady=40)
        text_container.pack(padx=(10, 10), fill='x')
        text_container['yscrollcommand'] = scroll.set
        text_container.insert('end',
                              'Adipiscing enim eu turpis egestas pretium aenean. Leo integer malesuada nunc vel risus commodo viverra maecenas. Nunc mattis enim ut tellus elementum sagittis vitae et leo. Risus in hendrerit gravida rutrum quisque non tellus orci ac. Habitant morbi tristique senectus et. Amet commodo nulla facilisi nullam vehicula. Velit dignissim sodales ut eu sem integer vitae justo eget. Congue eu consequat ac felis donec. Sed odio morbi quis commodo odio. Purus sit amet volutpat consequat. Orci dapibus ultrices in iaculis nunc sed augue. Eget arcu dictum varius duis at consectetur lorem donec. Sit amet justo donec enim. Tincidunt tortor aliquam nulla facilisi cras. Gravida arcu ac tortor dignissim convallis aenean et tortor at. Id aliquet risus feugiat in ante metus dictum.')
        text_container.config(state='disabled')
        check_var = tkinter.IntVar()
        checkBox = tkinter.Checkbutton(self.get_frame(),
                                       text="Accepter les Conditions Générale d'Utilisation (CGU)",
                                       bg="#cc2146", fg="black", variable=check_var, onvalue=1, offvalue=0)
        checkBox.config(highlightbackground='#cc2146', highlightcolor='#cc2146')
        checkBox.pack()
        button = tkinter.Button(self.get_frame(), text="Confirmer",
                                command=lambda: self.launch_default_app(check_var))
        button.pack(pady=30)

    def launch_default_app(self, check_var):
        if get_check(check_var):
            self.yaml_file.register_key("approve_conditions", True, Logs("latest.log"))

            self.close()
            launch_app_window()
        else:
            self.send_notification(1, "You need to check the check box, before continue")



def launch_condition_window():
    window = ConditionsWindow("General conditions", "500x400", False, False)
    window.execute_loop()

def launch_app_window():
    window = AppWindow("Main Menu", "600x500", True, False)
    window.execute_loop()