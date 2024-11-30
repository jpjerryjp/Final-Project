'''
Final Project
'''

import tkinter as tk
from tkinter import font


def ClearWindow(): 
    '''This function clears the window to open a new page'''
    for widget in window.winfo_children(): 
        #Destroy every thing in the window
        widget.destroy()
        

def WelcomePage():
    '''This function will initialize the first page that asks for the filepath'''
    #Make these global since we will need to access them outside the function
    global window, entWelcome
    
    #Intialize the window and allow user to adjust size
    window = tk.Tk()
    window.title("Search Text File")
    window.geometry()
    window.resizable(True, True) 
    
    #Frame to hold everything in
    frmWelcome = tk.Frame(window) 
    frmWelcome.pack(side="top", padx=20, pady=10)

    #This asks the user for the file location
    lblWelcome = tk.Label(frmWelcome, font=("Helvetica", 12, "bold"), text="Welcome, please type the file location (absolute file location):")
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
    
       
def GetFile():
    '''This function is called when the submit button on the first page is clicked '''
    #Set to global so we can acess later
    global fileLoc, fileContent
        
    #Get entry value which has the file location
    tempFileLoc = entWelcome.get()
    
    #Check that the user inserts valid file location
    #If user doesn't insert anything then do nothing
    if tempFileLoc == "":
        pass
    
    #If the user doesn't insert a / or \ then display error since it is not an absolute filepath
    elif (tempFileLoc.find("/") and tempFileLoc.find("\\")) == -1:
        entWelcome.delete(0, "end")
        entWelcome.insert(0, "Must be a valid file path")
    
    #If the user doesn't insert a . then display error since there is no extension
    elif tempFileLoc.find(".") == -1:
        entWelcome.delete(0, "end")
        entWelcome.insert(0, "Must have a file name extension")
        
    #If everything is good then do this
    else:    
        fileLoc = tempFileLoc
        #If it has \ instead of /, then fix it
        if fileLoc.find("\\") == -1:
            fileLoc = fileLoc.replace("\\", "/")
        #Remove " or ' since windows copies filepath with ""
        fileLoc = fileLoc.strip("'")
        fileLoc = fileLoc.strip('"')
                
        #Call function to get file data
        fileContent = LoadFile(fileLoc)
        #If no error then run FindPage()
        if fileContent != None:
            FindPage()
        

def LoadFile(file_path):
    '''This function tries to load the file and return the list of the file content'''
    #Try and except tries to read the file and if there is an error then it runs the except clause
    try:
        #Read the entire content of the file in read mode and store it in a list
        with open(file_path, 'r') as file: 
            content = file.readlines()  
        return content
    
    #If there is a problem opening the file, do display error message and return None
    except:   
        entWelcome.delete(0, "end")
        entWelcome.insert(0, "The file was not found. Please check the path and try again.")
        return None
    
     
def FindPage():
    '''This function will open the next page that searches the first word'''
    #Global since these will be accessed outside this function
    global frmSearchResults, entSearch, instance
    
    #Clear the window to display new window
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
    '''This function will be called when the search button is pressed'''
    #This function is here to intitalize the instance to 1 when the search button is pressed.
    #SetupSearch is its own function so that it can be called when the next or previous button is pressed and not 
    #Reset the instance to 1
    global instance
    instance = 1
    #Call function to set up search
    SetUpSearch()


def SetUpSearch():
    '''This function will be called after the search button is pressed and will initialize the screen to display results'''
    #Need to access these 
    global frmSearchResults, instance, totalInstance, instanceLocations
    #Get the word from search entry
    word = entSearch.get()
    #Get the total instances and their locations
    totalInstance, instanceLocations = count_word(word, fileContent)

    #This clears the search results frame everytime the user clicks the search button
    frmSearchResults.destroy()
    
    #Frame that holds all search result related info
    frmSearchResults = tk.Frame(window)
    frmSearchResults.pack(side="top")
    
    #This just displays the total number of instances
    lblSearchInstances = tk.Label(frmSearchResults, text=f"{totalInstance} instances found", font=("Helvetica", 12, "normal"))
    lblSearchInstances.pack(side="top", pady=10)
    
    #This displays which instance it is showing. If no instances, it shows "No matches found!"
    if totalInstance != 0:
        lblSearchResults = tk.Label(frmSearchResults, text=f"Instance {instance}:", font=("Helvetica", 12, "normal"))
        lblSearchResults.pack(side="top", pady=10)
    else:
        lblSearchResults = tk.Label(frmSearchResults, text=f"No matches found!", font=("Helvetica", 12, "normal"))
        lblSearchResults.pack(side="top", pady=10)
    
    #This shows multiple lines of text
    textSearchResults = tk.Text(frmSearchResults, height=10, width=80)
    textSearchResults.pack(side="top")

    #This is so that the text can be larger and set the searched word bold and underlined
    textSearchResults.tag_configure("underline", underline=True, font=("Helvetica", 12, "bold"))
    textSearchResults.tag_configure("normal", font=("Helvetica", 12, "normal"))
    
    #If ther is a result then get the info before and after the word to display
    if instance != 0:
        previous, word, next = GetSentenceWithWord(instance, instanceLocations, word, fileContent)

        #This is inserting the text with its format. The word is bolded and the rest is normal
        textSearchResults.insert("end", previous, "normal")
        textSearchResults.insert("end", word, "underline")
        textSearchResults.insert("end", next, "normal")

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
        
    
def count_word(word, fileContent):
    '''This function will count the total number of found words and return the locations in style [line, string index]'''
    #Set the word to lowercase. As of right now we do not do case sensitive. We also initialize everything 
    word = word.lower()
    totalInstances = 0
    instanceLocations = []

    #Loop through the lines in fileContent and count total instances and its location
    for lineIndex, line in enumerate(fileContent):
        #Lowercase the sentence too so that we can search for a match
        line = line.lower()
        #If the word is in this line
        if word in line:
            #Count the total number of times that the word appears in the line and add that to the total
            instances = line.count(word)
            totalInstances += instances
            
            #Find the location or starting index of each word in the line and add it to instanceLocations
            curIndex = line.find(word)
            instanceLocations.append([lineIndex, curIndex])
            if instances > 1:
                for instance in range(1,instances):
                    curIndex = line.find(word, curIndex+1)
                    instanceLocations.append([lineIndex, curIndex])
    
    return totalInstances, instanceLocations
          
          
def GetSentenceWithWord(instance, instanceLocations, inputword, fileContent):
    '''This function will get the previous line and data up to the word, and the data after the word and the next line.
    This is to display the word in a different style(underlined) with the rest of the line and previous and next line in another style.
    This function returns the previous line and data up to the word, the word, and the data after the word till the end of the next line.'''
    #Get the line and index of the desired word and initialize variables
    line, index = instanceLocations[instance-1] 
    prevLine = ""
    word = ""
    
    #If line is >= 1 then get the previous line
    if line > 0:
        prevLine = fileContent[line-1]
    #Add what is before the word but in the same line
    prevLine += fileContent[line][:index]
    #Add what is after the word but is in the same line
    nextLine = fileContent[line][index+len(inputword):]
    
    #If line is not at the end of the document then get the next line
    if line < len(fileContent)-1:
        nextLine += fileContent[line+1]
    #Get the word 
    word = fileContent[line][index:index+len(inputword)]
    return prevLine, word, nextLine 
        
           
def NextButton():
    '''This function will move to the next sentence with the instance'''
    global instance
    #Increment instances as long as it does not exceed the total. If it does then dont change.
    if instance <= totalInstance-1:
        instance += 1
    #Set up the search results window again with new data 
    SetUpSearch()


def PrevButton():
    '''This function will move to the previous sentence with the instance '''
    global instance
    #Decrement instances as long as it does not fall below 1. If it does then dont change.
    if instance >= 2:
        instance -= 1
    #Set up the search results window again with new data 
    SetUpSearch()

#Start by opening the welcome page
WelcomePage()
window.mainloop()