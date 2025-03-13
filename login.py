import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


frame_styles = {"relief": "groove",
                "bd": 3, "bg": "#BEB2A7",
                "fg": "#073bb3", "font": ("Arial", 9, "bold")}


class LoginPage(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#708090", height=430, width=630) #Adding in the background
        main_frame.pack(fill="both", expand="true")

        self.geometry("630x430") #setting window size
        self.resizable(0, 0)
        title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "blue"}

        text_styles = {"font": ("Verdana", 14),
                       "background": "blue",
                       "foreground": "#E1FFFF"}

        frame_login = tk.Frame(main_frame, bg="blue", relief="groove", bd=2) #holds all the buttons
        frame_login.place(reply=0.30, relx=0.17, height=130, width=400)
        

root.mainloop()