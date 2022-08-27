from tkinter import *
from tkinter import messagebox


def bookreturn():
    global book_id, student_id, root1

    def returnbook():
        p=book_id.get()
        q=student_id.get()
        if p and q:
            messagebox.showinfo("Returns","Book returned succesfully. Thank you!")
        else:
            messagebox.showerror("Invalid ID","Please enter a valid ID")

        root1.destroy()
        return

    root1=Tk()
    root1.geometry("449x380")
    root1.maxsize(449,380)
    root1.minsize(449,380)
    root1.title("Return Book")
    heading=Label(root1,text="RETURN BOOK",bg='black',fg='yellow',font="gotham 28 bold",borderwidth=10,relief=SUNKEN,padx=75,pady=8)
    heading.grid(row=0,column=0)

    f1=Frame(root1,height=600,width=700,bg="black",pady=50,padx=80)
    f1.grid(row=3,column=0,pady=5)
    Label(f1,text="Enter book id:",bg="black",fg="white",font="comicsanms 11",padx=10,pady=10).grid(row=3,column=1)
    book_id=Entry(f1)
    book_id.grid(row=3,column=2)
    Label(f1,text="Enter student id:",bg="black",fg="white",font="comicsanms 11",padx=10,pady=10).grid(row=4,column=1)
    student_id=Entry(f1)
    student_id.grid(row=4,column=2)
    Button(f1,text="Exit",font=("times 11 bold"),command=root1.destroy,padx=8).grid(row=6,column=2,padx=10,pady=10)
    Button(f1,text="Submit",font=("times 11 bold"),command=returnbook).grid(row=5,column=2,padx=10,pady=10)
    
    

    root1.mainloop()
    

#bookreturn()
