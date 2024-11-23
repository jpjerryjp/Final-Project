'''
Final Project
'''

import tkinter as tk
from tkinter import font

#This function will initialize the first page that asks for the filepath
def InitializeWelcome():
    #Make these global since we will need to access them outside the function
    global window, entWelcome, fileLoc
    
    #Intialize the window and allow user to adjust size
    window = tk.Tk()
    window.title('Search Text File')
    window.geometry()
    window.resizable(True, True) 

    #Font for the text
    fntWelcome = font.Font(family="Helvetica", size=12, weight="bold")
    
    #Frame to hold everything in
    frmWelcome = tk.Frame(window, padx=40, pady=40) 
    frmWelcome.pack(side="top")

    #This asks the user for the file location
    lblWelcome = tk.Label(frmWelcome, font=fntWelcome, text='Welcome, please type the file location(absolute file location):')
    lblWelcome.pack(side="top")
    
    #This is the entry to type into
    entWelcome = tk.Entry(frmWelcome, cursor="hand2", width=60)
    entWelcome.pack(side="top")
    
    #This creates a scrollbar for the entry window since it is a large file location usually
    h_scroll = tk.Scrollbar(frmWelcome, orient='horizontal', command=entWelcome.xview) 
    h_scroll.pack(fill="x")
    entWelcome.config(xscrollcommand=h_scroll.set)
    
    #Button to submit entry value. It calls GetFile() when clicked
    btnWelcome = tk.Button(frmWelcome, text='Submit', background="darkorange2", activebackground="blue2", 
                           command=GetFile, cursor="hand2")
    btnWelcome.pack(side="top")
    
    fileLoc = ""
    
    
#This function is called when the submit button on the first page is clicked    
def GetFile():
    #Set to global so we can acess later
    global fileLoc
        
    #Get entry value
    tempFileLoc = entWelcome.get()
    
    #Check that the user inserts valid file location
    if tempFileLoc == "":
        pass
    
    elif (tempFileLoc.find("/") and tempFileLoc.find("\\")) == -1:
        entWelcome.delete(0, "end")
        entWelcome.insert(0, "Must be a valid file path")
    
    elif tempFileLoc.find(".") == -1:
        entWelcome.delete(0, "end")
        entWelcome.insert(0, "Must have a file name extension")
        
    elif (tempFileLoc.find('"') and tempFileLoc.find("'")) != -1:
        entWelcome.delete(0, "end")
        entWelcome.insert(0, "Cannot have \"\" or ''")
        
    else:    
        fileLoc = tempFileLoc
        print(f"File location is: {fileLoc}")
    

InitializeWelcome()

window.mainloop()