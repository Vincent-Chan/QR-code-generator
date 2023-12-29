#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the necessary libraries and modules

import pyqrcode
import png
from PIL import ImageTk, Image
from pyqrcode import QRCode
import tkinter as tk
from tkinter import *
import PIL.Image


# In[2]:


# Create the window

window = Tk()  
window.geometry('500x500')
window.title('QR code generator')
 
Label(window,text='Please input the website in the following textbox',font='arial 15').pack()

# String which represents the QR code
s = tk.StringVar()


# In[3]:


# The function to create QR code

def create_qrcode():
    s1 = s.get()
    qr = pyqrcode.create(s1)
    qr.png('QRcode.png', scale = 6)
    Label(window,text='The QR Code is created and saved successfully as QRcode.png').pack()
    
# Creat the button and the input textbox

Entry(window,textvariable = s, font = 'arial 15').pack()
Button(window,text = 'create', bg = 'red' , command = create_qrcode).pack()


# In[4]:


# Display the window
window.mainloop()

