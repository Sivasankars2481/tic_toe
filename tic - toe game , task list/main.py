import tkinter.messagebox
from tkinter import *

obj = Tk()
obj.geometry('400x400')
obj.title('Calculator')

obj.configure(bg='light blue')


def divide():
    num1 = number1.get()
    num2 = number2.get()
    result = num1/num2
    tkinter.messagebox.showinfo('Result Data', 'Result: '+str(result))


Label(obj, text='Enter Value A:', font=('calibre', 15), bg='light blue').place(x=30, y=30)
Label(obj, text='Enter Value B:', font=('calibre', 15), bg='light blue').place(x=30, y=80)

number1 = IntVar()
number2 = IntVar()

Entry(obj, textvariable=number1, font=('calibri', 13)).place(x=180, y=30)
Entry(obj, textvariable=number2, font=('calibri', 13)).place(x=180, y=80)

Button(obj, text ='divide',font=('calibri',15),bg='blue',fg='white',width='10',height='1',command =divide).place(x=150,y=200)
obj.mainloop()
