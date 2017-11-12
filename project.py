from Tkinter import *
from PIL import *
import Tkinter, Tkconstants, tkFileDialog
import ImageWriter
import Image, ImageFilter, ImageDraw

## Code designed and written by: Muza Alobaidan
## Andrew ID: mjalobai
## File Created: November 4, 2:00pm
## Modification History:
## Start         End
## 04/11 2:00pm  04/11 3:30pm
## 05/11 9:30am  05/11 12:15pm
## 06/11 8:00pm  06/11 10:15pm
## 10/11 3:00pm  10/11 05:25pm
## 11/11 12:00pm 11/11 02:30pm
## 11/11 4:00pm  11/11 08:00pm
## 12/11 9:00am  12/11 12:25pm


class Window:
    def __init__(self,parent=None):
        self.frame = Frame(parent,bg="white")
        self.frame.pack(expand=True,fill=BOTH)
        self.allbuttons = []
        menubar = Menu(parent) #creates menu bar 
        
        ##Buttons
        #rotation button refer to the rotation function once it is clicked
        rotation = Label(self.frame, text="Degrees of rotation: ") 
        rotation.grid(column=0, row=0)
        box = Entry(self.frame)
        box.grid(column=1, row=0)
        self.rotatebtn= Button(self.frame,text="Rotate", command=lambda: self.Rotate(box))
        self.rotatebtn.grid(column=2, row=0)
        self.allbuttons.append(self.rotatebtn)

        
        #text buttton refer to the text button once it is clicked
        self.textbtn= Button(self.frame, text="Text", command=self.Text) 
        self.allbuttons.append(self.textbtn)
        self.textbtn.grid(column=0,row=1)

        #blur button refer to the blur function once it is clicked
        self.blurbtn= Button(self.frame, text="Blur", command= self.Blur)
        self.allbuttons.append(self.blurbtn)
        self.blurbtn.grid(column=0,row=2)
        
        parent.config(menu=menubar)
        
        #menu bar
        #drop down list for open and save functions
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.Open)
        filemenu.add_command(label="Save", command = self.Save)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        #menu bar
        #drop down list for undo and redo functions
        fileMenu = Menu(menubar, tearoff=0)        
        fileMenu.add_command(label="Undo")
        fileMenu.add_command(label="Redo")
        menubar.add_cascade(label="Edit", menu=fileMenu)

    
    #this function open the open dialog box to open an image
    def Open(self):
        self.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        global FileName #global used to be able to call FileName in all other functions
        global pic #global used to be able to call pic in all other functions
        FileName=str(self.filename) 
        pic = Image.open(FileName) 

    #open the save dialog box
    #save the picture as hi.jpg in the same location of the file
    def Save(self):
        self.filename = tkFileDialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        name= str(self.filename)[72:]
        pic.save("hi.jpg")
        
    #this function blur the whole image (change the filter of the image)
    #then it saves it in the same location as this file
    #by default it saves it as hello.jpg in the same folder of the file
    def Blur(self):
        blurimage = pic.filter(ImageFilter.BLUR)
        blurimage.save("hello.jpg")

    #this function writes a text in the code once clicking on the text button
    #then it saves it in the same location as this file
    #the text Hello will be typed in orange in (50,50)
    #by default it will be saved as text.jpg in the same folder of this file
    def Text(self):
        draw = ImageDraw.Draw(pic)
        draw.text(xy=(85,85),text="Hello", fill=(0,0,0)) 
        pic.save("text.jpg")
        
    #this function rotates the image with the amount of degree that the user specify in the entry
    #then it saves it in the same location as this file by the name of rotateimage.jpg
    def Rotate(self,box):        
        rotateimage=pic.rotate(float(box.get()))
        rotateimage.save("rotateimage.jpg")
        
        


        

wnd = Tk()
wnd.geometry("1500x1500")
myWindow = Window(wnd)
wnd.mainloop()

