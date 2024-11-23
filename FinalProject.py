'''
Final Project
'''

import tkinter as tk
from tkinter import font

def InitializeWelcome():
    #Create window, label it, and set dimentions
    global window, entWelcome, fileLoc
    
    window = tk.Tk()
    window.title('Search Text File')
    window.geometry('500x500')
    window.resizable(True, True) 

    fntWelcome = font.Font(family="Helvetica", size=12, weight="bold")

    lblWelcome = tk.Label(window, font=fntWelcome, text='Welcome, please type the \nfile location(absolute file location):')
    lblWelcome.pack(side="top")
    
    entWelcome = tk.Entry(window, cursor="hand2")
    entWelcome.pack(side="top")
    
    # btnWelcome = tk.Button(window, text = "Buttons", bg='white', padx=5, pady=5)
    btnWelcome = tk.Button(window, text='Submit', background="darkorange2", activebackground="blue2", command=EnteredFileLoc, cursor="hand2")
    btnWelcome.pack(side="top")
    
    fileLoc = ""
    
def EnteredFileLoc():
    global fileLoc
        
    tempFileLoc = entWelcome.get()
    if tempFileLoc and tempFileLoc.find("/") != -1:
        fileLoc = tempFileLoc
    else:
        entWelcome.delete(0, "end")
        entWelcome.insert(0, "Invalid Input")
        
    print(f"File location is: {fileLoc}")
    #need to make user feedback more accurate
    


InitializeWelcome()

window.mainloop()