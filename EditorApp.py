from imaplib import Int2AP
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageFilter, ImageEnhance, ImageColor, ImageTk
import os

root = Tk()
root.title("Basic Photo Editor")
root.geometry("700x800")

def select():
    global img_path, img
    img_path = filedialog.askopenfilename(initialdir=os.getcwd())
    img = Image.open(img_path)
    img.thumbnail((300,300))
    img1 = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=img1)
    canvas2.image = img1

def blur(event): 
    global img_path, img1, imgg
    for m in range(0, v1.get() + 1):
        img=Image.open(img_path)
        img.thumbnail((300,300))
        imgg = img.filter(ImageFilter.BoxBlur(m))
        img1 = ImageTk.PhotoImage(imgg)
        canvas2.create_image(300, 210, image= img1)
        canvas2.image = img1

def brightness(event): 
    global img_path, img2, img3
    for m in range(0, v2.get() + 1):
        img=Image.open(img_path)
        img.thumbnail((300,300))
        imgg = ImageEnhance.Brightness(img)
        img2 = imgg.enhance(m)
        img3 = ImageTk.PhotoImage(img2)
        canvas2.create_image(300, 210, image= img3)
        canvas2.image = img3

def contrast(event):
    global img_path, img4, img5
    for m in range(0, v3.get()+1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = ImageEnhance.Contrast(img)
        img4 = imgg.enhance(m)
        img5 = ImageTk.PhotoImage(img4)
        canvas2.create_image(300, 210, image=img5)
        canvas2.image = img5

def rotate(event): 
    global img_path, img6, img7
    img=Image.open(img_path)
    img.thumbnail((300,300))
    img6 = img.rotate((rotate_combo.get()))
    img7 = ImageTk.PhotoImage(img6)
    canvas2.create_image(300, 210, image= img7)
    canvas2.image = img7     


#def color(event): 
#    global img_path, img8, img9
#    for m in range(0, v4.get() + 1):
#       img=Image.open(img_path)
#        img.thumbnail((300,300))
#        img8 = ImageColor.getcolor()
#        img9 = ImageTk.PhotoImage(img9)
#        canvas2.create_image(300, 210, image= img9)
#        canvas2.image = img9"
        
def grayscale(event): 
    global img_path, imgg1, img10, img11
    for m in range(0, v6.get() + 1):
        img=Image.open(img_path)
        img.thumbnail((300,300))
        imgg1 = ImageEnhance.Color(img)
        img10 = imgg1.enhance.color(m)
        img11 = ImageTk.PhotoImage(img10)
        canvas2.create_image(300, 210, image= img11)
        canvas2.image = img11

def sharpness(event): 
    global img_path, img12, img13
    for m in range(0, v5.get() + 1):
        img=Image.open(img_path)
        img.thumbnail((300,300))
        imgg = ImageEnhance.Sharpness(img)
        img12 = imgg.enhance(m)
        img13 = ImageTk.PhotoImage(img12)
        canvas2.create_image(300, 210, image= img13)
        canvas2.image = img13

img1 = None
img3 = None
img5 = None
img7 = None
img9 = None
img11 = None
img2 = None

def save():
    global img_path, img1, imgg, img2, img3, img4, img5, img6, img7, img8, img9, im10, img11
    ext = img_path.split(".")[-1]
    file = asksaveasfilename(defaultextension=f".{ext}", filetypes=[( "All Files", "*.*"), ("PNG file", "*.png"), ("JPG file", "*.jpg")])
    if file:
        if canvas2.image == img1:
            imgg.save(file)
        elif canvas2.image == img3:
            img2.save(file)
        elif canvas2.image == img5:
            img4.save(file)
        elif canvas2.image == img7:
            img6.save(file)    
        elif canvas2.image == img9:
            img8.save(file)  
        elif canvas2.image == img11:
            img10.save(file) 
        elif canvas2.image == img13:
            img12.save(file)      

#Interface
#Blur
blurr = Label(root, text="Blur:", font=("ariel 17 bold"), width=9, anchor='e')
blurr.place(x=15, y=8)
v1 = IntVar()
scale1 = ttk.Scale(root, from_=0, to=5, variable=v1,
                   orient=HORIZONTAL, command=blur)
scale1.place(x=150, y=10)

#Brightness
bright = Label(root, text="Brightness:", font=("ariel 17 bold"))
bright.place(x=8, y=50)
v2 = IntVar()
scale2 = ttk.Scale(root, from_=0, to=2, variable=v2,
                   orient=HORIZONTAL, command=brightness)
scale2.place(x=150, y=55)

#Contrast
contrast = Label(root, text="Contrast:", font=("ariel 17 bold"))
contrast.place(x=35, y=92)
v3 = IntVar()
scale3 = ttk.Scale(root, from_=0, to=10, variable=v3,
                   orient=HORIZONTAL, command=contrast)
scale3.place(x=150, y=100)

#B&W/Grayscale
grayscale = Label(root, text="Black & White:", font=("ariel 17 bold"))
grayscale.place(x=370, y=50)
v6 = IntVar()
scale4 = ttk.Scale(root, variable=v6, from_= 0, to= 1, orient=HORIZONTAL, command=grayscale)
#scale4 = ttk.Checkbutton(root, command=grayscale, onvalue=0.0, offvalue=1.0)
scale4.place(x=500, y=55)

#Sharpness
sharp = Label(root, text="Sharpness:", font=("ariel 17 bold"), width=9, anchor='e')
sharp.place(x=370, y=92)
v5 = IntVar()
scale5 = ttk.Scale(root, from_=0, to=10, variable=v5,
                   orient=HORIZONTAL, command=sharpness)
scale5.place(x=500, y=92)

#Rotate
rotate = Label(root, text="Rotate:", font=("ariel 17 bold"))
rotate.place(x=370, y=8)
values = [0, 90, 180, 270, 360]
rotate_combo = ttk.Combobox(root, values=values, font=('ariel 10 bold'))
rotate_combo.place(x=460, y=15)
rotate_combo.bind("<<ComboboxSelected>>", rotate)

# create canvas to display image
canvas2 = Canvas(root, width="600", height="420", relief=RIDGE, bd=2)
canvas2.place(x=15, y=150)

#CREATE BUTTONS
#select button
btn1 = Button(root, text="Select Image", bg='black', fg='blue',
              font=('ariel 15 bold'), relief=GROOVE, command=select)
btn1.place(x=100, y=595)

#save button
btn2 = Button(root, text="Save", width=12, bg='black', fg='blue',
              font=('ariel 15 bold'), relief=GROOVE, command=save)
btn2.place(x=280, y=595)

#exit button
btn3 = Button(root, text="Exit", width=12, bg='black', fg='blue',
              font=('ariel 15 bold'), relief=GROOVE, command=root.destroy)
btn3.place(x=460, y=595)

root.mainloop()
