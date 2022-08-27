from tkinter import *
from tkinter import messagebox
import json

def view():
    pass

def add():
    global bookinfo1, bookinfo2, bookinfo3, bookinfo4, root
    root=Tk()
    root.geometry("700x600")
    root.minsize(455,500)
    root.title("Library Management System")

    Label(root,text="ADD BOOK",font=("times",28,"bold"),fg="yellow",bg="black").pack(side=TOP,fill=X)
    Label(root,text=" Enter the following details ",bg="grey",fg="black").pack(pady=5)

    labelframe = Frame(root,bg='black')
    labelframe.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    lb1 = Label(labelframe,text='Book ID : ',bg='black',fg='white')
    lb1.place(relx=0.05,rely=0.2,relheight=0.08)
    bookinfo1 = Entry(labelframe)
    bookinfo1.place(relx=0.3,rely=0.2,relwidth=0.62,relheight=0.08)
    lb2 = Label(labelframe,text='Title : ',bg='black',fg='white')
    lb2.place(relx=0.05,rely=0.35,relheight=0.08)
    bookinfo2 = Entry(labelframe)
    bookinfo2.place(relx=0.3,rely=0.35,relwidth=0.62,relheight=0.08)
    lb3 = Label(labelframe,text='Author : ',bg='black',fg='white')
    lb3.place(relx=0.05,rely=0.50,relheight=0.08)
    bookinfo3 = Entry(labelframe)
    bookinfo3.place(relx=0.3,rely=0.50,relwidth=0.62,relheight=0.08)
    lb4 = Label(labelframe,text='Status(avail/issued) : ',bg='black',fg='white')
    lb4.place(relx=0.05,rely=0.65,relheight=0.08)
    bookinfo4 = Entry(labelframe)
    bookinfo4.place(relx=0.3,rely=0.65,relwidth=0.62,relheight=0.08)

    Submit = Button(root,text='SUBMIT',bg='lightblue',fg='white',command=book_register)
    Submit.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)
    Quit = Button(root,text='QUIT',bg='lightblue',fg='white',command=root.destroy)
    Quit.place(relx=0.53,rely=0.9,relwidth=0.18,relheight=0.08)

    root.mainloop()
    
def book_register():

    book_id = bookinfo1.get()
    title = bookinfo2.get()
    author = bookinfo3.get()
    status = bookinfo4.get()
    
    a = {book_id:{'title':title, 'author':author, 'status':status}}
    with open('books.txt', 'a') as f:
        f.write("\n")
        f.write(json.dumps(a))
        messagebox.showinfo('Success',"Book added successfully")
    f.close()
    

def remove():
    pass

def issue():
    pass

def returns():
    global root, bookname
    root=Tk()
    root.geometry("400x150")
    root.title("Return Book")
    Label(root,text="Enter book id:",fg="black",font="comicsanms 11").pack(side=TOP)
    bookname=Entry(root)
    bookname.pack(side=TOP,fill=X,padx=50)
    Button(root,text="Exit",font=("times 11"),command=root.destroy).pack(side=BOTTOM,pady=15)
    Button(root,text="submit",font=("times 11"),command=addtodata).pack(side=BOTTOM,pady=5)

    root.mainloop()

def addtodata():
    p=bookname.get()
    with open("bookslist.txt", "a") as f:
        f.write(f"{p}\n")
    print(p," added")

root=Tk()
root.geometry("700x600")
root.minsize(455,500)
root.title("Library Management System")


Label(root,text="LIBRARY MANAGEMENT SYSTEM",font=("times",28,"bold"),fg="yellow",bg="black",relief=RIDGE,borderwidth=8).pack(side=TOP,fill=X)
Label(root,text=" WELCOME TO THE LIBRARY ",font=("avenir",18,"bold"),fg="lightgreen",bg="black").pack(side=TOP,padx=10,pady=15)
Label(root,text=" Pick an option to continue ",bg="grey",fg="black").pack(pady=5)
Button(root,text="View Books",padx=90,pady=10,command=view,font=("gotham",14),bg="lightblue").pack(padx=2,pady=4)
Button(root,text="Add Book",padx=100,pady=10,command=add,font=("gotham",14),bg="lightblue").pack(padx=2,pady=4)
Button(root,text="Remove Book",padx=80,pady=10,command=remove,font=("gotham",14),bg="lightblue").pack(padx=2,pady=4)
Button(root,text="Issue Book to student",padx=50,pady=10,command=issue,font=("gotham",14),bg="lightblue").pack(padx=2,pady=4)
Button(root,text="Return Book",padx=90,pady=10,command=returns,font=("gotham",14),bg="lightblue").pack(padx=2,pady=4)



root.mainloop()
