import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from functools import partial
from tkinter import scrolledtext

# Global variable to hold sql select statements for refreshResults()
prevSqlSelect = ""

def main():
    window = tk.Tk()
    window.title("Book Inventory")
    window.geometry("1050x600")
    window.configure(bg='white')

    # Labels and entry for Creating a book in inventory 
    lblCreate = tk.Label(window,text="Create", bg="grey", font=("Arial Bold", 15))
    lblCreate.grid(column=0, row=0,sticky = "we",columnspan=10,pady=20)

    lalBookTitle = tk.Label(text="Title of book", bg ="white")
    lalBookTitle.grid(column=0,row=1,sticky = "W",padx=3, pady = 2)
    bookTitle =tk.StringVar()  
    bookTitleEntry = tk.Entry(window,textvariable=bookTitle, bg="lightblue" )
    bookTitleEntry.grid(column=1, row=1)

    lalAuthorName = tk.Label(text="Author", bg ="white")
    lalAuthorName.grid(column=0,row=2,sticky = "W",padx=3, pady = 2)
    authorName =tk.StringVar()  
    authorNameEntry = tk.Entry(window, textvariable=authorName,bg="lightblue")
    authorNameEntry.grid(column=1, row=2)

    lalGenre = tk.Label(text="Genre", bg ="white")
    lalGenre.grid(column=0,row=3,sticky = "W",padx=3, pady = 2)
    genre=tk.StringVar()  
    genreEntry = tk.Entry(window,textvariable=genre,bg="lightblue")
    genreEntry.grid(column=1, row=3)

    lalPPU = tk.Label(text="Price per unit", bg ="white")
    lalPPU.grid(column=0,row=4,sticky = "W",padx=3, pady = 2)
    pricePerUnit =tk.IntVar()  
    ppuEntry = tk.Entry(window,textvariable=pricePerUnit,bg="lightblue")
    ppuEntry.grid(column=1, row=4)

    lalQuantity = tk.Label(text="Quantity", bg ="white")
    lalQuantity.grid(column=0,row=5, sticky = "W",padx=3, pady = 2)
    quantity =tk.IntVar() 
    quantityEntry = tk.Entry(window, textvariable=quantity,bg="lightblue")
    quantityEntry.grid(column=1, row=5)   

    # Label for searching book in inventory
    lblSearch = tk.Label(window,text="Search", bg="grey", font=("Arial Bold", 15))
    lblSearch.grid(column=0, row=8,sticky = "we",columnspan=10,pady=20)

    lalSearch = tk.Label(text="Input", bg ="white")
    lalSearch.grid(column=0,row=11, pady = 2, sticky = "W")

    search =tk.StringVar() 
    searchEntry = tk.Entry( window, width=20, textvariable=search, bg="lightblue")
    searchEntry.grid(column=1, row=11, pady = 2, sticky = "W")

    # Label for showing results in search
    lblResults = tk.Label(window,text="Results", bg="grey", font=("Arial Bold", 15))
    lblResults.grid(column=0, row=14, sticky = "we", columnspan=10, pady=15)

    lal_ID = tk.Label(text="ID number", bg ="white")
    lal_ID.grid(column=0, row=15, pady=2, sticky = "W")

    lal_bookTitle = tk.Label(text="Book Title",  bg ="white")
    lal_bookTitle.grid(column=1,row=15,pady=2, sticky = "W")

    lal_author = tk.Label(text="Author",  bg ="white")
    lal_author.grid(column=2,row=15,pady=2, sticky = "W")

    lal_bookGenre = tk.Label(text="Genre",  bg ="white")
    lal_bookGenre.grid(column=3,row=15,pady=2, sticky = "W")

    lal_bookPrice = tk.Label(text="Price",  bg ="white")
    lal_bookPrice.grid(column=4,row=15,pady=2,sticky = "W")

    lal_bookQuantity = tk.Label(text="Quantity",  bg ="white")
    lal_bookQuantity.grid(column=5,row=15,pady=2,sticky = "W")

    # Functions for program
    def addToDB():
        bt = bookTitle.get()
        an = authorName.get()
        gen = genre.get()
        ppu = pricePerUnit.get()
        qtt = quantity.get()
        mydb = getConnection()
        mycursor = mydb.cursor()

        #search to see if book already exists
        sql = "SELECT * FROM book WHERE BookTitle = %s AND BookAuthor = %s "
        values = (bt, an,)
        mycursor.execute(sql, values)
        res = mycursor.fetchall()

        #if book exists overwrite       
        if len(res) > 0:
            ID = res[0][0]
            sql = "UPDATE book SET BookTitle = %s, BookAuthor = %s, BookGenre = %s, BookPrice = %s, BookQuantity = %s WHERE IDnumber = %s" 
            values= (bt, an, gen, ppu, qtt, ID,)
            MsgBox = tk.messagebox.askquestion ('Book Exists','This book is already in inventory, do you want to overwrite it?',icon = 'warning')
            if MsgBox == 'yes':
                clearEntry()
            else:
                tk.messagebox.showinfo('Return','You will now return to the application screen.')
                return

        #add to DB
        else:            
            sql = "INSERT INTO BOOK (BookTitle, BookAuthor,BookGenre,BookPrice,BookQuantity) VALUES (%s, %s,%s, %s, %s)"
            values=(bt, an, gen, ppu, qtt)

        mycursor.execute(sql,values)
        mydb.commit()
        mydb.close()
        clearEntry()
    
    def getConnection():
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="Kelsy",
        passwd="batman",
        database="KLW_BOOK_INFO",
        auth_plugin="mysql_native_password"
        )
        return mydb

    # Clear entry on book submit
    def clearEntry():
        bookTitleEntry.delete(first=0, last=100)
        authorNameEntry.delete(first=0, last=100)
        genreEntry.delete(first=0, last=100)
        ppuEntry.delete(first=0, last=100)
        ppuEntry.insert(INSERT, 0)
        quantityEntry.delete(first=0, last=100)
        quantityEntry.insert(INSERT, 0)

    def askClear():
        MsgBox = tk.messagebox.askquestion ('Clear Book','Are you sure you want clear this book information?',icon = 'warning')
        if MsgBox == 'yes':
            clearEntry()
        else:
            tk.messagebox.showinfo('Return','You will now return to the application screen.')

    # Removes previously printed results 
    def clearResults():
        children = window.winfo_children()
        i = 0
        
        while i < len(children):
            if i > 27:  #number of children that exists on page before printing results including 0
                children[i].destroy()
            i += 1


    def searchByGenre():
        global prevSqlSelect

        mydb = getConnection()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM book WHERE BookGenre = %s"
        vals = (search.get(),)
        mycursor.execute(sql, vals)
        prevSqlSelect = mycursor.statement  # Assign select statement for refreshResults func
        myresult = mycursor.fetchall()
        printResults(myresult)

    def searchByID():
        global prevSqlSelect

        mydb = getConnection()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM book WHERE IDnumber = %s"
        vals = (search.get(),)
        mycursor.execute(sql, vals)
        prevSqlSelect = mycursor.statement # Assign select statement for refreshResults func
        myresult = mycursor.fetchall()
        printResults(myresult)

    def searchByTitle():
        global prevSqlSelect

        mydb = getConnection()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM book WHERE BookTitle = %s"
        vals = (search.get(),)
        mycursor.execute(sql, vals)
        prevSqlSelect = mycursor.statement # Assign select statement for refreshResults func
        myresult = mycursor.fetchall()
        printResults(myresult)  

    def searchByAuthor():
        global prevSqlSelect

        mydb = getConnection()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM book WHERE BookAuthor = %s"
        vals = (search.get(),)
        mycursor.execute(sql, vals)
        prevSqlSelect = mycursor.statement # Assign select statement for refreshResults func
        myresult = mycursor.fetchall()
        printResults(myresult)

    def showAllBooks():
        global prevSqlSelect

        mydb = getConnection()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM book"
        mycursor.execute(sql)
        prevSqlSelect = mycursor.statement # Assign select statement for refreshResults func
        myresult = mycursor.fetchall()
        printResults(myresult)
    
    def printResults(myresult):
        clearResults()

        # If no results display 'no results' and return 
        if len(myresult) == 0:
            emptyspace = tk.Label(window, width=20, text="No Results", bg ="white")
            emptyspace.grid(column=0, row=16, pady = 2, sticky = "W")
            return    

        # Creat frame and canvas for scrolling area
        frame2 = tk.Frame()
        frame2.grid(row=16, column=0, columnspan=7, sticky=NW)
        canvas = tk.Canvas(frame2, bg="white")
        canvas.grid(row=0, column=0)

        vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
        vsbar.grid(row=0, column=1, sticky=NS)
        canvas.configure(yscrollcommand=vsbar.set)

        data_frame = tk.Frame(canvas, bg="white", bd=2)

        # Loop over results and append data to data_frame
        i = 0
        while i < len(myresult):
            view_ID = tk.Label(data_frame, width=20, text=myresult[i][0], bg="lightblue")
            view_ID.grid(column=0, row=i, pady = 2, sticky = "W")

            results_bookTitle =tk.StringVar()  
            view_bookTitle = tk.Entry(data_frame, width=30, textvariable=results_bookTitle,bg="lightblue")
            view_bookTitle.grid(column=1, row=i, pady = 2, sticky = "W")
            view_bookTitle.insert(INSERT, myresult[i][1])

            results_author =tk.StringVar()  
            view_author = tk.Entry(data_frame, width=20, textvariable=results_author,bg="lightblue")
            view_author.grid(column=2, row=i, pady = 2, sticky = "W")
            view_author.insert(END, myresult[i][2])

            results_genre =tk.StringVar()  
            view_genre = tk.Entry(data_frame, width=20, textvariable=results_genre,bg="lightblue")
            view_genre.grid(column=3, row=i, pady = 2, sticky = "W")
            view_genre.insert(END, myresult[i][3])

            results_bookPrice =tk.IntVar()  
            view_bookPrice = tk.Entry(data_frame, width=20, textvariable=results_bookPrice,bg="lightblue")
            view_bookPrice.grid(column=4, row=i, pady = 2, sticky = "W")
            view_bookPrice.delete(ANCHOR)
            view_bookPrice.insert(END, myresult[i][4])

            results_bookQuantity =tk.IntVar()  
            view_bookQuantity = tk.Entry(data_frame, width=20, textvariable=results_bookQuantity,bg="lightblue")
            view_bookQuantity.grid(column=5, row=i, pady = 2, sticky = "W")
            view_bookQuantity.delete(ANCHOR)
            view_bookQuantity.insert(END, myresult[i][5])

            # Button for editing book 
            btn8 = tk.Button(data_frame, text="Edit", cursor="hand2",activebackground="green",command=partial(edit,myresult[i][0],results_bookTitle,results_author,results_genre,results_bookPrice,results_bookQuantity))
            btn8.grid(column=7, row=i,padx = 10, pady=10)

            # Button for deleting book
            btn9 = tk.Button(data_frame, text="Delete", cursor="hand2",activebackground="red",command= partial(delete,myresult[i][0])) 
            btn9.grid(column=8, row=i, padx = 10, pady=10)

            i += 1

        # Create canvas window to hold the data_frame.
        canvas.create_window((0,0), window=data_frame, anchor=NW)
        data_frame.update_idletasks()  
        bbox = canvas.bbox(tk.ALL) 

        rows = 3  # Number of rows to display.
        cols = 7  # Number of columns to display.

        # Define the scrollable region as entire canvas with only the desired number of rows and columns displayed.
        width, height = bbox[2]-bbox[1], bbox[3]-bbox[1]
        scrollw, scrollh = int((width/7) * cols), int((height/i) * rows)
        canvas.configure(scrollregion=bbox, width=scrollw, height=scrollh)

    # Update printed results after editing or deleting
    def refreshResults():
        mydb = getConnection()
        mycursor = mydb.cursor()
        mycursor.execute(prevSqlSelect)
        myresult = mycursor.fetchall()
        printResults(myresult)

    # Edit Results
    def edit(ID,title,author,genre,price,quantity):
        title = title.get()
        author = author.get()
        genre = genre.get()
        price = price.get()
        quantity = quantity.get()

        MsgBox = tk.messagebox.askquestion ('Edit Book','Are you sure you want update this book?', icon = 'warning')
        if MsgBox == 'yes':
            mydb = getConnection()
            mycursor = mydb.cursor()
            sql = "UPDATE book SET BookTitle = %s, BookAuthor = %s, BookGenre = %s, BookPrice = %s, BookQuantity = %s WHERE IDnumber = %s" 
            vals= (title, author, genre, price, quantity, ID,)
            mycursor.execute(sql,vals)
            mydb.commit()
            mydb.close()
            refreshResults()
        else:
            tk.messagebox.showinfo('Return','You will now return to the application screen.')

    # Delete result from database        
    def delete(idNum):
        MsgBox = tk.messagebox.askquestion ('Delete Book','Are you sure you want delete this book?', icon = 'warning')
        if MsgBox == 'yes':
            mydb = getConnection()
            mycursor = mydb.cursor()
            sql = "DELETE FROM book WHERE IDnumber = %s"
            val = (idNum,)
            mycursor.execute(sql, val)
            mydb.commit()
            mydb.close()
            refreshResults()
            
        else:
            tk.messagebox.showinfo('Return','You will now return to the application screen.')
        
    # Submit to database button
    btn1 = tk.Button(window, text="Submit to Inventory", cursor="hand2", activebackground="green",command=addToDB)
    btn1.grid(column=0, row=7,pady=10)

    # Clear entry button
    btn2 = tk.Button(window, text="Clear Entry", cursor="hand2", activebackground="red",command=askClear)
    btn2.grid(column=1, row=7,pady=10)
    
    #Buttons for search entry
    btn3 = tk.Button(window, text="Search by genre", cursor="hand2", activebackground="green",command=searchByGenre)
    btn3.grid(column=0, row=12, pady=10)

    btn4 = tk.Button(window, text="Search by ID #", cursor="hand2",activebackground="green",command=searchByID)
    btn4.grid(column=1, row=12, pady=10)

    btn5 = tk.Button(window, text="Search by Title", cursor="hand2",activebackground="green",command=searchByTitle)
    btn5.grid(column=2, row=12, pady=10)

    btn6 = tk.Button(window, text="Search by Author",cursor="hand2", activebackground="green",command=searchByAuthor)
    btn6.grid(column=3, row=12, pady=10)

    btn7 = tk.Button(window, text="Show all books", cursor="hand2",activebackground="green",command=showAllBooks)
    btn7.grid(column=4, row=12, pady=10)

    window.mainloop()

main()
