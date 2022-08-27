from tkinter import *

def view():
    from view_books import viewbooks
    viewbooks()

def add():
    from add_book import bookadd
    bookadd()

def remove():
    from remove_book import bookremove
    bookremove()

def issue():
    from  issue_book import bookissue
    bookissue()

def returns():
    from return_book import bookreturn
    bookreturn()

    
root=Tk()
root.geometry("700x600")
root.minsize(655,500)
root.wm_iconbitmap('book_PNG51090.ico')
root.title("Library Management System-Dashboard")

bg=PhotoImage(file="bird-library-livestream.png")
Label(root,image=bg).place(x=0,y=0)

Label(root,text="LIBRARY MANAGEMENT SYSTEM",font=("times",28,"bold"),bg="#eba16a",fg="black",relief=RIDGE,borderwidth=8,pady=6).pack(side=TOP,fill=X)
Label(root,text=" WELCOME TO THE LIBRARY ",font=("avenir",18,"bold"),fg="#57574f",bg="#f5f267").pack(side=TOP,padx=10,pady=15)
Label(root,text=" Pick an option to continue ",bg="#c0ebeb",fg="black").pack(pady=5)

Button(root,text="View Books",padx=90,pady=10,command=view,font=("gotham",14),bg="black",fg="#b6fc03").pack(padx=2,pady=4)
Button(root,text="Add Book",padx=100,pady=10,command=add,font=("gotham",14),bg="black",fg="#b6fc03").pack(padx=2,pady=4)
Button(root,text="Remove Book",padx=80,pady=10,command=remove,font=("gotham",14),bg="black",fg="#b6fc03").pack(padx=2,pady=4)
Button(root,text="Issue Book to student",padx=50,pady=10,command=issue,font=("gotham",14),bg="black",fg="#b6fc03").pack(padx=2,pady=4)
Button(root,text="Return Book",padx=90,pady=10,command=returns,font=("gotham",14),bg="black",fg="#b6fc03").pack(padx=2,pady=4)



root.mainloop()
