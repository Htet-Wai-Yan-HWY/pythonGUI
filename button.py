import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo

#window
root =tk.Tk()
root.geometry("600x600")
root.resizable(False,False)
root.title("BUTTON DEMO")

#exit button
exit_button =ttk.Button(
    root,
    text="EXIT",
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=10,
    ipady=5,
    expand=True
)

root.mainloop()