'''
CREATED BY: Jessica Gallo
START DATE: 10/27/2019
LAST MODIFIED: 11/06/2019
INFO: Python program for Hangman
      Gives you the option of changing the language
      (English, Italian, French, Spanish, Japanese)
      Uses Tkinter and Turtle modules
'''

from tkinter import *
# import turtle

# ########## WINDOW ##########
window = Tk()  # parent is called window
window.title("Hangman Game")  # sets title in white
window.resizable(0, 0)  # cant resize window

# ---------- Setting an image as the background
bg_image = PhotoImage(file=r"C:\Users\User\Pictures\CB.gif")

w = bg_image.width()  # gets image width
h = bg_image.height()  # gets image height
window.geometry("%dx%d+0+0" % (w, h))  # sets window as width and height of picture

panel1 = Label(window, image=bg_image)
panel1.pack(side="top", fill="both", expand="yes")
# ----------
###############################

'''
def draw_circle(turtle, color, size, x, y):
    turtle.goto(150, 200)
    turtle.backward(150, 400)
    turtle.left(100, 400)
    turtle.backward(100, 450)
    turtle.right(200, 450)
    turtle.forward(200, 400)
    turtle.left(100, 400)
    turtle.forward()


tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(500)

draw_circle(tommy, "green", 50, 25, 10)
'''

# ########## MOUSEOVER FUNCTIONS ##########


def MouseOverEE(event):
    EasyBtnENG.config(foreground="light green")
    # changes look of button text to bold and green when mouse is over the button


def MouseLeaveEE(event):
    EasyBtnENG.config(foreground="white")
    # changes look of button text to it's original style when mouse is over the button


def ButtonClickedEE(event):
    EasyBtnENG.config(background="light green", foreground="black")


def MouseOverME(event):
    MedBtnENG.config(foreground="yellow")
    # changes look of button text to bold and yellow when mouse is over the button


def MouseLeaveME(event):
    MedBtnENG.config(foreground="white")
    # changes look of button text to it's original style when mouse is over the button


def ButtonClickedME(event):
    MedBtnENG.config(background="yellow", foreground="black")


def MouseOverHE(event):
    HardBtnENG.config(foreground="red")
    # changes look of button text to bold and red when mouse is over the button


def MouseLeaveHE(event):
    HardBtnENG.config(font=("ink free", 20, "normal"), foreground="white")
    # changes look of button text to it's original style when mouse is over the button


def ButtonClickedHE(event):
    HardBtnENG.config(background="red", foreground="black")
#############################################


panel1.image = bg_image  # saves the panel's image from garbage collection

panel1.grid_columnconfigure(1, weight=1)

# Header Title for game
HMLbl = Label(panel1,
              text="HANGMAN",  # sets what the text is going to say
              font=("ink free", 60),  # sets font and size of font
              background="#1f1d1d",    # sets background color of text
              foreground="white")  # sets the color of the text
HMLbl.grid(row=0, column=1, columnspan=4)   # sets where the label will be on the grid
HMLbl.config(anchor=CENTER)

panel1.grid_rowconfigure(1, weight=1)

# ########## BUTTONS ##########
# ===== ENGLISH =====
# command:lambda:function() attaches the function to the button
EasyBtnENG = Button(panel1,
                    text="EASY",
                    font=("ink free", 20),
                    background="#1f1d1d",
                    foreground="white",
                    height=1,
                    width=8,
                    command=lambda: EasyClickENG())
EasyBtnENG.bind("<Enter>", MouseOverEE)
EasyBtnENG.bind("<Leave>", MouseLeaveEE)
EasyBtnENG.bind("<Button-1>", ButtonClickedEE)
EasyBtnENG.config(cursor="hand1", relief="raised")
EasyBtnENG.grid(row=2, column=3)

MedBtnENG = Button(panel1,
                   text="MEDIUM",
                   font=("ink free", 20),
                   background="#1f1d1d",
                   foreground="white",
                   height=1,
                   width=8,
                   command=lambda: MedClickENG())
MedBtnENG.bind("<Enter>", MouseOverME)
MedBtnENG.bind("<Leave>", MouseLeaveME)
MedBtnENG.bind("<Button-1>", ButtonClickedME)
MedBtnENG.config(cursor="hand1")
MedBtnENG.grid(row=3, column=3)

HardBtnENG = Button(panel1,
                    text="HARD",
                    font=("ink free", 20),
                    background="#1f1d1d",
                    foreground="white",
                    height=1,
                    width=8,
                    borderwidth=2,
                    command=lambda: HardClickENG())
HardBtnENG.bind("<Enter>", MouseOverHE)
HardBtnENG.bind("<Leave>", MouseLeaveHE)
HardBtnENG.bind("<Button-1>", ButtonClickedHE)
HardBtnENG.config(cursor="hand1")
HardBtnENG.grid(row=4, column=3)
################################

panel1.grid_columnconfigure(4, weight=1)
panel1.grid_rowconfigure(5, weight=1)


def MouseOverLetter(event):
    EasyBtnENG.config(foreground="grey")
    # changes look of button text to bold and green when mouse is over the button


def MouseLeaveLetter(event):
    EasyBtnENG.config(foreground="black")
    # changes look of button text to it's original style when mouse is over the button


# ########## BUTTON FUNCTIONS ##########
# ===== ENGLISH =====
def EasyClickENG():
    EasyBtnENG.grid_forget()
    MedBtnENG.grid_forget()
    HardBtnENG.grid_forget()

    # panel1.grid_rowconfigure()

    def LetterClickedENG():
        print("A")
        Abtn.config(state=DISABLED)

    # ########## LETTER BUTTONS ##########
    Abtn = Button(panel1,
                  text="A",
                  font=("ink free", 15),
                  background="#1f1d1d",
                  foreground="white",
                  height=1,
                  width=2,
                  command=lambda: LetterClickedENG())
    Abtn.bind("<Enter>", MouseOverLetter)
    Abtn.bind("<Leave>", MouseLeaveLetter)
    Abtn.config(cursor="hand1")
    Abtn.grid(row=5, column=1)

    Bbtn = Button(panel1,
                  text="B",
                  font=("ink free", 15),
                  background="#1f1d1d",
                  foreground="white",
                  height=1,
                  width=2,
                  command=lambda: LetterClickedENG())
    Bbtn.bind("<Enter>", MouseOverLetter)
    Bbtn.bind("<Leave>", MouseLeaveLetter)
    Bbtn.config(cursor="hand1")
    Bbtn.grid(row=5, column=2)

    Cbtn = Button(panel1,
                  text="C",
                  font=("ink free", 15),
                  background="#1f1d1d",
                  foreground="white",
                  height=1,
                  width=2,
                  command=lambda: LetterClickedENG())
    Cbtn.bind("<Enter>", MouseOverLetter)
    Cbtn.bind("<Leave>", MouseLeaveLetter)
    Cbtn.config(cursor="hand1")
    Cbtn.grid(row=5, column=3)

    Dbtn = Button(panel1,
                  text="D",
                  font=("ink free", 15),
                  background="#1f1d1d",
                  foreground="white",
                  height=1,
                  width=2,
                  command=lambda: LetterClickedENG())
    Dbtn.bind("<Enter>", MouseOverLetter)
    Dbtn.bind("<Leave>", MouseLeaveLetter)
    Dbtn.config(cursor="hand1")
    Dbtn.grid(row=5, column=4)

    Ebtn = Button(panel1,
                  text="E",
                  font=("ink free", 15),
                  background="#1f1d1d",
                  foreground="white",
                  height=1,
                  width=2,
                  command=lambda: LetterClickedENG())
    Ebtn.bind("<Enter>", MouseOverLetter)
    Ebtn.bind("<Leave>", MouseLeaveLetter)
    Ebtn.config(cursor="hand1")
    Ebtn.grid(row=5, column=5)

    Fbtn = Button(panel1,
                  text="F",
                  font=("ink free", 15),
                  background="#1f1d1d",
                  foreground="white",
                  height=1,
                  width=2,
                  command=lambda: LetterClickedENG())
    Fbtn.bind("<Enter>", MouseOverLetter)
    Fbtn.bind("<Leave>", MouseLeaveLetter)
    Fbtn.config(cursor="hand1")
    Fbtn.grid(row=5, column=6)

    Gbtn = Button(panel1,
                  text="G",
                  font=("ink free", 15),
                  background="#1f1d1d",
                  foreground="white",
                  height=1,
                  width=2,
                  command=lambda: LetterClickedENG())
    Gbtn.bind("<Enter>", MouseOverLetter)
    Gbtn.bind("<Leave>", MouseLeaveLetter)
    Gbtn.config(cursor="hand1")
    Gbtn.grid(row=5, column=7)

    Hbtn = Button(panel1,
                  text="H",
                  font=("ink free", 15),
                  background="#1f1d1d",
                  foreground="white",
                  height=1,
                  width=2,
                  command=lambda: LetterClickedENG())
    Hbtn.bind("<Enter>", MouseOverLetter)
    Hbtn.bind("<Leave>", MouseLeaveLetter)
    Hbtn.config(cursor="hand1")
    Hbtn.grid(row=5, column=8)

    Ibtn = Button(panel1,
                  text="I",
                  font=("ink free", 15),
                  background="#1f1d1d",
                  foreground="white",
                  height=1,
                  width=2,
                  command=lambda: LetterClickedENG())
    Ibtn.bind("<Enter>", MouseOverLetter)
    Ibtn.bind("<Leave>", MouseLeaveLetter)
    Ibtn.config(cursor="hand1")
    Ibtn.grid(row=5, column=9)

    Jbtn = Button(panel1,
                  text="J",
                  font=("ink free", 15),
                  background="#1f1d1d",
                  foreground="white",
                  height=1,
                  width=2,
                  command=lambda: LetterClickedENG())
    Jbtn.bind("<Enter>", MouseOverLetter)
    Jbtn.bind("<Leave>", MouseLeaveLetter)
    Jbtn.config(cursor="hand1")
    Jbtn.grid(row=6, column=1)

    Kbtn = Button(panel1,
                  text="K",
                  font=("ink free", 15),
                  background="#1f1d1d",
                  foreground="white",
                  height=1,
                  width=2,
                  command=lambda: LetterClickedENG())
    Kbtn.bind("<Enter>", MouseOverLetter)
    Kbtn.bind("<Leave>", MouseLeaveLetter)
    Kbtn.config(cursor="hand1")
    Kbtn.grid(row=6, column=2)

    Lbtn = Button(panel1,
                  text="L",
                  font=("ink free", 15),
                  background="#1f1d1d",
                  foreground="white",
                  height=1,
                  width=2,
                  command=lambda: LetterClickedENG())
    Lbtn.bind("<Enter>", MouseOverLetter)
    Lbtn.bind("<Leave>", MouseLeaveLetter)
    Lbtn.config(cursor="hand1")
    Lbtn.grid(row=6, column=3)

    Mbtn = Button(panel1,
                  text="M",
                  font=("ink free", 15),
                  background="#1f1d1d",
                  foreground="white",
                  height=1,
                  width=2,
                  command=lambda: LetterClickedENG())
    Mbtn.bind("<Enter>", MouseOverLetter)
    Mbtn.bind("<Leave>", MouseLeaveLetter)
    Mbtn.config(cursor="hand1")
    Mbtn.grid(row=6, column=4)
    ########################################

def MedClickENG():
    print("That was medium!")


def HardClickENG():
    print("That was hard!")
# ======================================

"""
# ---------- ITALIANO BUTTONS
# command:lambda:function() attaches the function to the button
EasyBtnIT = Button(panel1,
                   text="FACILE",
                   command=lambda: EasyClickIT())
EasyBtnIT.grid(row=3, column=6, padx=100)

MedBtnIT = Button(panel1,
                  text="MEZZA",
                  command=lambda: MedClickIT())
MedBtnIT.grid(row=4, column=6, padx=100)

HardBtnIT = Button(panel1,
                   text="DIFACILE",
                   command=lambda: HardClickIT())
HardBtnIT.grid(row=5, column=6, padx=100)
# ----------


# ========== BUTTON FUNCTIONS ITALIANO ==========
def EasyClickIT():
    print('Era facile!')


def MedClickIT():
    print("Era mezza mezza!")


def HardClickIT():
    print("Era difficile!")
# ======================================


# ---------- FRANCOIS BUTTONS
# command:lambda:function() attaches the function to the button
EasyBtnFR = Button(panel1,
                   text="EASY",
                   command=lambda: EasyClickFR())
EasyBtnFR.grid(row=6, column=6, padx=100)

MedBtnFR = Button(panel1,
                  text="MEDIUM",
                  command=lambda: MedClickFR())
MedBtnFR.grid(row=7, column=6, padx=100)

HardBtnFR = Button(panel1,
                   text="HARD",
                   command=lambda: HardClickFR())
HardBtnFR.grid(row=8, column=6, padx=100)
# ----------


# ========== BUTTON FUNCTIONS FRANCOIS ==========
def EasyClickFR():
    print('Era facile!')


def MedClickFR():
    print("Era mezza mezza!")


def HardClickFR():
    print("Era difficile!")
# ======================================


# ---------- ESPANOL BUTTONS
# command:lambda:function() attaches the function to the button
EasyBtnSP = Button(panel1,
                   text="EASY",
                   command=lambda: EasyClickSP())
EasyBtnSP.grid(row=9, column=6, padx=100)

MedBtnSP = Button(panel1,
                  text="MEDIUM",
                  command=lambda: MedClickSP())
MedBtnSP.grid(row=10, column=6, padx=100)

HardBtnSP = Button(panel1,
                   text="HARD",
                   command=lambda: HardClickSP())
HardBtnSP.grid(row=11, column=6, padx=100)
# ----------


# ========== BUTTON FUNCTIONS ESPANOL ==========
def EasyClickSP():
    print('Era facile!')


def MedClickSP():
    print("Era mezza mezza!")


def HardClickSP():
    print("Era difficile!")
# ======================================


# ========== BUTTON FUNCTIONS NIHON==========
def EasyClickJP():
    print('Era facile!')


def MedClickJP():
    print("Era mezza mezza!")


def HardClickJP():
    print("Era difficile!")
# ======================================
"""

window.mainloop()
