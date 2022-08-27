from tkinter import *
from tkinter import messagebox

def bookremove():
    global book_id, root2

    def removebook():  
        bid=book_id.get()
        if bid:
            with open("books.txt", "r") as f_old:
                data=f_old.read()
                with open("books.txt", "w") as f_new:
                    data=data.split('\n')
                    for j in data:
                        if bid in j:
                            pass
                        else:
                            f_new.write(f"{j}\n")
            messagebox.showinfo("Book Removed","Book removed from data.")
        else:
            messagebox.showerror("Invalid ID","Please enter correct book id.")

        root2.destroy()
        return
        
    
    root2=Tk()
    root2.geometry("455x300")
    root2.maxsize(455,300)
    root2.minsize(455,300)
    root2.title("Remove Book")
    heading=Label(root2,text="REMOVE BOOK",bg='black',fg="yellow",font="gotham 28 bold",borderwidth=10,relief=SUNKEN,padx=75,pady=8)
    heading.grid(row=0,column=0)

    f1=Frame(root2,height=10,width=700,bg="black",pady=30,padx=100)
    f1.grid(row=3,column=0,pady=5)
    Label(f1,text="Enter book id:",bg="black",fg="white",font="comicsanms 11",padx=10,pady=10).grid(row=3,column=1)
    book_id=Entry(f1)
    book_id.grid(row=3,column=2)
    Button(f1,text="Exit",font=("times 11 bold"),command=root2.destroy,padx=8).grid(row=6,column=2,padx=10,pady=10)
    Button(f1,text="Submit",font=("times 11 bold"),command=removebook).grid(row=5,column=2,padx=10,pady=10)

    root2.mainloop()

#bookremove()
