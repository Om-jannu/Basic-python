import tkinter
from tkinter import *
import mysql.connector
import mysql
conn_obj = mysql.connector.connect(host="localhost", user="root", passwd="",database='pypro')
cr=conn_obj.cursor()
win = Tk()
win.geometry('1900x1080')
win.config(bg='#b3e8ff')
l5=Label(win,text='USER REGISTRATION',font=100,fg='#2f0023',bg='#b3e8ff')
l5.place(x=500,y=30)
l1 = Label(win, text='USERNAME:', font=100,bg='#b3e8ff')
l1.place(x=200, y=100)
l2 = Label(win, text='FIRST NAME:', font=100,bg='#b3e8ff')
l2.place(x=200, y=200)
l1 = Label(win, text='LAST NAME:', font=100,bg='#b3e8ff')
l1.place(x=200, y=300)
l2 = Label(win, text='EMAIL:', font=100,bg='#b3e8ff')
l2.place(x=700, y=100)
l1 = Label(win, text='PASS:', font=100,bg='#b3e8ff')
l1.place(x=700, y=200)
l2 = Label(win, text='CONFIRM PASS:', font=100,bg='#b3e8ff')
l2.place(x=700, y=300)



def vr():
    win.destroy()
    import Q6_2

b1 = tkinter.Button(win, text='VIEW RECORDS ➤', command=vr, font=36,bg='#f0af75')
b1.place(x=800, y=450)

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
tf_1.place(x=350, y=100)
t2 = Entry(win, font=36)
t2.place(x=350, y=200)
t3 = Entry(win, font=36)
t3.place(x=350, y=300)
t4 = Entry(win, font=36)
t4.place(x=900, y=100)
t5 = Entry(win, font=36)
t5.place(x=900, y=200)
t6 = Entry(win, font=36)
t6.place(x=900, y=300)


b2 = tkinter.Button(win, text='SAVE', command=sv, font=36,bg='#f0af75')
b2.place(x=300, y=450)


win.mainloop()
