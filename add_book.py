from tkinter import *
from tkinter import messagebox

def bookadd():
    global bookinfo1, bookinfo2, bookinfo3, bookinfo4, root5

    def addbook():

        book_id = bookinfo1.get()
        title = bookinfo2.get()
        author = bookinfo3.get()
        status = bookinfo4.get()
        
        with open('books.txt', 'a') as f:
            f.write(f"\n{book_id}: {{TITLE:  {title}, AUTHOR:  {author}, STATUS:  {status} }}")
            messagebox.showinfo('Success',"Book added successfully")
        
        root5.destroy()
        return

    root5=Tk()
    root5.geometry("600x500")
    root5.minsize(200,250)
    root5.title("Add book")
    root5.configure(bg="#323835")

    Label(root5,text="ADD BOOK",font=("times",28,"bold"),fg="yellow",bg="black",borderwidth=11,relief=SUNKEN).pack(side=TOP,fill=X)
    Label(root5,text=" Enter the following details ",fg="white",bg="#323835").pack(pady=15)

    labelframe = Frame(root5,height=800,width=600,bg='#323835')
    labelframe.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.45)
    lb1 = Label(labelframe,text='Book ID : ',bg='#323835',fg='white')
    lb1.place(relx=0.05,rely=0.2,relheight=0.08)
    bookinfo1 = Entry(labelframe)
    bookinfo1.place(relx=0.3,rely=0.2,relwidth=0.62,relheight=0.08)
    lb2 = Label(labelframe,text='Title : ',bg='#323835',fg='white')
    lb2.place(relx=0.05,rely=0.35,relheight=0.08)
    bookinfo2 = Entry(labelframe)
    bookinfo2.place(relx=0.3,rely=0.35,relwidth=0.62,relheight=0.08)
    lb3 = Label(labelframe,text='Author : ',bg='#323835',fg='white')
    lb3.place(relx=0.05,rely=0.50,relheight=0.08)
    bookinfo3 = Entry(labelframe)
    bookinfo3.place(relx=0.3,rely=0.50,relwidth=0.62,relheight=0.08)
    lb4 = Label(labelframe,text='Status(avail/issued) : ',bg='#323835',fg='white')
    lb4.place(relx=0.05,rely=0.65,relheight=0.08)
    bookinfo4 = Entry(labelframe)
    bookinfo4.place(relx=0.3,rely=0.65,relwidth=0.62,relheight=0.08)

    Submit = Button(labelframe,text='Submit',font=("times 11 bold"),command=addbook)
    Submit.place(relx=0.3,rely=0.83,relwidth=0.18,relheight=0.15)
    Quit = Button(labelframe,text='Quit',font=("times 11 bold"),command=root5.destroy)
    Quit.place(relx=0.53,rely=0.83,relwidth=0.18,relheight=0.15)

    root5.mainloop()

#bookadd()
