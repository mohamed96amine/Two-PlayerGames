

# -*- coding: utf-8 -*-
import player as Player

"""
 .. topic:: Module ``abstractgame``

   :author: `Mohamed Amine ELBACHRA`_
   
   :date:  2015, october
   
   This module defines an abstraction for two player games.
   This abstraction is used by :mod:`twoplayersgame` module.
   
   To define a particular game you have to chose how to design a game
   situation and then to create a module that implements the functions in
   this module.  Then, you can replace the ``import abstractgame as
   Game`` in :mod:`twoplayersgame` with ``import
   <your_implementation_module> as Game``.

"""

deplacement = {"T":   [ [-1, 0], [0,-1], [1 , 0], [0 , 1] ] ,
               "C":   [ [1 ,-2], [1, 2], [-1,-2], [-1, 2], [-2, 1], [-2, -1], [2 , 1], [2, -1] ] ,
               "F":   [ [-1,-1], [1, 1], [1 ,-1], [-1, 1] ] ,
               "D":   [ [0 , 1], [1, 1], [1 , 0], [1 ,-1], [0, -1], [-1, -1], [-1, 0], [-1, 1] ] ,
               "R":   [ [0 , 1], [1, 1], [1 , 0], [1 ,-1], [0, -1], [-1, -1], [-1, 0], [-1, 1] ] ,
               "Pb":  [ [-1, 0]],
               "Pn":  [ [1 , 0]],
               "sB":  [ [-1, 0], [-2, 0]],
               "sN":  [ [1 , 0], [2 , 0]]
               }
colors =  {"n" : "Black(n)",
           "b": "White(b)"}

minmaxValues = {"P" : 100,
                "C" : 300,
                "F" : 300,
                "T" : 500,
                "D" : 900,
                "R" : 0
}




def create_game():
    """
    creates the game
    """
    return {'p': 5}

def initSituation(game):
    """
    builds the initial situation for the game.

    :param game: the game for which the initial situation is created
    :type game: game
    :returns: *(situation)* the siutation at the beginning of the game
    """
    sit = [
            ['Tn', 'Cn', 'Fn', 'Dn', 'Rn', 'Fn', 'Cn', 'Tn'],
            ['Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn'],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
            ['Tb', 'Cb', 'Fb', 'Db', 'Rb', 'Fb', 'Cb', 'Tb']
          ]
    return sit

def clean(situation):
    """
    Cleans the board of game

    :param situation: situation
    :type situation: situation
    :return: a clean situation
    """
    return situation

def isFinished(situation):
    """
    tells if the game is finished when in given situation

    :param situation: the tested situation
    :type situation: a game situation
    :returns: *(boolean)* -- True if the given situation ends the game
    """
    return False


def fini(situation, p):
    """
    tells whether the game is finished or not

    :param situation: situation
    :type situation: situation
    :param p: player
    :type p: Player
    :return: boolean
    """
    if Player.get_spec(p) == 'X':
        color = "n"
    else:
        color = "b"
    if isCheck(situation, color):
        checkmate = checkMoves(situation, color )[1]
        if len(checkmate) == 0 :
            return True
    return False



def playerCanPlay(game, situation, player):
    """
    tells whether player can play in given situation

    :param game: the game 
    :type game: game
    :param situation: the situation to display
    :type situation: a game situation
    :param player: the player
    :type player: player
    :returns: *(boolean)* -- True iff player can play in situation
    """
    return True


def nextSituations(game, situation, player):
    """
    returns the list of situations that can be reached from given situation by the player in the game

    :param game: the game
    :type game: a two players game
    :param situation: the current situation
    :type situation: a game situation
    :param player: the current player
    :type player: player
    :returns: *(list<situtation>)* -- the list of situations that can be reached from given situation when player plays one round in the game
    """
    if Player.get_spec(player) == 'X':
        color = "n"
    else:
        color = "b"
    res = []
    values = checkMoves(situation, color)[0]
    sits = checkMoves(situation, color)[1]
    pieces = canPlay(situation, getKing(situation, color)[0], getKing(situation, color)[1])
    for k in range(len(sits)):
        res.append((sits[k], values[k]))
    return res


def getWinner(game, situation, player):
    """
    Gives the winner of the game that end in situation

    :param game: the game 
    :type game: game
    :param situation: the situation which is a final game situation
    :type situation: a game situation
    :param player: the player who should have played if situation was not final (then other player plays previous turn)
    :type player: player
    :returns: *(player)* -- the winner player or None in case of tie game
    :CU: situation is a final situation
    """
    if Player.get_spec(player) == 'X':
        color = "b"
    else:
        color = "n"
    if fini(situation, player):
        return player
    return None
    
def evalFunction(situation, player):
    """
    the evaluation function for the min-max algorithm. It evaluates the given situation,
    the evaluation function increases with the quality of the situation for the player

    :param situation: the current situation
    :type situation: a game situation
    :param player: the current player
    :type player: player
    :returns: *(number)* -- the score of the given situation for the given player.
        The better the situation for the minmax player, the higher the score. The opposite for human player.
    """
    if Player.get_spec(player) == 'X':
        color = "n"
    else:
        color = "b"
    note = 0
    if getWinner("", situation, player) != None:
        if getWinner('', situation, player).get_name() == 'computer':
            return 10000
        else :
            return -10000
    else:
        for i in range(8):
            for j in range(8):
               if situation[i][j][1] == color:
                    note  += - len(canPlay(situation, i, j)) * 10 + minmaxValues[situation[i][j][0]]
        if Player.get_name(player) == "computer":
            return note
        else:
            return - note

def changeValue(situation, valueToPlay, comp):
    """
    plays the value the computer has choosen after the minmax algorithm

    :param situation: situation
    :type situation: situation
    :param valueToPlay: the value
    :type valueToPlay: a tuple
    :param comp: The computer
    :type comp: Player
    """
    if Player.get_spec(comp) == 'X':
        color = "n"
    else:
        color = "b"
    x, y = valueToPlay[0],valueToPlay[1]
    v = validMoves(situation, x, y)
    for i,j in v :
        if simulateCheck(situation, x,y, i,j):
            if (situation[x][y] == 'Pb' and i == 0 ) or (situation[x][y] == 'Pn' and i == 7):
                situation[i][j] = 'D' + situation[x][y][1]
                situation[x][y] = '  '
            else:
                situation[i][j] = situation[x][y]
                situation[x][y] = '  '
            #situation[k[0]][k[1]] = situation[x][y]
            #situation[x] [y] = '  '
            return situation


def displaySituation(situation):
    """
    displays the situation

    :param situation: the situation to display
    :type situation: a game situation
    """
    TopLine = '  +----+----+----+----+----+----+----+----+'
    print('     0    1    2    3    4    5    6    7')
    print(TopLine)
    for x in range(8):
        print(x,end=' ')
        for y in range(8):
            print('| '+(situation[x][y]),end=' ')
        print('|')
        print(TopLine)

def humanPlayerPlays(game, player, situation):
    """
    makes the human player plays for given situation in the game

    :param game: the game 
    :type game: game
    :param player: the human player
    :type player: player
    :param situation: the current situation
    :type situation: a game situation
    :returns: *(game situtation)* -- the game situation reached afte the human player play
    """
    x, y = _input_coords(situation, player)
    i, j = move(situation, x, y)
    if (situation[x][y] == 'Pb'and i == 0) or (situation[x][y] == 'Pn' and i == 7):
        situation[i][j] = 'D' + situation[x][y][1]
        situation[x][y] = '  '
    else:
        situation[i][j] = situation[x][y]
        situation[x][y] = '  '
    return situation
    
def move(situation, x, y):
    """
    moves the pawn to the tile (x, y)

    :param situation: situation
    :param x: x-coordinate
    :param y: y-coordinate
    :return: coords
    """
    coords = input('Move? ')
    coords = coords.split(',')
    try :
        i = int(coords[0])
        j = int(coords[1])
        if isOnBoard(i,j) and (i, j) in canPlay(situation, x, y) and (i, j) in validMoves(situation, x, y):  
            return (i,j)
    except :
        return move(situation, x, y)
    print('illegal play')
    return move(situation, x, y)
    
    
def _input_coords(situation, player):
    """
    takes the input value from the player

    :param situation: situation
    :param player: player
    :return: the value
    """
    if Player.get_spec(player) == 'X':
        color = "n"
    else:
        color = 'b'
    print(Player.get_name(player) + '(' + colors[color]+')'+ " it's your turn")
    coords = input("coords of cell? ")
    coords = coords.split(',')
    x = int(coords[0])
    y = int(coords[1])
    try: 
        if isCheck(situation, situation[x][y][1]):
            l = (checkMoves(situation, situation[x][y][1])[0])
            if isOnBoard(x,y) and situation[x][y][1] == color and  (x,y) in l :
                 return (x,y)
        else:
            l = canPlay(situation,x,y)
            if situation[x][y][1] == color and len(l) != 0:
                return (x,y)
    except:
        return _input_coords(situation,player)
    print('illegal play')
    return _input_coords(situation,player)



def validMoves(situation, x, y):
    """
    returns the valid moves of the (x, y) pawn

    :param situation: situation
    :param x: x-coordinate
    :param y: y-coordinate
    :return: a list of possible moves
    """
    onemove = ['R', 'P', 'C']
    longmove = ['D','F', 'T']
    ennemy = Ennemy(situation[x][y])
    res = []
    if isOnBoard(x, y):
        if situation[x][y] == 'Pb':
            if x == 6:
                dep = deplacement['sB']
            else:
                dep = deplacement['Pb']
            res = res + trap (situation, x, y, ennemy)
        elif situation[x][y] == 'Pn':
            if x == 1 :
                dep = deplacement['sN']
            else:
                dep = deplacement['Pn']
            res = res + trap (situation, x, y, ennemy)
        else:
            dep = deplacement[situation[x][y][0]]
        for xd, yd in dep:
            i, j = x, y
            i += xd
            j += yd
            if isOnBoard(i, j) and situation[x][y][0] in longmove:
                while isOnBoard(i, j) and situation[i][j] == '  ':
                    res.append((i,j))
                    i += xd
                    j += yd
                if isOnBoard(i, j) and situation[i][j][1] == ennemy:
                    res.append((i,j))
            elif isOnBoard(i, j) and situation[x][y][0] in onemove:
                if situation[x][y][0] == 'P' and len(dep) == 2:
                    if situation[x+dep[0][0]][y+dep[0][1]] != '  ':
                        continue
                if situation[i][j] == '  ' :
                    res.append((i,j))
                elif situation[i][j][1] == ennemy :
                    if situation[x][y][0] != 'P':
                        res.append((i,j))
                    else:
                        break
    return res
def isOnBoard(x, y):
    """
    tells whether (x, y) is on board or not

    :param x: x-coordinate
    :param y: y-coordinate
    :return: Boolean
    """
    return 0 <= x < 8 and 0 <= y < 8

def Ennemy(pawn):
    """
    returns the ennemy color

    :param pawn: a pawn
    :type pawn: str
    :return: the ennemy color
    """
    if pawn[1] == "n":
        return 'b'
    else:
        return 'n'
    

def trap (situation, x, y, ennemy):
    """
    returns the possible trap moves of a pawn

    :param situation: situation
    :param x: x-coordinate
    :param y: y-coordinate
    :param ennemy: color of the ennemy
    """
    res = []
    if situation[x][y][1] == 'b':
        dep = [[-1,-1], [-1,1]]
    elif situation[x][y][1] == 'n':
        dep = [[1, -1], [1 ,1]]
    for xd, yd in dep:
        i, j = x, y
        i += xd
        j += yd
        if isOnBoard(i, j) and situation[i][j][1] == ennemy :
            res.append((i,j))
    return res

def getKing(sit, color):
    """
    gets the coords of the <color> King

    :param sit: situation
    :param color: color
    :return: coords(tuple)
    """
    for i in range(8):
        for j in range(8):
            if sit[i][j] == 'R'+color:
                return (i, j)
def isCheck(sit, color):
    """
    tells if the <color> King is in check position

    :param sit: situation
    :param color: color
    :return: Boolean
    """
    ennemy = Ennemy('P'+color)
    King = getKing(sit, color)
    for i in range(8):
        for j in range(8):
            if sit[i][j][1] == ennemy:
                l = validMoves(sit, i, j)
                if King in l :
                    return True       
    return False
def canPlay(sit, x, y):
    """
    returns the pawns that can be moved

    :param sit: situation
    :param x: x-coordinate
    :param y: y-coordinate
    :return: list of pawns
    """
    res = []
    if not isCheck(sit, sit[x][y][1]):
        return validMoves(sit, x, y)
    else:
        for i in range(8):
            for j in range(8):
                if sit[i][j][1] == sit[x][y][1] :
                    v = validMoves(sit, i,j)
                    for k in v:
                        s = initSituation('k')
                        for e in range(8):
                            for d in range(8):
                                s[e][d] = sit[e][d]
                        s[k[0]][k[1]] = s[i][j]
                        s[i][j] = '  '
                        if isCheck(s, sit[x][y][1]) == False:
                            if not (k[0],k[1]) in res:
                                res.append((k[0],k[1]))
    return res
def checkMoves(sit, color):
    """
    returns the possible moves when the <color> King is in Check position

    :param sit: situation
    :param color: color
    :return: list
    """
    res = []
    sits = []
    for i in range(8):
        for j in range(8):
            if sit[i][j][1] == color :
                v = validMoves(sit, i,j)
                for k in v:
                    s = initSituation('k')
                    for e in range(8):
                        for d in range(8):
                            s[e][d] = sit[e][d]
                    s[k[0]][k[1]] = s[i][j]
                    s[i][j] = '  '
                    if isCheck(s, color) == False:
                        if not (i,j) in res :
                            sits.append(s)
                            res.append((i,j))

    return (res, sits)

def simulateCheck(sit, x, y, a, b):
    """
    simulates a situation and tells if it's in check

    :param sit: situation
    :param x: the x-coordinate of the pawn
    :param y: the y-coordinate of the pawn
    :param a: the x-coordinate of the move
    :param b: the y-coordinate of the move
    :return: Boolean
    """
    s = initSituation('')
    for i in range(8):
        for j in range(8):
            s[i][j] = sit[i][j]
    s[a][b] = s[x][y]
    s[x][y] = '  '
    return not isCheck(s, s[a][b][1])


