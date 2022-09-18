#importing required libraries
from tkinter import *
import tkinter.messagebox
from captcha.image import ImageCaptcha
import string
import random
import os
import pyttsx3

audio_captcha=''
image_captcha=''
global ans
#generates image captcha's code and is  saved in variable image_captcha
def generate_captcha():
    data_set = list(string.ascii_letters+string.digits) #a-z,A-Z,0-9
    s=''
    for i in range(6):
        a=random.choice(data_set)
        s=s+a
        data_set.remove(a)

    global image_captcha
    image_captcha=s

    return s
#generates any 4 random numbers and is stored in a variable , audio captcha
def generate_digit_captcha():
    s1='';s=''
    for i in range(4):
        a = str(random.randint(0,9))
        s=s+a
        s1=s1+a+" "

    global audio_captcha
    audio_captcha=s

    return s1

#from OS a file named c1.png is generated where the image captcha will be displayed
def generate_image_captcha():
    os.startfile('c1.png')
#generates first image with the help of imagecaptcha library
def generate_first_image():
    img = ImageCaptcha()

    s = generate_captcha()
    #print(s)
    value = img.generate(s)
    img.write(s,"c1.png")

#function to regenerate image captcha
def regenerate_image_captcha():
    img = ImageCaptcha()

    s = generate_captcha()
    #print(s)
    value = img.generate(s)
    img.write(s,"c1.png")
    os.startfile('c1.png')
    #print("Image Captcha Generated.\n\n")

#function to generate the first audio captcha with the help of voice library which is imported from pyttsx3 library
def generate_audio_captcha():
    s=generate_digit_captcha()
    #print(s)

    voiceEngine = pyttsx3.init()

    voiceEngine.setProperty('rate',170)
    voiceEngine.setProperty('volume',1.0)

    voices = voiceEngine.getProperty('voices')
    voiceEngine.setProperty('voice',voices[1].id)

    voiceEngine.say(s)
    voiceEngine.runAndWait()
    voiceEngine.say(s)
    voiceEngine.runAndWait()

    #print("Audio Captcha Generated.\n\n")

def regenerate_audio_captcha():
    generate_audio_captcha()
#function to return the audio when the button is pressed
def get_audio():
    return audio_captcha
#function to return the image when the button is pressed
def get_image():
    return image_captcha

#function to check the text for audio captcha that's been taken
def check_audio_captcha():
    #answer = input("\nEnter Value : ")
    if ans.get() == get_audio():
        tkinter.messagebox.showinfo("SUCCESS!","Captcha Code Matched.")
        ans.set("")

    else:
        tkinter.messagebox.showinfo("WRONG!","Captcha Code does not Matched.")
        ans.set("")
#function to check the text for image captcha that's been taken
def check_image_captcha():
    if ans1.get() == get_image():
        tkinter.messagebox.showinfo("SUCCESS!","Captcha Code Matched.")
        ans1.set("")

    else:
        tkinter.messagebox.showinfo("WRONG!","Captcha Code does not Matched.")
        ans1.set("")
ans = StringVar()
#to open audio captcha in a new window
def openNewWindow():

    newWin= Tk()

    # sets the title of the
    # Toplevel widget
    newWin.title("Audio Captcha")


#framing the whole window with the required code
    Frame1 = LabelFrame(newWin, text="Audio Captcha.....", padx=50, pady=50, bg='cyan')
    Frame1.pack(padx=10, pady=20)

    Label_1 = Label(Frame1, font=('lato black', 33, 'bold'), text=" Audio Captcha ", padx=2, pady=2, bg="yellow",
                    fg="black")
    Label_1.grid(row=0, column=0, sticky=W)

    Label_2 = Label(Frame1, font=('arial', 20, 'bold'), text="", padx=2, pady=2, bg="cyan", fg="black")
    Label_2.grid(row=1, column=0, sticky=W)
#this button generates audio and thus plays the audio
    Label_9 = Button(Frame1, font=('arial', 19, 'bold'), text="Play Audio", padx=2, pady=2, bg="blue", fg="white",
                     command=generate_audio_captcha)
    Label_9.grid(row=4, column=0)

    Label_7 = Label(Frame1, font=('arial', 20, 'bold'), text="", padx=2, pady=2, bg="cyan", fg="black")
    Label_7.grid(row=2, column=0, sticky=W)
#entry block where the we will enter our input
    Entry_1 = Entry(Frame1, font=('arial', 20, 'bold'), bd=2, fg="black", textvariable=ans, width=14,
                    justify=LEFT)
    Entry_1.grid(row=5, column=0)

    Label_7 = Label(Frame1, font=('arial', 20, 'bold'), text="", padx=2, pady=2, bg="cyan", fg="black")
    Label_7.grid(row=6, column=0, sticky=W)

    Label_7 = Label(Frame1, font=('arial', 20, 'bold'), text="  ", padx=2, pady=2, bg="cyan", fg="black")
    Label_7.grid(row=6, column=1, sticky=W)
#this button checks the audio
    Label_8 = Button(Frame1, font=('Arial', 25, 'bold'), text="Check", padx=2, pady=2, bg="white", fg="blue",
                     command=check_audio_captcha)
    Label_8.grid(row=9, column=0)
#this button regenerates the audio
    Label_4 = Button(Frame1, font=('arial', 15, 'bold'), text="Regenerate", padx=2, pady=2, bg="white", fg="red",
                     command=regenerate_audio_captcha)
    Label_4.grid(row=10, column=0)

    Label_7 = Label(Frame1, font=('arial', 20, 'bold'), text="      ", padx=2, pady=2, bg="cyan", fg="black")
    Label_7.grid(row=11, column=1, sticky=W)


from PIL import ImageTk,Image

root= Tk()
root.title("GUI : captcha authentication-Image " )
root.configure(background="#b3edf8")
frame=LabelFrame(root,text="Image Captcha",padx=50 , pady=50,bg='cyan')
frame.pack(padx=10,pady=20)
Label_1 =Label( frame,font=('lato black', 33,'bold'), text=" Image Captcha ",padx=2,pady=2, bg="yellow",fg ="black")
Label_1.grid(row=0, column=0)



ans1 = StringVar()
generate_first_image()
#this button generates the image
Label_9 =Button(frame, font=('arial', 19,'bold'), text="Show Image",padx=2,pady=2, bg="blue",fg = "white",command=generate_image_captcha)
Label_9.grid(row=4, column=0)

Label_7 =Label(frame, font=('arial', 20,'bold'), text="",padx=2,pady=2, bg="cyan",fg = "black")
Label_7.grid(row=2, column=0,sticky=W)
#take entry from the user
Entry_1=Entry(frame,font=('arial',20,'bold'),bd=2,fg="black",textvariable= ans1, width=14,
justify=LEFT).grid(row=5,column=0)
Label_7 =Label(frame, font=('arial', 20,'bold'), text="",padx=2,pady=2, bg="cyan",fg = "black")
Label_7.grid(row=6, column=0,sticky=W)
Label_7 =Label(frame, font=('arial', 20,'bold'), text="  ",padx=2,pady=2, bg="cyan",fg = "black")
Label_7.grid(row=6, column=1,sticky=W)
#checks the image
Label_8 =Button(frame, font=('Arial', 25,'bold'), text="Check",padx=2,pady=2, bg="white",fg = "blue",command=check_image_captcha)
Label_8.grid(row=9, column=0)
#regenerates the image
Label_4 =Button(frame, font=('arial', 15,'bold'), text="Regenerate",padx=2,pady=2, bg="white",fg = "red",command=regenerate_image_captcha)
Label_4.grid(row=10, column=0)

Label_7 =Label(frame, font=('arial', 20,'bold'), text="      ",padx=2,pady=2, bg="cyan",fg = "black")
Label_7.grid(row=11, column=1,sticky=W)
button1=Button(frame, font=('arial', 15,'bold'), text="Audio Captcha",padx=2,pady=2, bg="white",fg = "red",command=openNewWindow)
button1.grid(row=12, column=0)
root.mainloop()