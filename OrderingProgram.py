from tkinter import *
from tkinter import ttk
import sqlite3


def register():
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Username * ").pack() 
    Entry(screen1, textvariable = username)
    Label(screen1, text = "Password * ").pack() 
    Entry(screen1, textvariable = password)


def login():
    print("Login session started")


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Rosmini Homework Planner 2025")
    Label(text = "Rosmini Homework Planner", bg="grey", width="300", height="2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height="2", width="30", command=login).pack()
    Label(text = "").pack() 
    Button(text = "Register", height = "2", width = "30", command=register).pack()

    screen.mainloop()

main_screen()






def main():
    app = Application()
    app.mainloop()


class Application(tk.Tk): 
    def __init__(self):
        super().__init__()
        self.title("Rosmini Homework Planner")
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1) 

        frame = InputForm(self) #Container for window 
        frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        frame2 = InputForm(self) #Container for window 
        frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        
#input form frame
class InputForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.entry = ttk.Entry(self) #pass onto frame which includes it
        self.entry.grid(row=0, column=0, sticky="ew")

        self.entry.bind("<Return>", self.add_to_list) #Call back and addes keyboard function

        self.entry_btn = ttk.Button(self, text="Add", command=self.add_to_list)
        self.entry_btn.grid(row=0, column=1)  

        self.text_list = tk.Listbox(self)
        self.text_list.grid(row=1, column=0, columnspan=2, sticky="nsew")

    def add_to_list(self, event=None):
        text = self.entry.get()
        if text:
            self.text_list.insert(tk.END, text)
            self.entry.delete(0, tk.END)


if __name__ == "__main__":
    main()

    


















    