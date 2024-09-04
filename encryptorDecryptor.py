from tkinter import *
import base64

#initialize window  
root = Tk()
root.geometry('1100x1100')
root.resizable(0,0)

#title of the window
root.title("My- Message Encode and Decode") 

#label
Label(root, text ='ENCRYPT DECRYPT', font = 'arial 20 bold').pack()
Label(root, text ='DataFlair', font = 'arial 20 bold').pack(side = BOTTOM)

#define variables
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

#function to encode
def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#function to decode
def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)

#function to set mode
def Mode():
    if mode.get() == 'e':
        Result.set(Encode(private_key.get(), Text.get()))
    elif mode.get() == 'd':
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

#function to exit
def Exit():
    root.destroy()

#function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

#message
Label(root, font = 'arial 12 bold', text ='MESSAGE').pack()
Entry(root, font = 'arial 10', textvariable = Text).pack()
Label(root, font = 'arial 12 bold', text ='KEY').pack()
Entry(root, font = 'arial 10', textvariable = private_key).pack()
Label(root, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').pack()
Entry(root, font = 'arial 10', textvariable = mode).pack()
Button(root, font = 'arial 10 bold', text = 'RESULT', command = Mode).pack()
Entry(root, font = 'arial 10', textvariable = Result).pack()

#result
Result.set('')
#reset button
Button(root, font = 'arial 10 bold', text = 'RESET', command = Reset).pack()
Button(root, font = 'arial 10 bold', text = 'EXIT', command = Exit).pack()

root.mainloop()
#end of the code