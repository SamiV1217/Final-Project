from tkinter import *
from tkinter import ttk
from displayFunctions import *
from insertFunctions import *
from removingBook import *
from updateBookPrice import *

#the main menu
def main():
    root = Tk()
    root.title("Main Menu")
    root.geometry("200x140")
    frame = ttk.Frame(root, padding="10 10 10 10")
    frame.pack(fill=tk.BOTH, expand=True)
    
    button1 = Button(frame, width= 15, text="Display Books", command=lambda:displayFunctions.display(root))
    button1.pack()
    button2 = Button(frame, width= 15, text="Insert Book", fg='green', command=lambda:insertFunctions.inserting(root))
    button2.pack()
    button3 = Button(frame, width= 15, text="Update a Book", fg='blue',command=lambda:updateBookPrice.updateBook(root))
    button3.pack()
    button4 = Button(frame, width= 15, text="Remove a Book", fg='red', command=lambda:removingBook.deleteBook(root))
    button4.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
