from tkinter import *
from tkinter import messagebox


def bookissue():
    global book_id, student_id, root3

    def issuebook():
        p=book_id.get()
        q=student_id.get()
        if p and q:
            with open("books.txt", "r") as f:
                data=f.read()
                if p in data:
                    for line in data.split('\n'):
                        if p in line:
                            if "avail" in line:
                                messagebox.showinfo("Issues","Book successfully issued to student.")
                            else:
                                messagebox.showinfo("Issues","Book isn't available. Please try Later.")
                        
                else:
                    messagebox.showerror("Invalid ID","Please enter a valid book ID")
                    
        else:
            messagebox.showerror("Invalid ID","Please enter a valid ID")
            
        root3.destroy()
        return

    root3=Tk()
    root3.geometry("433x375")
    root3.maxsize(433,375)
    root3.minsize(433,375)
    root3.title("Issue Book")
    heading=Label(root3,text=" ISSUE BOOK ",bg='black',fg='yellow',font="gotham 28 bold",borderwidth=10,relief=SUNKEN,padx=80,pady=8)
    heading.grid(row=0,column=0)

    f1=Frame(root3,height=600,width=680,bg="black",pady=50,padx=80)
    f1.grid(row=3,column=0,pady=5)
    Label(f1,text="Enter book id:",bg="black",fg="white",font="comicsanms 11",padx=10,pady=10).grid(row=3,column=1)
    book_id=Entry(f1)
    book_id.grid(row=3,column=2)
    Label(f1,text="Enter student id:",bg="black",fg="white",font="comicsanms 11",padx=10,pady=10).grid(row=4,column=1)
    student_id=Entry(f1)
    student_id.grid(row=4,column=2)
    Button(f1,text="Exit",font=("times 11 bold"),command=root3.destroy,padx=8).grid(row=6,column=2,padx=10,pady=10)
    Button(f1,text="Submit",font=("times 11 bold"),command=issuebook).grid(row=5,column=2,padx=10,pady=10)
    
    

    root3.mainloop()
    

#bookissue()
