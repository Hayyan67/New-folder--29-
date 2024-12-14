from tkinter import *

root = Tk()
root.title('My window')
root.geometry('300x300')
root.config(background="yellow")

Login = Label(root,text="Enter your Login Id", bg="light blue", fg="red", font=('Arial', 30), padx=10, pady=10)
Login.pack()
Password = Label(root,text="Enter your password", bg="light green", fg="blue", font=('Arial', 12), padx=10, pady=10)
Password.pack()
e1=Entry(root)
e1.pack()
def msg():
    a1=e1.get()
    m1="Hey "+ a1+ "\n Welcome to my window"
    L3 = Label(root, text=m1)
    L3.pack()

b1 =Button(root, text='Submit', bg='red', fg='white')
b1.pack()
root.mainloop()