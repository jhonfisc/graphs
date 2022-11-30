from tkinter import messagebox


def showMessageBox(title, msg, opcional=None):
    messagebox.showwarning(title, msg.replace("%", opcional) if opcional is not None else msg)
