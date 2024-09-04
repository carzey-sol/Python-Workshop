from numpy import size
import qrcode
from tkinter import *
from tkinter import messagebox

#Creating the window
wn = Tk()
wn.title('My QR Code Generator')
wn.geometry('700x700')
wn.config(bg='SteelBlue3')


#Func to generate the Qr code and save it
def generateCode():
    #Creating a QRCode object of the size specified
    qr = qrcode.QRCode(version = size.get(), box_size = 10, border = 5)
    qr.add_data(text.get()) #Adding the data to be encoded to the QRCode object
    qr.make(fit=True) #making the entire QR code space
    img = qr.make_image()
    fileDirec = loc.get() + '\\' + name.get() #Getting the directory where the file is to be stored
    img.save(f'{fileDirec}.png') #Saving the QR
    #pop up message
    messagebox.showinfo("QR Code","QR Code is successfully saved")

#Label for the window

headingFrame = Frame(wn,bg="azure",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="Generate QR Code with DataFlair",bg='azure', font=('Times New Roman',20,'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1,relheight=1)

#Taking the input from the user to get QR code
Frame1 = Frame(wn,bg='SteelBlue3',bd=5)
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)

label1 = Label(Frame1,text='Enter the text/URL:',bg='SteelBlue3',fg='azure',font=('Times New Roman',15))
label1.place(relx=0.05,rely=0.2,relheight=0.08)

text = Entry(Frame1,font=('Century 12'))
text.place(relx=0.05,rely=0.4,relwidth=1,relheight=0.2)

#Getting the input to save the QR code
Frame2 = Frame(wn,bg='SteelBlue3',bd=5)
Frame2.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)  

label2 = Label(Frame2,text='Enter the location to save the QR:',bg='SteelBlue3',fg='azure',font=('Times New Roman',15))
label2.place(relx=0.05,rely=0.2,relheight=0.08)

loc = Entry(Frame2,font=('Century 12'))
loc.place(relx=0.05,rely=0.4,relwidth=1,relheight=0.2)

#Getting the input of the QR code image name
Frame3 = Frame(wn,bg='SteelBlue3',bd=5)
Frame3.place(relx=0.1,rely=0.55,relwidth=0.7,relheight=0.3)

label3 = Label(Frame3,text='Enter the name of the QR code:',bg='SteelBlue3',fg='azure',font=('Times New Roman',15))
label3.place(relx=0.05,rely=0.2,relheight=0.08)

name = Entry(Frame3,font=('Century 12'))
name.place(relx=0.05,rely=0.4,relwidth=1,relheight=0.2)

#Getting the input of the size of the QR code
Frame4 = Frame(wn,bg='SteelBlue3',bd=5)
Frame4.place(relx=0.1,rely=0.7,relwidth=0.7,relheight=0.3)

label4 = Label(Frame4,text='Enter the size of the QR code:',bg='SteelBlue3',fg='azure',font=('Times New Roman',15))
label4.place(relx=0.05,rely=0.2,relheight=0.08)

size = Entry(Frame4,font=('Century 12'))
size.place(relx=0.05,rely=0.4,relwidth=1,relheight=0.2)

#Button to generate the QR code
generate = Button(wn,text='Generate QR Code',font=('Century 12'),command=generateCode)
generate.place(relx=0.3,rely=0.85,relwidth=0.4,relheight=0.1)

wn.mainloop()


#getting input of the QR Code image name
Frame3 = Frame(wn,bg='SteelBlue3',bd=5)
Frame3.place(relx=0.1,rely=0.55,relwidth=0.7,relheight=0.3)