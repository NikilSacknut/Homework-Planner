import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("Rosmini Homework Planner")

def add_to_list(event=None): #links to the callback function which enables "enter button"
    text = entry.get()
    if text: 
        text_list.insert(tk.END, text)
        entry.delete(0, tk.END)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = tk.Frame(root) #Container for window 
frame.grid(row=0, column=0, sticky="nsew")

frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)


entry = tk.Entry(frame) #pass onto frame which includes it
entry.grid(row=0, column=0, sticky="ew")

entry.bind("<Return>", add_to_list) #Call back and addes keyboard function

entry_btn = tk.Button(frame, text="Add", command=add_to_list)
entry_btn.grid(row=0, column=1)  

text_list = tk.Listbox(frame)
text_list.grid(row=1, column=0, columnspan=2, sticky="nsew")

root.mainloop()