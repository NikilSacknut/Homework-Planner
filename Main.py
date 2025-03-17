from tkinter import *
from tkinter import ttk
import os

def delete2():
    screen3.destroy()

def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("sucess")
    screen3.geometry("150x100")
    Label(screen3, text="Login Sucess").pack()
    Button(screen3, text= "OK", command=delete2).pack()


def password_not_recognised():
    print("working")


def user_not_found():
    print("working")


def register_user():
    print("working")

    #files and storing user data
    username_info = username.get()
    password_info = password.get()

    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

#Registration successs message
    Label(screen1, text="Registration Success", fg="green", font = ("calibri", 11)).pack()


#function which verifies if youve logged in or not 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0, END)

# if statements to verify the username and password
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
           login_sucess()
        else:
           passowrd_not_recognised()
    
    else:
        user_not_found()



def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")


    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

#Registration Page (where you register if you haven't made an acocunt yet)
    Label(screen1, text = "Please enter details below *  \n (make sure not to put a different password as it \n will not be stored securely) ").pack() 
    Label(screen1, text = "Username * ").pack() 
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password * ").pack() 
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    password_entry.pack()
    Label(screen1, text = "").pack() 
    Button(screen1, text= "Register", width= 10, height= 1, command= register_user).pack()





#login function which runs the login box
def login():
    global screen2 
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text= "").pack()
    
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    
    global username_entry1
    global password_entry1

    Label(screen2, text= "Username").pack()
    username_entry1 = Entry(screen2,textvariable= username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text= "").pack()
    Button(screen2, text="Login", width= 10, height= 1, command = login_verify).pack()
    

#Main screen Page (the login page)
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Rosmini Homework Planner 2025")
    Label(text="Rosmini Homework Planner", bg="blue", fg="red", width="300", height="2", font=("Calibri", 15), padx=10, pady=10).pack()
    Label(text = "").pack()
    Button(text = "Login", height="2", width="30", command=login).pack()
    Label(text = "").pack() 
    Label(text = "If you dont have an account register here!", width="300", height="2", font = ("Calibri", 9)).pack()
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

    


















    