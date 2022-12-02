import tkinter as tk 
from tkinter import ttk 
from tkinter.messagebox import showinfo

#root window 
root=tk.Tk()
root.geometry("600x600")
# root.resizable(False,False)
root.title("IMAGE BUTTON DEMO")

#add
shutdown_icon = tk.PhotoImage(file="./assects/shutdown.png")

exit_button =ttk.Button(
    root,
    image=shutdown_icon,
    text="shutdown",
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=10,
    ipady=5,
    expand=True
)

root.mainloop()