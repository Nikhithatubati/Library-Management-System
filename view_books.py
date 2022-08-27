from tkinter import *

def viewbooks():
    global root4

    root4=Tk()
    root4.geometry("700x780")
    root4.minsize(700,780)
    root4.title("View Books")
    root4.configure(bg="#E6E6FA")
    heading=Label(root4,text="BOOKS DETAILS",bg='black',fg="yellow",font="gotham 20 bold",borderwidth=10,relief=SUNKEN,padx=10,pady=4)
    heading.pack(pady=0,fill=X)

    main_frame=Frame(root4,height=700,width=780,borderwidth=0,relief=RIDGE,bg="#E6E6FA",padx=8)
    main_frame.pack(side=LEFT,anchor="nw",fill=X and Y)
    
    Label(main_frame,text="book id : {book details}", font="cambria 13 bold",pady=5,bg="#E6E6FA").pack(anchor="nw")
    with open("books.txt", "r") as f:
        data=f.read()
        data=data.split('\n')
        for i in data:
            Label(main_frame,text=f"{i}",font="times 12",bg="#E6E6FA").pack(anchor="nw")




    root4.mainloop()

#viewbooks()
