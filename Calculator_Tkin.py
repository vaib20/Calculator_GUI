from tkinter import *
root = Tk()
root.geometry("300x310")
root.resizable(0,0)
root.title("Calculator")
root.wm_iconbitmap("Calculator.ico")
# root.configure(background="grey")
def show(c):
    value1.set(value1.get()+c)

def equals():
    a1 = value1.get()
    value1.set(eval(a1))

def clear1():
    value1.set("")

value1 = StringVar()
Entry(root, textvariable=value1, font="Arial 30 bold",justify="right").pack(padx=10, pady=20)

f1 = Frame(root)
b1 = Button(f1, text="7", height=2, width=7, bg="black", fg="white", activebackground="grey", font="Arial 10 bold")
b1.pack(side=LEFT, padx=3)
b1.configure(command=lambda:show("7"))

b2 = Button(f1, text="8", height=2, width=7, bg="black", fg="white", activebackground="grey", font="Arial 10 bold")
b2.pack(side=LEFT, padx=3)
b2.configure(command=lambda:show("8"))

b3 = Button(f1, text="9", height=2, width=7, bg="black", fg="white", activebackground="grey", font="Arial 10 bold")
b3.pack(side=LEFT, padx=3)
b3.configure(command=lambda:show("9"))

b4 = Button(f1, text="C", height=2, width=7, bg="black", fg="white", activebackground="grey", font="Arial 10 bold")
b4.pack(side=LEFT, padx=3)
b4.configure(command=clear1)
f1.pack()


f2 = Frame(root)
b5 = Button(f2, text="4", height=2, width=7, bg="black", fg="white", activebackground="grey", font="Arial 10 bold")
b5.pack(side=LEFT, padx=3, pady=3)
b5.configure(command=lambda:show("4"))

b6 = Button(f2, text="5", height=2, width=7, bg="black", fg="white", activebackground="grey", font="Arial 10 bold")
b6.pack(side=LEFT, padx=3, pady=3)
b6.configure(command=lambda:show("5"))

b7 = Button(f2, text="6", height=2, width=7, bg="black", fg="white", activebackground="grey", font="Arial 10 bold")
b7.pack(side=LEFT, padx=3, pady=3)
b7.configure(command=lambda:show("6"))

b8 = Button(f2, text="*", height=2, width=7, bg="black", fg="white", activebackground="grey", font="Arial 10 bold")
b8.pack(side=LEFT, padx=3, pady=3)
b8.configure(command=lambda:show("*"))
f2.pack()


f3 = Frame(root)
b9 = Button(f3, text="1", height=2, width=7, bg="black", fg="white", activebackground="grey", font="Arial 10 bold")
b9.pack(side=LEFT, padx=3, pady=3)
b9.configure(command=lambda:show("1"))

b10 = Button(f3, text="2", height=2, width=7, bg="black", fg="white", activebackground="grey", font="Arial 10 bold")
b10.pack(side=LEFT, padx=3, pady=3)
b10.configure(command=lambda:show("2"))

b11 = Button(f3, text="3", height=2, width=7, bg="black", fg="white", activebackground="grey", font="Arial 10 bold")
b11.pack(side=LEFT, padx=3, pady=3)
b11.configure(command=lambda:show("3"))

b12 = Button(f3, text="+", height=2, width=7, bg="black", fg="white", activebackground="grey", font="Arial 10 bold")
b12.pack(side=LEFT, padx=3, pady=3)
b12.configure(command=lambda:show("+"))
f3.pack()


f4 = Frame(root)
b13 = Button(f4, text="-", height=2, width=7, bg="black", fg="white", activebackground="grey", font="Arial 10 bold")
b13.pack(side=LEFT, padx=3, pady=3)
b13.configure(command=lambda:show("-"))

b14 = Button(f4, text="0", height=2, width=7, bg="black", fg="white", activebackground="grey", font="Arial 10 bold")
b14.pack(side=LEFT, padx=3, pady=3)
b14.configure(command=lambda:show("0"))

b15 = Button(f4, text="/", height=2, width=7, bg="black", fg="white", activebackground="grey", font="Arial 10 bold")
b15.pack(side=LEFT, padx=3, pady=3)
b15.configure(command=lambda:show("/"))

b16 = Button(f4, text="=", height=2, width=7, bg="black", fg="white", activebackground="grey", font="Arial 10 bold")
b16.pack(side=LEFT, padx=3, pady=3)
b16.configure(command=equals)
f4.pack()

root.mainloop()
