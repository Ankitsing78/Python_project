from tkinter import *
root=Tk()
root.geometry("{0}x{1}".format((root.winfo_screenwidth()),(root.winfo_screenheight())))
try:
    root.background
    root.iconbitmap(r'C:\Users\ANKIT\Downloads\logo.ico')
except:
    pass
def donothing():
    pass
def fun1_start():
    pass
def fun2_stop():
    pass
def fun3_play():
    pass
def fun4_save():
    pass
def fun5_delete():
    pass
def fun1_lang():
    def en_lang():
        pass
    def hn_lang():
        pass
    def frn_lang():
        pass
    def du_lang():
        pass
    b1=Button(sub_frame3,text="English",command=en_lang).place(x=5,y=310)
    b2=Button(sub_frame3,text="French",command=frn_lang).place(x=5,y=337)
    b3=Button(sub_frame3,text="Dutch",command=du_lang).place(x=5,y=365)
    b4=Button(sub_frame3,text="Hindi",command=hn_lang).place(x=5,y=392)
def fun2_voice():
    def sophia():
        pass
    def alexa():
        pass
    def google():
        pass
    b1=Button(sub_frame3,text="sophia",command=sophia).place(x=60,y=310)
    b2=Button(sub_frame3,text="Alexa",command=alexa).place(x=60,y=337)
    b3=Button(sub_frame3,text="Google",command=google).place(x=60,y=365)
def fun3_pace():
    def fast():
        pass
    def medium():
        pass
    def slow():
        pass
    b1=Button(sub_frame3,text="FAST",command=fast).place(x=120,y=310)
    b2=Button(sub_frame3,text="Medium",command=medium).place(x=120,y=337)
    b3=Button(sub_frame3,text="Slow",command=slow).place(x=120,y=365)
#menu bar
mbar=Menu(root)
fmenu=Menu(mbar,tearoff=0)

mbar.add_cascade(label="File",menu=fmenu)
fmenu.add_command(label="New",command=donothing)
fmenu.add_command(label="Open",command=donothing)
fmenu.add_command(label="Save",command=donothing)
fmenu.add_command(label="Save as",command=donothing)
fmenu.add_separator()
fmenu.add_command(label="Exit",command=root.destroy)

Emenu=Menu(mbar,tearoff=0)
mbar.add_cascade(label="Tools",menu=Emenu)
Emenu.add_command(label="Search",command=donothing)
Emenu.add_cascade(label="Cut",command=donothing)
Emenu.add_cascade(label="Copy",command=donothing)
Emenu.add_cascade(label="Paste",command=donothing)
Emenu.add_cascade(label="Restart",command=donothing)

hmenu=Menu(mbar,tearoff=0)
mbar.add_cascade(label="Help",menu=hmenu)
hmenu.add_command(label="About",command=donothing)
hmenu.add_command(label="Credits",command=donothing)
root.config(menu=mbar)
#left_frame
side_frame=Frame(root,bg='#5c6e5c',height=1000,width=300).place(x=0,y=0)
#bhai smjh nhi aya iske liye isliye khaali frame h
sub_frame1=Frame(side_frame,bg="#ffffff",height=200,width=290).place(x=5,y=3)
#Select_box
sub_frame2=Frame(side_frame,bg='#ffffff',height=90,width=290).place(x=5,y=210)

s_1=Button(sub_frame2,text="Choose language",command=fun1_lang).place(x=6,y=210)
s_2=Button(sub_frame2,text="Select Voice",command=fun2_voice).place(x=6,y=240)
s_3=Button(sub_frame2,text="Set pace",command=fun3_pace).place(x=6,y=270)
#Check_box
sub_frame3=Frame(side_frame,bg='#ffffff',height=110,width=290).place(x=5,y=310)

sub_frame4=Frame(side_frame,bg='#ffffff',height=50,width=290).place(x=5,y=430)
slid1=Scale(sub_frame4,from_=0,to=10,length=270,resolution=0.1,orient=HORIZONTAL).place(x=12,y=440)
#Info
sub_frame5=Frame(side_frame,bg='#ffffff',height=300,width=290).place(x=5,y=480)
entry1=Text(sub_frame5,bg="#ffffff").place(x=0,y=510)
#upper frame
frame1=Frame(root,bg='#748f74',height=300,width=1000).place(x=310,y=0)
#btn frame
frame2=Frame(root,bg='#617861',height=50,width=1000).place(x=310,y=320)
btn1=Button(frame2,text='Start',padx=30,pady=8,command=fun1_start).place(x=320,y=325)
btn1=Button(frame2,text='Stop',padx=30,pady=8,command=fun2_stop).place(x=420,y=325)
btn1=Button(frame2,text='Play',padx=30,pady=8,command=fun3_play).place(x=520,y=325)
btn1=Button(frame2,text='Save',padx=30,pady=8,command=fun4_save).place(x=620,y=325)
btn5=Button(frame2,text='Delete',padx=30,pady=8,command=fun5_delete).place(x=720,y=325)

#Editing frame
frame3=Frame(root,bg='#5d7897',height=600,width=1000).place(x=310,y=390)
entry=Text(frame3,bg='#ffffff',height=600,width=1000).place(x=310,y=390)
#right_frame
rside_frame=Frame(root,bg='#5c6e6c',height=1000,width=200).place(x=1320,y=0)


root.mainloop()
