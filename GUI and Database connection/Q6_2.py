import tkinter
from tkinter import *
import mysql.connector
import mysql
conn_obj = mysql.connector.connect(host="localhost", user="root", passwd="",database='pypro')
cr=conn_obj.cursor()
win1 = Tk()
win1.geometry('1000x500')
win1.config(bg='#283747')
l5=Label(win1,text='RECORDS',bg='#283747')
l5.config(font=("Hanson", 40))
l5.place(x=300,y=30)

cr.execute('select username,fname,lname,email from reg_table')
records=cr.fetchall()
prt=''
for rec in records:
        prt+=str(rec[0])+'\t\t'+ str(rec[1])+'\t\t'+ str(rec[2])+'\t\t\t'+ str(rec[3]) +'\n\n\n'
l3=Label(win1,text=prt,font=36,bg='#283747')
l3.place(x=100,y=180)
cr.execute("commit")
l4=Label(win1,text='USERNAME\tFIRST NAME\tLAST NAME\t\tEMAIL',font=36)
l4.place(x=100,y=100)

def vr1():
    win1.destroy()
    import Q6_1
b1 = tkinter.Button(win1, text='🔙', command=vr1,bg='#283747')
b1.config(font=("Courier", 20))
b1.place(x=150, y=40)
win1.mainloop()
