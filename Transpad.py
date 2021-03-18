import pyaudio                                                                  #for microphone
import tkinter                                                                  #for gui
import os                                                                       #for saving and opening the file    
from googletrans import Translator                                              #for translator
from tkinter import *                                                           #for gui
from tkinter.messagebox import *                                                #for gui
from tkinter.filedialog import *                                                #for gui

translator = Translator()
class Transpad:
  
    __root = Tk() 
  
    # default window width and height 
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root) 
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0) 
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0) 
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
    __thisAImenu= Menu(__thisMenuBar,tearoff=0)
    __thisLangmenu = Menu(__thisMenuBar,tearoff=0)
    # To add scrollbar 
    __thisScrollBar = Scrollbar(__thisTextArea)      
    __file = None
  
    def __init__(self,**kwargs):
        
  
        # Set icon 
        try: 
                self.__root.wm_iconbitmap("Transpad.ico")  
        except: 
                pass
  
        # Set window size (the default is 300x300) 
  
        try: 
            self.__thisWidth = kwargs['width'] 
        except KeyError: 
            pass
  
        try: 
            self.__thisHeight = kwargs['height'] 
        except KeyError: 
            pass
  
        # Set the window text 
        self.__root.title("Untitled - Transpad") 
  
        # Center the window 
        screenWidth = self.__root.winfo_screenwidth() 
        screenHeight = self.__root.winfo_screenheight() 
      
        # For left-alling 
        left = (screenWidth / 2) - (self.__thisWidth / 2)  
          
        # For right-allign 
        top = (screenHeight / 2) - (self.__thisHeight /2)  
          
        # For top and bottom 
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
                                              self.__thisHeight, 
                                              left, top))  
  
        # To make the textarea auto resizable 
        self.__root.grid_rowconfigure(0, weight=1) 
        self.__root.grid_columnconfigure(0, weight=1) 
  
        # Add controls (widget) 
        self.__thisTextArea.grid(sticky = N + E + S + W) 
          
        # To open new file 
        self.__thisFileMenu.add_command(label="New", 
                                        command=self.__newFile)     
          
        # To open a already existing file 
        self.__thisFileMenu.add_command(label="Open", 
                                        command=self.__openFile) 
          
        # To save current file 
        self.__thisFileMenu.add_command(label="Save", 
                                        command=self.__saveFile)     
  
        # To create a line in the dialog         
        self.__thisFileMenu.add_separator()                                          
        self.__thisFileMenu.add_command(label="Exit", 
                                        command=self.__quitApplication) 
        self.__thisMenuBar.add_cascade(label="File", 
                                       menu=self.__thisFileMenu)      
          
        # To give a feature of cut  
        self.__thisEditMenu.add_command(label="Cut", 
                                        command=self.__cut)              
      
        # to give a feature of copy     
        self.__thisEditMenu.add_command(label="Copy", 
                                        command=self.__copy)          
          
        # To give a feature of paste 
        self.__thisEditMenu.add_command(label="Paste", 
                                        command=self.__paste)          
          
        # To give a feature of editing 
        self.__thisMenuBar.add_cascade(label="Edit", 
                                       menu=self.__thisEditMenu)      
          
        # To create a feature of description of the Transpad 
        self.__thisHelpMenu.add_command(label="About Transpad", 
                                        command=self.__showAbout)  
        self.__thisMenuBar.add_cascade(label="Help",
                                       menu=self.__thisHelpMenu)
        # For the AI
        self.__thisAImenu.add_command(label="Voice to text",
                                      command=self.voice)
        self.__thisMenuBar.add_cascade(label="AI", 
                                       menu=self.__thisAImenu)
        # For the Translation
        self.__thisLangmenu.add_command(label="HINDI",command=self.langH)
        self.__thisLangmenu.add_command(label="ENGLISH",command=self.langE)
        self.__thisLangmenu.add_command(label="Japanese",command=self.langJ)
        self.__thisLangmenu.add_command(label="Chinese",command=self.langC)
        self.__thisLangmenu.add_command(label="Arabic",command=self.langA)
        self.__thisLangmenu.add_command(label="Bulgarian",command=self.langB)
        self.__thisLangmenu.add_command(label="Bengali",command=self.langBen)
        self.__thisLangmenu.add_command(label="Croatian",command=self.langCro)
        self.__thisLangmenu.add_command(label="Czech",command=self.langCz)
        self.__thisLangmenu.add_command(label="German",command=self.langG)
        self.__thisLangmenu.add_command(label="Korean",command=self.langK)
        self.__thisLangmenu.add_command(label="Indonesian",command=self.langI)
        self.__thisLangmenu.add_command(label="Malyalam",command=self.langMal)
        self.__thisLangmenu.add_command(label="Marathi",command=self.langMar)
        self.__thisLangmenu.add_command(label="Nepali",command=self.langN)
        self.__thisLangmenu.add_command(label="Urdu",command=self.langU)
        self.__thisMenuBar.add_cascade(label="Languages",
                                       menu=self.__thisLangmenu)
          

  
        self.__root.config(menu=self.__thisMenuBar) 
  
        self.__thisScrollBar.pack(side=RIGHT,fill=Y)                     
          
        # Scrollbar will adjust automatically according to the content         
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)      
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set) 
      
          
    #voice input
    def voice(self):
        import speech_recognition as sr
        r=sr.Recognizer()
        with sr.Microphone() as x:        
            text=r.listen(x)
            a=r.recognize(text)
            a=a.lower()
            self.__thisTextArea.insert(1.0,a)
    #Tranlator
    def langE(self):
        a=self.__thisTextArea.get(1.0,END)
        translated = translator.translate(a, dest ='en')
        trans=translated.text
        self.__thisTextArea.delete(1.0,END) 
        self.__thisTextArea.insert(1.0,trans)
    def langH(self):
        a=self.__thisTextArea.get(1.0,END)
        translated = translator.translate(a, dest ='hi')
        trans=translated.text
        self.__thisTextArea.delete(1.0,END) 
        self.__thisTextArea.insert(1.0,trans)
    def langJ(self):
        a=self.__thisTextArea.get(1.0,END)
        translated = translator.translate(a, dest ='ja')
        trans=translated.text
        self.__thisTextArea.delete(1.0,END) 
        self.__thisTextArea.insert(1.0,trans)
    def langA(self):
        a=self.__thisTextArea.get(1.0,END)
        translated = translator.translate(a, dest ='ar')
        trans=translated.text
        self.__thisTextArea.delete(1.0,END) 
        self.__thisTextArea.insert(1.0,trans)
    def langB(self):
        a=self.__thisTextArea.get(1.0,END)
        translated = translator.translate(a, dest ='bg')
        trans=translated.text
        self.__thisTextArea.delete(1.0,END) 
        self.__thisTextArea.insert(1.0,trans)
    def langBen(self):
        a=self.__thisTextArea.get(1.0,END)
        translated = translator.translate(a, dest ='bn')
        trans=translated.text
        self.__thisTextArea.delete(1.0,END) 
        self.__thisTextArea.insert(1.0,trans)
    def langCro(self):
        a=self.__thisTextArea.get(1.0,END)
        translated = translator.translate(a, dest ='hr')
        trans=translated.text
        self.__thisTextArea.delete(1.0,END) 
        self.__thisTextArea.insert(1.0,trans)
    def langCz(self):
        a=self.__thisTextArea.get(1.0,END)
        translated = translator.translate(a, dest ='cs')
        trans=translated.text
        self.__thisTextArea.delete(1.0,END) 
        self.__thisTextArea.insert(1.0,trans)
    def langG(self):
        a=self.__thisTextArea.get(1.0,END)
        translated = translator.translate(a, dest ='de')
        trans=translated.text
        self.__thisTextArea.delete(1.0,END) 
        self.__thisTextArea.insert(1.0,trans)
    def langK(self):
        a=self.__thisTextArea.get(1.0,END)
        translated = translator.translate(a, dest ='ko')
        trans=translated.text
        self.__thisTextArea.delete(1.0,END) 
        self.__thisTextArea.insert(1.0,trans)
    def langI(self):
        a=self.__thisTextArea.get(1.0,END)
        translated = translator.translate(a, dest ='id')
        trans=translated.text
        self.__thisTextArea.delete(1.0,END) 
        self.__thisTextArea.insert(1.0,trans)
    def langMal(self):
        a=self.__thisTextArea.get(1.0,END)
        translated = translator.translate(a, dest ='ml')
        trans=translated.text
        self.__thisTextArea.delete(1.0,END) 
        self.__thisTextArea.insert(1.0,trans)
    def langMar(self):
        a=self.__thisTextArea.get(1.0,END)
        translated = translator.translate(a, dest ='mr')
        trans=translated.text
        self.__thisTextArea.delete(1.0,END) 
        self.__thisTextArea.insert(1.0,trans)
    def langN(self):
        a=self.__thisTextArea.get(1.0,END)
        translated = translator.translate(a, dest ='ne')
        trans=translated.text
        self.__thisTextArea.delete(1.0,END) 
        self.__thisTextArea.insert(1.0,trans)
    def langU(self):
        a=self.__thisTextArea.get(1.0,END)
        translated = translator.translate(a, dest ='ur')
        trans=translated.text
        self.__thisTextArea.delete(1.0,END) 
        self.__thisTextArea.insert(1.0,trans)
    def langC(self):
        a=self.__thisTextArea.get(1.0,END)
        translated = translator.translate(a, dest ='zh-cn')
        trans=translated.text
        self.__thisTextArea.delete(1.0,END) 
        self.__thisTextArea.insert(1.0,trans)
    
    def __quitApplication(self): 
        self.__root.destroy() 
        # exit() 
  
    def __showAbout(self): 
        showinfo("Transpad","Team Transpad") 
  
    #FIle Options
    def __openFile(self): 
          
        self.__file = askopenfilename(defaultextension=".txt", 
                                      filetypes=[("All Files","*.*"), 
                                        ("Text Documents","*.txt")]) 
  
        if self.__file == "": 
              
            # no file to open 
            self.__file = None
        else: 
              
            # Try to open the file 
            # set the window title 
            self.__root.title(os.path.basename(self.__file) + " - Transpad") 
            self.__thisTextArea.delete(1.0,END) 
  
            file = open(self.__file,"r") 
  
            self.__thisTextArea.insert(1.0,file.read()) 
  
            file.close() 
  
          
    def __newFile(self): 
        self.__root.title("Untitled - Transpad") 
        self.__file = None
        self.__thisTextArea.delete(1.0,END) 
  
    def __saveFile(self): 
  
        if self.__file == None: 
            # Save as new file 
            self.__file = asksaveasfilename(initialfile='Untitled.txt', 
                                            defaultextension=".txt", 
                                            filetypes=[("All Files","*.*"), 
                                                ("Text Documents","*.txt")]) 
  
            if self.__file == "": 
                self.__file = None
            else: 
                  
                # Try to save the file 
                file = open(self.__file,"w") 
                file.write(self.__thisTextArea.get(1.0,END)) 
                file.close() 
                  
                # Change the window title 
                self.__root.title(os.path.basename(self.__file) + " - Transpad") 
                  
              
        else: 
            file = open(self.__file,"w") 
            file.write(self.__thisTextArea.get(1.0,END)) 
            file.close() 
  
    #Edit Options
    def __cut(self): 
        self.__thisTextArea.event_generate("<<Cut>>") 
  
    def __copy(self): 
        self.__thisTextArea.event_generate("<<Copy>>") 
  
    def __paste(self): 
        self.__thisTextArea.event_generate("<<Paste>>") 
  
    def run(self): 
  
        # Run main application 
        self.__root.mainloop()
        

  
  
  
  
# Run main application 
Transpad = Transpad(width=600,height=400) 
Transpad.run()
