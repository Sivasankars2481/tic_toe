import tkinter.messagebox
from tkinter import *
import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', password='', db='Product')
cursor = db.cursor()


def update():
    def list_update():
        id = Pro_Id.get()
        name = Pro_name.get()
        price = Pro_price.get()
        qty = Pro_qty.get()
        cursor.execute('update  detail set name=%s,price=%s,qty=%s where id = %s', [name, price, qty, id])
        db.commit()
        tkinter.messagebox.showinfo('Product List', 'updated')
    global Pro_Id, Pro_name, Pro_price, Pro_qty, list_up
    list_up = Tk()
    list_up.geometry('500x400')
    list_up.title('Update')
    list_up.configure(bg='lightgreen')
    Label(list_up, text='Product ID', font=('calibri', 15)).place(x=30, y=30)
    Label(list_up, text='Product Name', font=('calibri', 15)).place(x=30, y=80)
    Label(list_up, text='Product price', font=('calibri', 15)).place(x=30, y=130)
    Label(list_up, text='Product Quantity', font=('calibri', 15)).place(x=30, y=180)

    Pro_Id = StringVar()
    Pro_name = StringVar()
    Pro_price = StringVar()
    Pro_qty = StringVar()

    Entry(list_up, textvariable=Pro_Id, font=('calibri', 13), bg='lightgreen',
          ).place(x=240, y=30)
    Entry(list_up, textvariable=Pro_name, font=('calibri', 13), bg='lightgreen',
          ).place(x=240, y=80)

    Entry(list_up, textvariable=Pro_price, font=('calibri', 13), bg='lightgreen',
          ).place(x=240, y=130)
    Entry(list_up, textvariable=Pro_qty, font=('calibri', 13), bg='lightgreen',
          ).place(x=240, y=180)
    Button(list_up, text='Update', font=('calibri', 13), bg='green',
           width='8', height='1', fg='white',command=list_update).place(x=200,y=230)

def add():
    def add_list():
        id = Pro_Id.get()
        name = Pro_name.get()
        price = Pro_price.get()
        qty = Pro_qty.get()
        cursor.execute('insert into detail values(%s,%s,%s,%s)', [id, name, price, qty])
        db.commit()
        tkinter.messagebox.showinfo('Product List', 'Added')
    global Pro_Id,Pro_name, Pro_price, Pro_qty, list_add
    list_add = Tk()
    list_add.geometry('500x400')
    list_add.title('ADD')
    list_add.configure(bg='lightgreen')
    Label(list_add, text='Product ID', font=('calibri', 15)).place(x=30, y=30)
    Label(list_add, text='Product Name', font=('calibri', 15)).place(x=30, y=80)
    Label(list_add, text='Product price', font=('calibri', 15)).place(x=30, y=130)
    Label(list_add, text='Product Quantity', font=('calibri', 15)).place(x=30, y=180)

    Pro_Id = StringVar()
    Pro_name = StringVar()
    Pro_price = StringVar()
    Pro_qty = StringVar()

    Entry(list_add, textvariable=Pro_Id, font=('calibri', 13), bg='lightgreen',
          ).place(x=240, y=30)
    Entry(list_add, textvariable=Pro_name, font=('calibri', 13), bg='lightgreen',
          ).place(x=240, y=80)

    Entry(list_add, textvariable=Pro_price, font=('calibri', 13), bg='lightgreen',
          ).place(x=240, y=130)
    Entry(list_add, textvariable=Pro_qty, font=('calibri', 13), bg='lightgreen',
          ).place(x=240, y=180)
    Button(list_add, text='ADD', font=('calibri', 13), bg='green',
           width='8', height='1', fg='white',command= add_list).place(x=200,y=230)

def view():
    Label(page, text='Product List', font=('calibri', 25)).place(x=200, y=20)
    cursor.execute('select *from detail')
    data = cursor.fetchall()
    rows= len(data)
    cols=len(data[0])
    Label(page, text='Product ID', font=('calibri', 15),bg='lightblue',).grid(row=1,column=0)
    Label(page, text='Product Name', font=('calibri', 15), bg='lightblue', ).grid(row=1, column=1)
    Label(page, text='Product Price', font=('calibri', 15), bg='lightblue', ).grid(row=1, column=2)
    Label(page, text='Product Quantity', font=('calibri', 15), bg='lightblue', ).grid(row=1, column=3)
    for i in range(rows):
        for j in range(cols):
             s = Entry(page, font=('calibri', 15))
             s.grid(row=i+2,column=j)
             s.insert(END,data[i][j])





def start():
    global page
    page = Tk()
    page.geometry('1300x600')
    page.title('Authentication')
    page.configure(bg='lightgreen')
    Label(page, text='Product List', font=('calibri', 25)).place(x=500, y=20)
    Label(page, )
    Button(page, text='Add', font=('calibri', 15), bg='green', fg='white',
           width='12', height='1',command= add ).place(x=60, y=500)
    Button(page, text='Update', font=('calibri', 15), bg='green', fg='white',
           width='12', height='1', command=update).place(x=500, y=500)
    Button(page, text='Delete', font=('calibri', 15), bg='green', fg='white',

           width='12', height='1' ).place(x=1000, y=500)
    Button(page, text='View', font=('calibri', 15), bg='green', fg='white',

           width='12', height='1',command=view).place(x=1200, y=500)

    page.mainloop()


start()

