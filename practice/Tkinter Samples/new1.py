from tkinter import *

window = Tk()
window.title("First GUI")
window.minsize(width=500,height=500)

#label

label = Label(text="I am a Label",font=("Arial",24))
label.pack()

label["text"] = "new Text"
label.config(text="new text")

def button_clicked():
    print("I got Clicked")
    new_text = input.get()
    label.config(text=new_text)


button = Button(text="Click Me",command=button_clicked)
button.pack()


#Entry component

input = Entry(width=40)
input.pack()



window.mainloop()