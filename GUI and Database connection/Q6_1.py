import tkinter
from tkinter import *
import mysql
import mysql.connector
conn_obj = mysql.connector.connect(host="localhost", user="root", passwd="",database='pypro')
cr=conn_obj.cursor()
win = Tk()
win.geometry('1000x500')
win.config(bg='#283747')
l5=Label(win,text='USER REGISTRATION',font=200,fg='#ffffff',bg='#283747')
l5.grid(row=1,column=1,padx=10,pady=10)

l1 = Label(win, text='USERNAME:', font=200,bg='#283747')
l1.grid(row=2,column=1,padx=10,pady=10)
l2 = Label(win, text='EMAIL:', font=100,bg='#283747')
l2.grid(row=2,column=3,padx=10,pady=10)

l2 = Label(win, text='FIRST NAME:', font=100,bg='#283747')
l2.grid(row=3,column=1,padx=10,pady=10)
l1 = Label(win, text='LAST NAME:', font=100,bg='#283747')
l1.grid(row=3,column=3,padx=10,pady=10)

l1 = Label(win, text='PASS:', font=100,bg='#283747')
l1.grid(row=4,column=1,padx=10,pady=10)
l2 = Label(win, text='CONFIRM PASS:', font=100,bg='#283747')
l2.grid(row=4,column=3,padx=10,pady=10)

def vr():
    win.destroy()
    import Q6_2

b1 = tkinter.Button(win, text='VIEW RECORDS ➤', command=vr, font=36,bg='#283747')
b1.grid(row=5,column=4,padx=10,pady=10)

def sv():
    e1 = tf_1.get()
    e2 = t2.get()
    e3 = t3.get()
    e4 = t4.get()
    e5 = t5.get()
    e6 = t6.get()
    cr.execute("insert into reg_table values('" + e1 + "','" + e2 + "','" + e3 + "','" + e4 + "','" + e5 + "','" + e6 + "')")
    cr.execute("commit");

tf_1 = Entry(win, font=36)
tf_1.grid(row=2,column=2,padx=10,pady=10)
t2 = Entry(win, font=36)
t2.grid(row=3,column=2,padx=10,pady=10)
t3 = Entry(win, font=36)
t3.grid(row=3,column=4,padx=10,pady=10)
t4 = Entry(win, font=36)
t4.grid(row=2,column=4,padx=10,pady=10)
t5 = Entry(win, font=36)
t5.grid(row=4,column=2,padx=10,pady=10)
t6 = Entry(win, font=36)
t6.grid(row=4,column=4,padx=10,pady=10)


b2 = tkinter.Button(win, text='SAVE', command=sv, font=36,bg='#283747')
b2.grid(row=5,column=2,padx=10,pady=10)


win.mainloop()
