'''
Final Project
'''

import tkinter as tk
from tkinter import font

#This function clears the window to open a new page
def ClearWindow(): 
    for widget in window.winfo_children(): 
        widget.destroy()
        

#This function will initialize the first page that asks for the filepath
def WelcomePage():
    #Make these global since we will need to access them outside the function
    global window, entWelcome, fileLoc
    
    #Intialize the window and allow user to adjust size
    window = tk.Tk()
    window.title("Search Text File")
    window.geometry()
    window.resizable(True, True) 
    
    #Frame to hold everything in
    frmWelcome = tk.Frame(window) 
    frmWelcome.pack(side="top", padx=20, pady=10)

    #This asks the user for the file location
    lblWelcome = tk.Label(frmWelcome, font=("Helvetica", 12, "bold"), text="Welcome, please type the file location(absolute file location):")
    lblWelcome.pack(side="top", pady=10)
    
    #This is the entry to type into
    entWelcome = tk.Entry(frmWelcome, cursor="hand2", width=80)
    entWelcome.pack(side="top")
    
    #This creates a scrollbar for the entry window since it is a large file location usually
    h_scroll = tk.Scrollbar(frmWelcome, orient="horizontal", command=entWelcome.xview) 
    h_scroll.pack(fill="x")
    entWelcome.config(xscrollcommand=h_scroll.set)
    
    #Button to submit entry value. It calls GetFile() when clicked
    btnWelcome = tk.Button(frmWelcome, text="Submit", background="darkorange2", activebackground="blue2", 
                           command=GetFile, cursor="hand2")
    btnWelcome.pack(side="top", pady=20)
    
    fileLoc = ""
    
    
#This function is called when the submit button on the first page is clicked    
def GetFile():
    #Set to global so we can acess later
    global fileLoc, fileContent
        
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
        if fileLoc.find("\\") == -1:
            fileLoc = fileLoc.readlines("\\", "/")
        print(f"File location is: {fileLoc}")
        
        #Call function to get file data
        fileContent = load_file(fileLoc)
        FindPage()
        
        
def load_file(file_path):
    #Load the text file and return its content as a single string
    try:
        with open(file_path, 'r') as file:  # Open the file in read mode
            content = file.read()  # Read the entire content of the file
        return content
    except FileNotFoundError:
        print("The file was not found. Please check the path and try again.")
        return None
    
     
#This function will open the next page that searches the first word
def FindPage():
    global frmSearchResults, entSearch
    
    ClearWindow()
    
    #This is a frame for the search section
    frmSearch = tk.Frame(window)
    frmSearch.pack(side=("top"), pady=20)
    
    #This asks the user for the word to search
    lblSearch = tk.Label(frmSearch, text="Search for:", font=("Helvetica", 12, "normal"))
    lblSearch.pack(side="left")
    
    #This is the entry to type the search word into
    entSearch = tk.Entry(frmSearch, cursor="hand2", width=20)
    entSearch.pack(side="left", padx=10)
    
    #Button to submit search word. It calls Search() when clicked
    btnSearch = tk.Button(frmSearch, text="Search", background="darkorange2", activebackground="blue2", 
                           command=Search, cursor="hand2")
    btnSearch.pack(side="left", padx=10)
    
    #This is just here to initialize it so that ther is no error clearning it when Search is called
    frmSearchResults = tk.Frame(window)
    
    
def Search():
    global frmSearchResults
    
    instances = count_word(entSearch.get(), fileContent)
    
    #This clears the search results frame everytime the user clicks the search button
    frmSearchResults.destroy()
    
    #Frame that holds all search result related info
    frmSearchResults = tk.Frame(window)
    frmSearchResults.pack(side="top")
    
    #This just displays the total number of instances
    lblSearchInstances = tk.Label(frmSearchResults, text=f"{instances} instances found", font=("Helvetica", 12, "normal"))
    lblSearchInstances.pack(side="top", pady=10)
    
    #This displays which instance it is showing
    lblSearchResults = tk.Label(frmSearchResults, text=f"Instance {1}:", font=("Helvetica", 12, "normal"))
    lblSearchResults.pack(side="top", pady=10)
    
    #This shows multiple lines of text
    textSearchResults = tk.Text(frmSearchResults, height=10, width=80)
    textSearchResults.pack(side="top")

    #This is so that the text can be larger and set the searched word bold and underlined
    textSearchResults.tag_configure("underline", underline=True, font=("Helvetica", 12, "bold"))
    textSearchResults.tag_configure("normal", font=("Helvetica", 12, "normal"))
    
    '''Function to get sentence before and after word'''
    
    Text2 = "To add another binding to an existing "
    Word = "tag"
    Text3 = ", pass the same first three arguments and '+' as the fourth argument."

    #This is inserting the text with its format
    textSearchResults.insert("end", Text2, "normal")
    textSearchResults.insert("end", Word, "underline")
    textSearchResults.insert("end", Text3, "normal")

    #This makese it so the user cannot edit the text in the textbox
    textSearchResults["state"] = "disabled"
    
    #This frame holds the next and previous buttons
    frmNPButtons = tk.Frame(frmSearchResults)
    frmNPButtons.pack(side="top", fill="x", pady=20)
    
    #This button calls the function NextButton() when clicked
    btnNext = tk.Button(frmNPButtons, text="Next", background="darkorange2", activebackground="blue2", 
                        command=NextButton, cursor="hand2")
    btnNext.pack(side="right", padx=30)
    
    #This button calls the function PrevButton() when clicked
    btnPrev = tk.Button(frmNPButtons, text="Previous", background="darkorange2", activebackground="blue2", 
                        command=PrevButton, cursor="hand2")
    btnPrev.pack(side="left", padx=30)
        
    
def count_word(word, text):
    """Count the number of times a word appears in the text, ignoring punctuation."""
    # Define a set of common punctuation characters to remove
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    # Normalize the word to lowercase for case-insensitive comparison
    word = word.lower()

    # Remove punctuation from the text
    cleaned_text = ''.join(char if char not in punctuation else ' ' for char in text).lower()

    # Split the cleaned text into words and count matches
    words = cleaned_text.split()
    count = words.count(word)
    
    return count
          
           
#This function will move to the next sentence with the instance 
def NextButton():
    pass


#This function will move to the previous sentence with the instance 
def PrevButton():
    pass


WelcomePage()
window.mainloop()