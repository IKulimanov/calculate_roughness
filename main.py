from tk_gui_app import Example
from tkinter import Tk, Frame, BOTH


def main():
    root = Tk()
    # root.geometry("500x+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
