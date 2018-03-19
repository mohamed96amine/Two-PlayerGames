# -*- coding: utf-8 -*-


"""
 .. topic:: Module ``Connect4``

   :author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

   :date:  2015, october

   this module is an impletation of UI(User interface) of the connect4 game

"""


import os,ask, twoplayergame, random
import tkinter as tk
import player as Player
from functools import partial
from twoplayergame import *
import tkinter.messagebox as msgbox


def create():
    """
    creates the initial situation and draws it
    """
    global img
    global current
    g = puissance.create_game()
    sit = puissance.initSituation(g)
    if ask.askplayer() == 1:
        p1 = Player.new_player('human','X')
        p2 = Player.new_player('computer','O')
    else:
        p1 = Player.new_player('player1','X')
        p2 = Player.new_player('player2','O')
    p = [p1, p2]
    current = p[random.randint(0,1)]
    if Player.get_name(current) == 'computer' : 
            sit  = AlphaBeta.IA(sit,current,switch_player(current, p1,p2),6,puissance)
            current = switch_player(current, p1,p2)
    win = tk.Tk()
    win.title('puissance 4')
    iconpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"icons")
    img = [tk.PhotoImage(file=os.path.join(iconpath,"blanc1.gif")),
           tk.PhotoImage(file=os.path.join(iconpath,"rouge.gif")),
           tk.PhotoImage(file=os.path.join(iconpath,"jaune.gif"))]
    b = []
    for i in range(7):
        b.insert(i,[])
        for j in range(6):
            if sit[j][i] == 'O':
                ig = img[2]
            if sit[j][i] == 'X':
                ig = img[1]
            if sit[j][i] == ' ':
                ig = img[0]
            button = tk.Button(win,padx=0, pady=0, width=90, height=90, image = ig, background = 'blue') 
            button.grid(column = i, row = j)
            button.bind("<Button-1>",partial(handler,(button.grid_info()['column']),sit ,p1,p2,b))
            b[i].insert(j,button)
    win.mainloop()
dif = 4
def handler(column, sit, p1, p2, b, eve):
    """
    handles the click

    :param column: the column of the button
    :type column: int
    :param sit: the current situation
    :type sit: situation
    :param p1: the first player
    :type p1: player
    :param p2: the second player
    :type p2: player
    :param b: buttons list
    :type b: list
    :param eve: the event
    :type eve: event
    """
    global current
    global dif
    spec = Player.get_spec(current)
    if not puissance.isFinished(sit) :
        if Player.get_name(current) != 'computer' :
            if puissance.isValidMove(sit, column) :
                for i in range(6):
                    if sit[i][column] == ' ':
                        if i == 5:
                            sit[i][column] = Player.get_spec(current)
                        else:
                            continue
                    else:
                        sit[i-1][column] = Player.get_spec(current)
                        break
        current = switch_player(current, p1,p2)
        
        if not puissance.isFinished(sit) and Player.get_name(current) == 'computer' :
            print(dif)
            sit  = AlphaBeta.IA(sit, current, switch_player(current, p1,p2),dif ,puissance)
            if dif < 8 :
                dif += 1
            current = switch_player(current, p1,p2)
    __redraw(sit,b)
    if puissance.isFinished(sit):
        winner = twoplayergame.checkwinner(sit, sit, current, p1, p2, puissance)
        _disable(sit, b)
        msg = finalState(winner)
        msgbox.showinfo("finished",msg)

def __redraw(g,b):
    """
    redraws the new situation after every action
    
    :param g: situation
    :type g: situation
    :param  b: buttons list
    :type b: list
    """
    global img
    for i in range(6):
        for j in range(7):
            button = b[j][i]
            if g[i][j] == 'X':
                new_img = img[1]
                button.config(image=new_img)
            if g[i][j] == 'O':
                new_img = img[2]
                button.config(image=new_img)
def _disable(g,b):
    """
    disables the game board

    :param g: the current situation
    :type g: situation
    :param b: buttons list
    :type b: list
    """
    for i in range(7):
        for j in range(6):
            button = b[i][j]
            button.config(state=tk.DISABLED)
            button.bind("<Button-3>","")
            
create()
            
        
    

