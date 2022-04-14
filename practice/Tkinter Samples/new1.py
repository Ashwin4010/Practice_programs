import tkinter

window = tkinter.Tk()
window.title("First GUI")
window.minsize(width=500,height=500)

#label

label = tkinter.Label(text="I am a Label",font=("Arial",24))
label.pack(expand=True)


window.mainloop()