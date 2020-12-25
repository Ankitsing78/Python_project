from tkinter import *

root = Tk() #Makes the window
root.wm_title("Voice") #Makes the title that will appear in the top left
root.config(background = "#bdb7b7")


def fun1():
          
    entry.insert(0.0, "You click Fun1\n")

def fun2():

    entry.insert(0.0, "You click Fun2\n")

def fun3():
    
    entry.insert(0.0, "You click Fun3\n")


#Left Frame and its contents
leftFrame = Frame(root, width=200, height = 600)
leftFrame.grid(row=0, column=0, padx=20, pady=5)

Label(leftFrame, text="Instructions:").grid(row=0, column=0, padx=10, pady=2)

Instruct = Button(leftFrame,text="New Record")
Instruc = Button(leftFrame,text="Save").grid(row=2,column=0,padx=10,pady=2)
Instru = Button(leftFrame,text="Reset").grid(row=3,column=0,padx=10,pady=2)
Instr = Button(leftFrame,text="Help").grid(row=4,column=0,padx=10,pady=2)
Inst = Button(leftFrame,text="Credits").grid(row=5,column=0,padx=10,pady=2)
Instruct.grid(row=1, column=0, padx=10, pady=2)

try:
    imageEx = PhotoImage(file = 'pic1.png')
    Label(leftFrame, image=imageEx).grid(row=6, column=0, padx=10, pady=2)
except:
    print("Image not found")

#Right Frame and its contents
rightFrame = Frame(root, width=600, height = 400)
rightFrame.grid(row=0, column=1, padx=10, pady=2)

RecordCanvas = Canvas(rightFrame, width=400, height=100, bg='#3c6e85')
RecordCanvas.grid(row=0, column=0, padx=10, pady=2)

btnFrame = Frame(rightFrame, width=200, height = 200)
btnFrame.grid(row=1, column=0, padx=10, pady=2)

entry= Text(rightFrame, width = 30, height = 10, takefocus=0)
entry.grid(row=2, column=0, padx=10, pady=2)

Btn1 = Button(btnFrame, text="Language", command=fun1)
Btn1.grid(row=0, column=0, padx=10, pady=2)

Btn2 = Button(btnFrame, text="VoiceAI", command=fun2)
Btn2.grid(row=0, column=1, padx=10, pady=2)

Btn3 = Button(btnFrame, text="ETC", command=fun3)
Btn3.grid(row=0, column=2, padx=10, pady=2)


root.mainloop()
