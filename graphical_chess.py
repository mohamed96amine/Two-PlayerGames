# -*- coding: utf-8 -*-

"""
 .. topic:: Module ``Chess``

   :author: `Mohamed Amine ELBACHRA`_

   :date:  2015, october

   this module is an impletation of UI(User interface) of the chess game

"""


import os, ask, twoplayergame, random, time
import tkinter as tk
import player as Player
from functools import partial
from twoplayergame import *
import tkinter.messagebox as msgbox


def create():
    """
    creates the initial situation and draws it
    """
    global img, current, images
    g = chess.create_game()
    sit = chess.initSituation(g)
    if ask.askplayer() == 1:
        p1 = Player.new_player('human', 'O')
        p2 = Player.new_player('computer', 'X')
    else:
        p1 = Player.new_player('player1', 'O')
        p2 = Player.new_player('player2', 'X')
    current = p1
    win = tk.Tk()
    win.title('chess')
    iconpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons")
    img = [tk.PhotoImage(file =os.path.join(iconpath, "Tn.gif")),
           tk.PhotoImage(file =os.path.join(iconpath, "Cn.gif")),
           tk.PhotoImage(file =os.path.join(iconpath, "Fn.gif")),
           tk.PhotoImage(file =os.path.join(iconpath, "Dn.gif")),
           tk.PhotoImage(file =os.path.join(iconpath, "Rn.gif")),
           tk.PhotoImage(file =os.path.join(iconpath, "Tb.gif")),
           tk.PhotoImage(file =os.path.join(iconpath, "Cb.gif")),
           tk.PhotoImage(file =os.path.join(iconpath, "Fb.gif")),
           tk.PhotoImage(file =os.path.join(iconpath, "Db.gif")),
           tk.PhotoImage(file =os.path.join(iconpath, "Rb.gif")),
           tk.PhotoImage(file =os.path.join(iconpath, "Pn.gif")),
           tk.PhotoImage(file =os.path.join(iconpath, "Pb.gif")),
           tk.PhotoImage(file =os.path.join(iconpath, "tap.gif")),
           tk.PhotoImage(file =os.path.join(iconpath, "burlywood.gif"))
            ]
    images = {'Tn' : img[0],'Cn' : img[1],'Fn' : img[2],'Dn' : img[3],'Rn' : img[4],'Tb' : img[5],'Cb' : img[6],
          'Fb' : img[7],'Db' : img[8],'Rb' : img[9],'Pn' : img[10],'Pb' : img[11],}
    b = []
    for i in range(8):
        b.insert(i,[])
        for j in range(8):
            if (i+j)% 2 == 0:
                bg = 'khaki'
            else:
                bg = 'burlyWood'
            if sit[j][i] !='  ':
                button = tk.Button(win, padx=0, pady=0, width=80, height=80, image = images[sit[j][i]], background = bg)
            else:
                button = tk.Button(win, padx=0, pady=0, width=80, height=80, image = img[12], background = bg)
            button.grid(column = i, row = j)
            button.bind("<Button-3>", partial(rightClick, (button.grid_info()['row']), (button.grid_info()['column']), sit, b))
            button.bind("<Button-1>", partial(leftClick, (button.grid_info()['row']), (button.grid_info()['column']), sit, p1, p2, b))
            b[i].insert(j,button)
    win.mainloop()

def rightClick(x, y, sit, b, eve) :
    """
    handles the right click

    :param x: x-coordinate
    :type x: int
    :param y: y-coordinate
    :type y: int
    :param sit: situation
    :type sit: situation
    :param b: list of buttons
    :type b: list
    :param eve: the event
    """
    global res, current
    if Player.get_spec(current) == 'X':
        color = 'n'
    else:
        color = 'b'
    
    try :
        __redraw(sit, b)
        if chess.isCheck(sit, sit[x][y][1]):
            l = chess.checkMoves(sit, sit[x][y][1])[0]
            if sit[x][y][1] == color and  (x, y) in l :
                res = (x, y)
                b[y][x].config (background = 'maroon')
                d = chess.canPlay(sit, x, y)
                v = chess.validMoves(sit, x, y)
                for i,j in v:
                    if (i, j) in d and  chess.simulateCheck(sit, x, y, i, j):
                        b[j][i].config (background = 'maroon')
        else:
            l = chess.canPlay(sit, x, y)
            if sit[x][y][1] == color and len(l) != 0:
                res = (x, y)
                b[y][x].config(background = 'maroon')
                for i,j in l:
                    b[j][i].config(background = 'maroon')
    except :
        pass
    
    
def leftClick(x, y, sit, p1, p2, b, eve):
    """
    handles the left click

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
    try : 
        if (x, y) in chess.canPlay(sit, res[0] ,res[1]) and (x,y) in (chess.validMoves(sit,res[0],res[1])) :
            i , j = res[0],res[1]
            if (sit[i][j] == 'Pb' and x == 0 ) or (sit[i][j] == 'Pn' and x == 7):
                sit[x][y] = 'D' + sit[i][j][1]
                sit[i][j] = '  '
            else:
                sit[x][y] = sit[i][j]
                sit[i][j] = '  '
            current = switch_player(current, p1, p2)
        if chess.isCheck(sit, chess.Ennemy(sit[x][y])):
            msgbox.showinfo("Echec","Echec ! ")
        __redraw(sit, b)
        if chess.fini(sit, current):
            _disable(sit, b)
            loser = checkwinner (sit, sit, current, p1, p2, chess)
            msg = loser + " Sorry you lose!"
            msgbox.showinfo("Checkmate" , "CheckMate! "+msg)
        if Player.get_name(current) == 'computer':
            sit = AlphaBeta.IA(sit, current, switch_player(current, p1,p2), 2, chess)
            current = switch_player(current, p1, p2)
        __redraw(sit, b)
        if chess.fini(sit, current):
            _disable(sit, b)
            loser = checkwinner (sit, sit, current, p1, p2, chess)
            msg = loser + " Sorry you lose!"
            msgbox.showinfo("Checkmate" , "CheckMate! "+msg)
    except:
        pass


def __redraw(g, b):
    """
    redraws the new situation after every action
    
    :param g: situation
    :type g: situation
    :param  b: buttons list
    :type b: list
    """
    global img, images
    for i in range(8):
        for j in range(8):
            button = b[i][j]
            if (i+j)% 2 == 0:
                bg = 'khaki'
            else:
                bg = 'burlyWood'
            if g[j][i] != '  ':
                button.config(image = images[g[j][i]], background = bg)
            else:
                button.config(image = img[12], background = bg)
                
def _disable(g, b):
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

          
create()
            
        
    

