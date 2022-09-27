from tkinter import*
#import tkinter as Tk
from PIL import Image, ImageFilter, ImageEnhance, ImageColor


img = Image.open("dog.jpeg")


def showImg():
    global img
    img.show()

def reset():
    img = Image.open("dog.jpeg")
    print

def edgeEnhance():
    global img
    img = img.filter(filter=ImageFilter.EDGE_ENHANCE)
    y = 0
    while y < 20:
        img = ImageEnhance.Brightness(img).enhance(float(("0." + str(y))))
        img.show()
        img = Image.open("dog.jpeg")
        y+=1

def Smooth():
    global img
    img = img.filter(filter=ImageFilter.SMOOTH)

def brightness(x):
    global img
    x = float(x)
    img = ImageEnhance.Brightness(img).enhance(x)

def sharpness(x):
    global img
    x = float(x)
    img = ImageEnhance.Sharpness(img).enhance(x)

def contrast(x):
    global img
    x = float(x)
    img = ImageEnhance.Contrast(img).enhance(x)

def saturation(x):
    global img
    x = float(x)
    img = ImageEnhance.Color(img).enhance(x)

def showValue():
    global img
    if entries[0].get() != "":
        brightness(entries[0].get())
    if entries[1].get() != "":
        sharpness(entries[1].get())
    if entries[2].get() != "":
        contrast(entries[2].get())
    if entries[3].get() != "":
        saturation(entries[3].get())
    for i in range(5):
        print(entries[i].get())
    img.show()
    img = Image.open("dog.jpeg")



window = Tk()
window.configure(bg='blue')

window.resizable(0,0)
window.title("Photo Booth")
#window.geometry('500x500')

tools = ["Brightness", "Sharpness", "Contrast", "Saturation", "EdgeEnhance(1 or 0)"]



entries = []
for i in range(len(tools)):
    Label(window, text = tools[i], borderwidth=1).grid(row=i)
    entries.append(Entry(window))
    entries[i].grid(row=i, column=1)

Button(window, text='Enter Values', command=showValue).grid(row=len(tools),column=1,sticky=W,pady=4, padx=100)
Button(window, text='Quit', command=quit).grid(row=len(tools),column=0,sticky=W,pady=4, padx=100)

Checkbutton(window, text = "EdgeEnhance", command=edgeEnhance).grid(row=0, column=2, sticky=W, pady=4, padx=0)
Checkbutton(window, text = "Smooth", command=Smooth).grid(row=1, column=2, sticky=W, pady=4, padx=0)
Checkbutton(window, text = "Reset Image", command=reset).grid(row=2, column=2, sticky=W, pady=4, padx=0)


window.mainloop()
