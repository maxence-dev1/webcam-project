import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import cv2
from PIL import Image, ImageTk
import datetime
import os



mdp  = '1234'

class Application:
    def __init__(self, window, cap):
        self.window = window

        self.cap = cap
        self.width, self.height = 1000, 562  

        self.canvas = tk.Canvas(window, width= self.width , height=self.height)
        self.canvas.pack()

        self.update()

    def update(self):
        self.ret, self.frame = self.cap.read()

        if self.ret:
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            self.frame = cv2.resize(self.frame, (self.width, self.height))
            img = Image.fromarray(self.frame)
            img_tk = ImageTk.PhotoImage(image=img)

            
            self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
            self.canvas.img_tk = img_tk  

        self.window.after(10, self.update)
    
    def screen(self):
        date = datetime.datetime.now()
        cv2.imwrite(f"F:\programmation\projet webcam\photos\{date.day}-{date.month},{date.hour}h{date.minute} {date.second}.jpg", self.frame)
        






def fermer():
    pass

def fermer_fenetre(event):
    window.destroy()



def place():
    window.geometry(f'+{0}+{0}')
    window.after(1, place)

def on_enter_pressed(event):
    user_input = entry.get()
    print("Texte entré :", user_input)
    if user_input == mdp : 
        window.destroy()
    else : 
        app.screen()
        os.system("shutdown /s /t 0")

def screenshot(event):
    app.screen()


def main():
    global window
    global entry
    global app
    cap = cv2.VideoCapture(0)
    window = tk.Tk()
    window.title("Verification")
    window.geometry(f"{window.winfo_screenwidth() + window.winfo_screenwidth()//10 }x{window.winfo_screenheight() + window.winfo_screenheight()//10}")
    place()
    window.config(background='#FFFFFF')
    frame = Frame(window, bg = "#FFFFFF")
    #texte de la fenetre
    texte = tk.Label(frame, text= 'souris tu es filmé',  font=("Helvetica", 100), bg = ("#FFFFFF"), fg = "#000000", justify = "center", wraplength=1080)
    app = Application(frame, cap)
    texte.pack(expand= YES)
    frame.pack()
    #empecher de bouger de fermer
    window.protocol("WM_DELETE_WINDOW", fermer)
    window.resizable(False, False)
    window.attributes("-toolwindow", True)
    window.bind("<KeyPress-q>", fermer_fenetre)
    window.bind("<Escape>", screenshot)

    #zone de texte
    entryFrame = tk.Frame(window, bg = "#FFFFFF")
    entryFrame.pack()
    texte = tk.Label(entryFrame, text= 'entre le mot de passe',  font=("Helvetica", 50), bg = ("#FFFFFF"), fg = "#000000", justify = "center", wraplength=1080)
    entry = tk.Entry(entryFrame, width=10,  font = tkFont.Font(family = 'Helvetica', size = 50))  
    entry.pack()
    texte.pack()
    
    entry.bind("<Return>", on_enter_pressed)
    
    window.mainloop()

    cap.release()
    cv2.destroyAllWindows()


main()
