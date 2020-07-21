from tkinter import *

root = Tk()
root.geometry("1000x650")
# root.attributes("-fullscreen", True)

e = Entry(root)
e.pack()

def add_yeet(event):
    new_yeet = Label(root, text="Yeet") 
    new_yeet.pack()

def myClick():
    myLabel = Label(root, text="Look! I clicked the button!!!!!!!")
    myLabel.pack()
    print(e.get())

label = Label(root, text="Add Yeet")
label.bind("<Button-1>", add_yeet)
label.pack()


myButton = Button(root, text="Click Me", command=myClick)
myButton.pack()

root.mainloop()