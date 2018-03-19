# -*- coding: utf-8 -*-


"""
 .. topic:: Module ``Othello``

   :author: `Mohamed Amine ELBACHRA`_

   :date:  2015, october

   this module is an impletation of UI(User Interface) of the reversi(othello) game

"""

import os, ask, minmax, othello, random, AlphaBeta
import tkinter as tk
import player as Player
import tkinter.messagebox as msgbox
from functools import partial
from twoplayergame import *


def create():
    """
    creates the initial situation and draws it
    """
    sit = othello.create_game()
    g = othello.initSituation(sit)
    if ask.askplayer() == 1:
        p1 = Player.new_player('human','X')
        p2 = Player.new_player('computer','O')
        dif = ask.askdif()
    else:
        p1 = Player.new_player('player1','X')
        p2 = Player.new_player('player2','O')
        dif = 0
    p = [p1, p2]
    global img
    global current
    current = p[random.randint(0,1)]
    if Player.get_name(current) == 'computer' and othello.playerCanPlay(g, g, current):
            g = othello.clean(g)
            g = AlphaBeta.IA(g,current,switch_player(current, p1,p2),dif,othello)
            current = switch_player(current, p1,p2)
    win = tk.Tk()
    win.title('Othello')
    iconpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"icons")
    img = [tk.PhotoImage(file=os.path.join(iconpath,"tap.gif")),tk.PhotoImage(file=os.path.join(iconpath,"noir.gif")),
        tk.PhotoImage(file=os.path.join(iconpath,"blanc.gif")),tk.PhotoImage(file=os.path.join(iconpath,"possible.gif"))]
    b = []
    for i in range(8):
        b.insert(i,[])
        for j in range(8):
            if g[i][j] == "O":
                ig = img[2]
            if g[i][j] == "X":
                ig = img[1]
            if g[i][j] == " ":
                ig = img[0]
            button = tk.Button(win,padx=0,pady=0, width=71, height= 71, image= ig, background = 'green' ) 
            button.grid(column = i, row = j)
            button.bind("<Button-1>",partial(handler,(button.grid_info()['row']), (button.grid_info()['column']), g, p1, p2, b, dif))
            b[i].insert(j,button)
    hints(g,b)   
    __redraw(g,b)
    othello.clean(g)
    win.mainloop()
def _disable(g,b):
    """
    disables the game board

    :param g: the current situation
    :type g: situation
    :param b: buttons list
    :type b: list
    """
    for i in range(8):
        for j in range(8):
            button = b[i][j]
            button.config(state=tk.DISABLED)
            button.bind("<Button-3>","")

            
def handler(x, y, g, p1, p2, b, dif, eve):
    """
    handles player's clicks and manage turns of the players
    
    :param x: the x-coordinate of the move
    :type x: int
    :param y: the y-coordinate of the move
    :type y: int
    :param g: the current situation
    :type g: situation
    :param p1: the first player
    :type p1: player
    :param p2: the second player
    :type p2: player
    :param b: buttons list
    :type b: list
    :param dif: the difficulty of the game(the depth of the IA recursivity)
    :type dif: int
    :param eve: the event
    :type eve: event
    """
    global current
    if not othello.isFinished(g):
        if Player.get_name(current) != 'computer' and othello.playerCanPlay(g, g, current):
            g = othello.clean(g)
            if othello.isValidMove(g, current, x, y) :
                valid = (othello.validMoves(g , current, x, y))
                for k in valid:
                    x1, y1 = k[0],k[1]
                    g[x1][y1] = (Player.get_spec(current))
                g[x][y] = Player.get_spec(current)
                current = switch_player(current, p1,p2)
        elif not othello.playerCanPlay(g, g, current):
            current = switch_player(current, p1,p2)
        if Player.get_name(current) == 'computer' and othello.playerCanPlay(g, g, current):
            g = othello.clean(g)
            g = AlphaBeta.IA(g, current, switch_player(current, p1,p2), dif, othello)
            current = switch_player(current, p1,p2)
    hints(g,b)   
    __redraw(g,b)
    othello.clean(g)
    if othello.isFinished(g):
        winner = checkwinner (g, g, current, p1, p2, othello)
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
    for i in range(8):
        for j in range(8):
            button = b[j][i]
            if g[i][j] == 'X':
                new_img = img[1]
                button.config(image=new_img)
            if g[i][j] == 'O':
                new_img = img[2]
                button.config(image=new_img)
            if g[i][j] == ' ':
                new_img = img[0]
                button.config(image = new_img)
            if g[i][j] == '.':
                new_img = img[3]
                button.config(image = new_img)

    return g 
def hints(g, b):
    """
    show hints for the current player
    
    :param g: situation
    :type g: situation
    :param  b: buttons list
    :type b: list
    """
    global current
    valid = othello.getValidMoves (g,current)
    for j in valid:
        i, a = j[0], j[1]
        g[i][a] = '.'
    return g

create()
            
        
    

