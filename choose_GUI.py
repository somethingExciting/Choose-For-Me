# import modules
import tkinter as tk
import os
from tkinter import *
from tkinter import messagebox
# import custom modules
import choose_functions


class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height=50, width=50)
        # variables
        self.isClicked = False
        self.text = StringVar()
        self.text.set("No decision made yet...")

        # labels
        self.label = tk.Label(self, text="Input your choices as comma separated values: ")
        self.label.grid(row=0, column=0)
        self.choice = tk.Label(self, textvariable=self.text, fg="red", font=("Arial", 16))
        self.choice.grid(row=4, column=0)

        # Entry
        self.entry = tk.Text(self, height=10, width=40)
        self.entry.grid(row=1, column=0)

        # Buttons
        self.choose_btn = tk.Button(self, text="Choose!", command=self.choose)
        self.choose_btn.grid(row=2, column=0, sticky="NEWS")
        self.clear_btn = tk.Button(self, text="Clear", command=self.clear_text)
        self.clear_btn.grid(row=3, column=0, sticky="NEWS")

        # Resizing
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)
        self.grid_rowconfigure(3,weight=1)

    def clear_text(self):
        self.entry.delete("1.0", END)

    def choose(self):
        if not self.entry.get("1.0", END):
            print("Error: No input detected")
            self.text.set("No input detected!")
        else:
            self.text.set(choose_functions.this_or_that(self.entry.get("1.0", END)))


def pls_look_pretty():
    root = Tk()
    root.geometry('500x250')
    root.title('This or That')
    root.iconbitmap(os.getcwd()+"/icon.ico")
    App(root).pack(expand=True, fill='both')
    root.mainloop()


if __name__ == "__main__":
    pls_look_pretty()
