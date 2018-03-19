# -*- coding: utf-8 -*-


"""
 .. topic:: Module ``ask``

   :author: `Mohamed Amine ELBACHRA`_

   :date:  2015, october

   This module handles the interaction with player .


"""
from tkinter import *
import player as Player
import tkinter.messagebox as msgbox

def askdif():
    """
    asks the diffuclty

    :return: the diffuclty
    """
    global var, root
    root = Tk()
    var = StringVar()
    for item in ['Easy', 'Medium', 'Hard']:
        rb = Radiobutton(root, text=item,
                          value=item,
                          variable=var)
        rb.pack(side=LEFT)
    b = Button(root, text='Go!', command = dif)
    b.pack()
    root.mainloop()
    return res1
    
def dif():
    """
    handles the different choices

    :return: the chosed value
    """
    global var, res1
    if  (var.get()) == 'Easy':
        res1 =  1
    elif (var.get()) == 'Medium':
        res1 = 5
    elif var.get() == 'Hard':
        res1 = 7
    root.destroy()
    return res1
def askplayer():
    """
    handles the different choices

    :return: the chosed the chosed value
    """
    global root, var1
    root = Tk()
    var1 = StringVar()
    for item in ['1 player', '2 players']:
        rb = Radiobutton(root, text=item, value=item, variable=var1)
        rb.pack(side=LEFT)
    b = Button(root, text='Go!', command = player)
    b.pack()
    root.mainloop()
    return res
    
def player():
    """
    :return: the chosed value
    """
    global var1, res
    if  (var1.get()) == '1 player':
        res = 1
    elif (var1.get()) == '2 players':
        res = 2
    root.destroy()
    return res
    
