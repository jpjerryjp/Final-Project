'''
Final Project
'''

import tkinter as tk
from tkinter import font

def ClearWindow(): 
    for widget in window.winfo_children(): 
        widget.destroy()

#This function will initialize the first page that asks for the filepath
def WelcomePage():
    #Make these global since we will need to access them outside the function
    global window, entWelcome, fileLoc
    
    #Intialize the window and allow user to adjust size
    window = tk.Tk()
    window.title('Search Text File')
    window.geometry()
    window.resizable(True, True) 
    
    #Frame to hold everything in
    frmWelcome = tk.Frame(window) 
    frmWelcome.pack(side="top", padx=20, pady=10)

    #This asks the user for the file location
    lblWelcome = tk.Label(frmWelcome, font=("Helvetica", 12, "normal"), text='Welcome, please type the file location(absolute file location):')
    lblWelcome.config(font=("Helvetica", 12, "bold"))
    lblWelcome.pack(side="top", pady=10)
    
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
    btnWelcome.pack(side="top", pady=20)
    
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
        #Call function to get file data
        FindPage()
        
#This function will open the next page that 
def FindPage():
    ClearWindow()
    
    frmSearch = tk.Frame(window)
    frmSearch.pack(side=("top"), pady=20)
    
    #This asks the user for the file location
    # lblWelcome = tk.Label(frmSearch, font=fntWelcome, text='Welcome, please type the file location(absolute file location):')
    # lblWelcome.config(font=("Helvetica", 12, "bold"))
    lblWelcome = tk.Label(frmSearch, text='Search for:', font=("Helvetica", 12, "normal"))
    lblWelcome.pack(side="left")
    
    #This is the entry to type into
    entWelcome = tk.Entry(frmSearch, cursor="hand2", width=20)
    entWelcome.pack(side="left", padx=10)
    
    #Button to submit entry value. It calls GetFile() when clicked
    btnWelcome = tk.Button(frmSearch, text='Search', background="darkorange2", activebackground="blue2", 
                           command=Search, cursor="hand2")
    btnWelcome.pack(side="left", padx=10)
    
def Search():
    #Search function here
    
    frmSearchResults = tk.Frame(window)
    frmSearchResults.pack(side=("top"), pady=20)
    
    lblWelcome = tk.Label(frmSearchResults, text='XX instances found', font=("Helvetica", 12, "normal"))
    lblWelcome.pack(side="top", pady=10)
    
    lblWelcome = tk.Label(frmSearchResults, text='Instance X:', font=("Helvetica", 12, "normal"))
    lblWelcome.pack(side="top", pady=10)

    
        

WelcomePage()

window.mainloop()
#C:\Users\jerry\OneDrive\CGN3421-Computer Methods in Civil Engineering\L16 Variable Passing and Scope.pdf