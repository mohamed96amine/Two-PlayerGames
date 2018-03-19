# -*- coding: utf-8 -*-


"""
 .. topic:: Module ``TicTacToe``

   :author: `Mohamed Amine ELBACHRA`_

   :date:  2015, october

   this module is an impletation of UI(User interface) of the tictactoe game

"""


import os, minmax, tictactoe, ask, random, AlphaBeta
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
    sit = tictactoe.create_game()
    g = tictactoe.initSituation(sit)
    if ask.askplayer() == 1:
        p1 = Player.new_player('human','X')
        p2 = Player.new_player('computer','O')
    else:
        p1 = Player.new_player('player1','X')
        p2 = Player.new_player('player2','O')
    p = [p1, p2]
    current = p[random.randint(0,1)]
    if Player.get_name(current) == 'computer':
        g = AlphaBeta.IA(g,current, switch_player(current, p1, p2), 10, tictactoe)
        current = switch_player (current, p1, p2)
    win = tk.Tk()
    win.title('TicTacToe')
    iconpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"icons")
    img = [tk.PhotoImage(file=os.path.join(iconpath,"tap.gif")),tk.PhotoImage(file=os.path.join(iconpath,"X.gif")),tk.PhotoImage(file=os.path.join(iconpath,"O.gif"))]
    b = []
    for i in range(3):
        b.insert(i,[])
        for j in range(3):
            if g[i][j] == 'X':
                ig = img[1]
                button.config(image=ig)
            if g[i][j] == 'O':
                ig = img[2]
            if g[i][j] == '':
                ig = img[0]
            button = tk.Button(win,padx=0,pady=0, width=180, height=180, image=ig, background = 'darkKhaki') 
            button.grid(column = i, row = j)
            button.bind("<Button-1>",partial(handler,(button.grid_info()['row']),(button.grid_info()['column']),g,p1,p2,b))
            b[i].insert(j,button)
    win.mainloop()
    
def _disable(g,b):
    """
    disables the game board

    :param g: the current situation
    :type g: situation
    :param b: buttons list
    :type b: list
    """
    
    for i in range(3):
        for j in range(3):
            button = b[i][j]
            button.config(state=tk.DISABLED)
            button.bind("<Button-3>","") 
def handler(x, y, g, p1, p2, b, eve):
    """
    handles the click

    :param x: x-coordinate
    :param y: y-coordinate
    :param g: situation
    :param p1: player
    :param p2: player
    :param b: list of buttons
    :param eve: the event
    """
    global current
    spec = Player.get_spec(current)
    if g[x][y] == '':
        g[x][y] = spec
        if Player.get_name(current) != 'computer' and Player.get_name(switch_player(current, p1,p2)) == "computer" and not tictactoe.isFinished(g):
            g = minmax.IA(g,switch_player(current, p1,p2), current, 10, tictactoe)
        else:
            current = switch_player(current, p1,p2)
        __redraw(g,b)
    if tictactoe.isFinished(g):
        winner = tictactoe.getWinner(g,g,switch_player(current, p1,p2))
        _disable(g,b)
        msg = finalState(winner)
        msgbox.showinfo("finished",msg)

def __redraw(g,b):
    """
    redraws the new situation after every action
    
    :param g: situation
    :type g: situation
    :param b: buttons list
    :type b: list
    """
    global img
    for i in range(3):
        for j in range(3):
            button = b[j][i]
            if g[i][j] == 'X':
                new_img = img[1]
                button.config(image=new_img)
            if g[i][j] == 'O':
                new_img = img[2]
                button.config(image=new_img)
create()
            
        
    

