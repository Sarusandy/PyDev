from Tkinter import *
import mysql.connector as m

root = Tk()

def retrieve_rows(eno):
    db = m.connect(user='root',password='sarusandy',database='world')
    cursor = db.cursor()

    args=(eno)
    print "employee no=",eno
    sql = "select * from emp where eno = {}".format(args)
    print sql;
    cursor.execute(sql)
    row = cursor.fetchone()
    if row is not None:
        lbl=Label(text=row).place(x=50,y=200)
    else:
        lbl=Label(text="No record Found").place(x=50,y=200)
    cursor.close()
    db.close()

def display(self):
    str=e1.get()
    lbl=Label(text="You entered "+str).place(x=50,y=150)
    s=int(str)
    print s
    retrieve_rows(int(str))

f=Frame(root, height=350, width=600)
#f.propogate(0)
f.pack()

l1=Label(text="Enter Employee Number")
e1 = Entry(f, width=15, fg='blue', bg='yellow')

e1.bind("<Return>",display)
l1.place(x=50,y=100)
e1.place(x=300,y=100)

root.mainloop()
    
