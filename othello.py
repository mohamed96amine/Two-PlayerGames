

# -*- coding: utf-8 -*-
import player as Player
"""
 .. topic:: Module ``Othello``

   :author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_
   
   :date:  2015, october
   
   This module defines an abstraction for two player games.
   This abstraction is used by :mod:`othello` module.
   
   To define a particular game you have to chose how to design a game
   situation and then to create a module that implements the functions in
   this module.  Then, you can replace the ``import abstractgame as
   Game`` in :mod:`twoplayersgame` with ``import
   <your_implementation_module> as Game``.

"""

def create_game(depth = 6):
    """
    initiates the game
    
    :param depth: the depth of the recursive minmax program (default = 5)
    :type depth: int
    """
    return {"p": depth}

def initSituation(game):
    """builds the initial situation for the game. 

    :param game: the game for which the initial situation is created
    :type game: game
    :returns: *(situation)* the siutation at the beginning of the game
    """
    situation = [[' ' for x in range(8)] for y in range(8)]
    situation[3][3] = "X"
    situation[3][4] = 'O'
    situation[4][3] = 'O'
    situation[4][4] = 'X'
    return situation 

def isFinished(situation):
    """
    tells if the game is finished when in given situation

    :param situation: the tested situation
    :type situation: a game situation
    :returns: *(boolean)* -- True if the given situation ends the game
    """
    finished = True
    for i in range(8):
        for j in range(8) :
            if situation[i][j] == " ":
                finished = False
                
    return finished

def clean(situation):
    """
    cleans the situation by deleting possible moves
    
    :param situation: the current situation of game
    :type situation: list
    """
    for i in range(8):
        for j in range(8):
            if situation[i][j] == '.':
                situation[i][j] = ' '
    return situation

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
    valid = getValidMoves (situation,player)
    for j in valid:
        i, a = j[0], j[1]
        situation[i][a] = '.'
    return len(valid) != 0

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
    spec = Player.get_spec(player)
    winner = getWinner([], situation, player)
    name = Player.get_name(player)
    edge = corner = compteur = 0
    for i in range(8):
        for j in range(8):
            if isOnCorner(i,j) and situation[i][j] == spec:
                corner += 1
            if situation [i][j] == spec:
                compteur += 1
            if isOnEdge(i, j) and situation[i][j] == spec:
                edge += 1
    if name == 'computer' and winner == player:
        return  1000 + compteur + 6*corner + 2*edge
    if name != 'computer' and winner == player:
        return -1000 - compteur - 6*corner - 2*edge
    if winner == None:
        return 0
    
def changeValue(situation, valueToPlay, comp):
    """
    
    """
    x, y = valueToPlay[0],valueToPlay[1]
    l = (validMoves(situation , comp, x, y))
    for k in l:
        x1, y1 = k[0],k[1]
        situation[x1][y1] = (Player.get_spec(comp))
    situation[x][y] = Player.get_spec(comp)
    
    return situation
def isOnCorner(x, y):
    """
    tells whether a point is on corner
    
    :param x: the x-coordinate of the point
    :type x: int
    :param y: the y-coordinate of the point
    :type y: int
    """
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)
def isOnEdge(x, y):
    """
    tells whether a point is on corner
    
    :param x: the x-coordinate of the point
    :type x: int
    :param y: the y-coordinate of the point
    :type y: int
    """
    return (x == 0 or y == 0) or (x == 7 or y == 0) or (x == 0 or y == 7) or (x == 7 or y == 7)

    
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
    sits = []
    valid = getValidMoves(situation, player)
    for sit in valid :
        s = initSituation(game)
        for i in range(8):
            for j in range(8):
                s[i][j] = situation[i][j]
        x, y = sit[0],sit[1]
        l = (validMoves(s , player, x, y))
        for k in l:
            x1, y1 = k[0],k[1]
            s[x1][y1] = (Player.get_spec(player))
        s[x][y] = Player.get_spec(player)
        sits.append((s,(x,y)))
    return sits
        

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
    spec = Player.get_spec(player)
    compteur = adv = 0
    for i in range(8):
        for j in range(8):
            if situation[i][j] == spec:
                compteur += 1
            if situation[i][j] != spec and situation[i][j] != ' ':
                adv += 1
    if compteur > adv:
        return player
    else:
        return None
            




def displaySituation(situation):
    """
    displays the situation

    :param situation: the situation to display
    :type situation: a game situation
    """
    X = O = 0
    TopLine = '  +---+---+---+---+---+---+---+---+'
    print('    0   1   2   3   4   5   6   7')
    print(TopLine)
    for x in range(8):
        print(x,end=' ')
        for y in range(8):
            if situation[x][y] == 'O':
                O += 1
            if situation[x][y] == 'X':
                X += 1
            print('| '+(situation[y][x]),end=' ')
        print('|')
        print(TopLine)
    print('X : ' + str(X))
    print('O : ' + str(O))
    clean(situation)

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
    x, y = _input_coords (situation, player)
    l = (validMoves(situation , player, x, y))
    for k in l:
        x1, y1 = k[0],k[1]
        situation[x1][y1] = (Player.get_spec(player))
    situation[x][y] = Player.get_spec(player)
    return situation

    
def _input_coords(situation, player):
    """
    manage the interaction with the human player

    :param situation: the current situation
    :type situation: list
    :param player: player
    :type player: player
    """
    print(Player.get_name(player) + '(' + Player.get_spec(player) +')'+ " it's your turn")
    coords = input("coords of cell? ")
    coords = coords.split(',')
    try :
        x = int(coords[0])
        y = int(coords[1])
        if isValidMove(situation, player, x, y):  
            return (x,y)
    except :
        return _input_coords(situation,player)
    print('illegal play')
    return _input_coords(situation,player)


def otherTil(tile):
    """
    gives the opposite of the given tile
    
    :param tile: X or O
    :type tile: str
    """
    if tile == 'X':
        return 'O'
    if tile == 'O':
        return 'X'
    
def isOnBoard(x,y):
    """
    tells whether a point is on board
    
    :param x: the x-coordinate of the point
    :type x: int
    :param y: the y-coordinate of the point
    :type y: int
    """

    return x >= 0 and x <= 7 and y >= 0 and y <= 7


def validMoves(board, player, xstart, ystart):
    """
    gives the tiles to flip 

    :param board: the current situation
    :type board: list
    :param player: the current player
    :type player: player
    :param xstart: the x-coordinate
    :type xstart: int
    :param ystart: the y-coordinate
    :type ystart: int
    """
    tile = Player.get_spec(player)
    otherTile = otherTil(tile)
    tilesToFlip = []
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return tilesToFlip
    board[xstart][ystart] = tile
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        if isOnBoard(x, y) and board[x][y] == otherTile :
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile :
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y):
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x,y])
    board[xstart][ystart] = ' '
    return tilesToFlip
    
def getValidMoves(situation, player):
    """
    gives the valid moves of the player given
    
    :param situation: the current situation :
    :type situation: list
    :param player: the player
    :type player: player
    """
    
    spec = Player.get_spec(player)
    valid = []
    for i in range(8):
        for j in range(8):
            if isValidMove(situation,player,i,j):
                valid.append((i,j))
    return valid

def isValidMove(situation, player,x,y):
    """
    tells if it's a valid move

    :param situation: the current situation
    :type situation: list
    :param player: the player
    :type player: player
    :param x: the x-coordinate of the point
    :type x: int
    :param y: the y-coordinate of the point
    :type y: int
    """
    
    l = validMoves(situation, player, x, y)
    return len(l) != 0

