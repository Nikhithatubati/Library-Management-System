from tkinter import *
import pymysql
from tkinter import messagebox
def connecting_SQL():
    mypass = "Nikhitha"#use your own password
    mydatabase = "db" #The database name
    con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()
    issueTable = "books_issued"
    bookTable = "books"
def view():
    pass

def add():
    pass

def removebook():
    connecting_SQL()
    issueTable = "books_issued"
    bookTable = "books"
    bid = bookInfo1.get()
    
    deleteSql = "delete from "+bookTable+" where bid = '"+bid+"'"
    deleteIssue = "delete from "+issueTable+" where bid = '"+bid+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        messagebox.showinfo('Success',"Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")
    
    print(bid)
    bookInfo1.delete(0, END)
    root.destroy()

def remove():
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(455,500)
    root.geometry("700x600")

        
    Label(root, text="Delete Book", font=("times",28,"bold"),  fg="yellow", bg="black").pack(side=TOP, fill=X)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    Button(root,text="SUBMIT",bg="lightblue", fg="black",command=removebook).place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    Button(root,text="Quit",bg="lightblue", fg="black", command=root.destroy).place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def issue():
    pass

def returnbook():
    pass

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
Button(root,text="Return Book",padx=90,pady=10,command=returnbook,font=("gotham",14),bg="lightblue").pack(padx=2,pady=4)



root.mainloop()
