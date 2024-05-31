import tkinter as tk
from tkinter import *
import playsound as p
from playsound import *

window = Tk()
window.geometry("200x250")
window.title("soundboard")
window.config(background="red")

def scream():
    p.playsound("carti-scream.mp3")

def wha():
    p.playsound("carti-wha.mp3")

def whatttt():
    p.playsound("carti-whatttt.mp3")

def seeyuh():
    p.playsound("carti-seeyuh.mp3")

def stummy():
    p.playsound("my-stummy-hurt.mp3")

def siren():
    p.playsound("credit-siren.mp3")

text= Label(window, text= "𝐂𝐀𝐑𝐓𝐈𝐍𝐄𝐒𝐄",background="red",foreground="white", font=2000)
text.pack()

text2= Label(window, text= "",background="red")
text2.pack()

bscream = Button(window,text="scream",command=scream,background="black",foreground="white")
bscream.pack()

bwha = Button(window,text="wha",command=wha,background="black",foreground="white")
bwha.pack()

bseeyuh = Button(window,text="seeyuh",command=seeyuh,background="black",foreground="white")
bseeyuh.pack()

bwhatttt = Button(window,text="whatttt",command=whatttt,background="black",foreground="white")
bwhatttt.pack()

bstummy = Button(window,text="stummy",command=stummy,background="black",foreground="white")
bstummy.pack()

bsiren = Button(window,text="siren",command=siren,background="black",foreground="white")
bsiren.pack()









window.mainloop()
