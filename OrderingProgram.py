import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("Rosmini Homework Planner")

def add_to_list():
    text = entry.get()
    if text: 
        text_list.insert(tk.END, text)
        entry.delete(0, tk.END)



frame = tk.Frame(root) #Container for window 
frame.grid(row=0, column=0)

entry = tk.Entry(frame) #pass onto frame which includes it
entry.grid(row=0, column=0)

entry_btn = tk.Button(frame, text="Add", command=add_to_list)
entry_btn.grid(row=0, column=1)

text_list = tk.Listbox(frame)
text_list.grid(row=1, column=0)

root.mainloop()