#importing modules
from textblob import TextBlob
from tkinter import *

# Function to check the spelling
def checkSpelling():
    a = text.get()  # Getting the text from the user input
    b = TextBlob(a)  # Passing the text to TextBlob for correction
    correctedText.set("The Corrected Text is: " + str(b.correct()))  # Displaying the corrected text

# Creating the window
wn = Tk()
wn.title('Spell Checker')
wn.geometry('600x400')
wn.config(bg='SlateGray1')

# Input Label
Label(wn, text="Enter Text:", font=('Arial', 14), bg='SlateGray1').pack(pady=10)

# Entry widget for user to enter text
text = Entry(wn, width=50, font=('Arial', 14))
text.pack(pady=10)

# StringVar to hold the corrected text
correctedText = StringVar()

# Label to display the corrected text
Label(wn, textvariable=correctedText, font=('Arial', 14), bg='SlateGray1').pack(pady=20)

# Button to trigger the spell checking
Button(wn, text='Check Spelling', command=checkSpelling, font=('Arial', 14), bg='lightblue').pack(pady=20)

# Run the application
wn.mainloop()
