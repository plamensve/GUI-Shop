from tkinter import Tk, Canvas, PhotoImage
from tkinter.ttk import Label


def create_root():
    root = Tk()

    root.title("GUI Shop")
    root.geometry("700x600")
    root.resizable(False, False)

    return root


def create_frame():
    frame = Canvas(root, width=800, height=700, bg='#3B3B3B')
    frame.grid(row=0, column=0)
    return frame


root = create_root()
frame = create_frame()
