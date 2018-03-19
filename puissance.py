

# -*- coding: utf-8 -*-


"""
 .. topic:: Module ``Puissance4``

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

import player as Player

def create_game(depth = 4):
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
    sit = [[' ' for x in range(7)] for y in range(6) ]
    return sit

def clean(situation):
    """
    cleans the situation

    :param situation: the current situation
    :type situation: a game situation
    """
    return situation

def isFinished(situation):
    """
    tells if the game is finished when in given situation

    :param situation: the tested situation
    :type situation: a game situation
    :returns: *(boolean)* -- True if the given situation ends the game
    """
    for k in range(6):
        for l in range(7):
            if situation[k][l] != ' ':
                if k == 6 and l == 7:
                    return True
            else:
                break
    for i in range(6):
        for j in range(7):
            if situation[i][j] != ' ':
                spec = situation[i][j]
                for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
                    counter = 0
                    x, y = i, j
                    x += xdirection
                    y += ydirection
                    if isOnBoard(x, y) :
                        if situation[x][y] == spec:
                            counter += 1
                            x += xdirection
                            y += ydirection
                            while isOnBoard(x, y) and situation[x][y] == spec:
                                counter +=1
                                x += xdirection
                                y += ydirection
                                if counter == 3 :
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
    sits = []
    spec = Player.get_spec(player)
    for i in range(7):
        if isValidMove(situation, i):
            sit = initSituation(game)
            for x in range(6):
                for y in range(7):
                    sit[x][y] = situation[x][y]
            for k in range(6):
                if sit[k][i] == ' ':
                    if k == 5:
                        sit[k][i] = Player.get_spec(player)
                        sits.append((sit,i))
                    else:
                        continue
                else:
                    sit[k-1][i] = Player.get_spec(player)
                    sits.append((sit,i))
                    break
    return sits
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
    winner = getWinner([], situation, player)
    if winner != None :
        if Player.get_name(player) == Player.get_name(winner) == 'computer':
            return 100000
        elif Player.get_name(player) != 'computer' and Player.get_name(winner) != 'computer':
            return -100000
        else:
            return 1
    counter = note = 0
    spec = Player.get_spec(player)
    for i in range(6):
        for j in range(7):
            if situation[i][j] == Player.get_spec(player):
                for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
                    counter = 0
                    x, y = i, j
                    x += xdirection
                    y += ydirection
                    if isOnBoard(x, y) :
                        if situation[x][y] == ' ':
                            counter += 1
                            x += xdirection
                            y += ydirection
                            while isOnBoard(x, y) and situation[x][y] == " ":
                                counter +=1
                                x += xdirection
                                y += ydirection
                                
                                if counter == 3 :
                                    note = 10000
                                else :
                                    note = -10000
    
    else:
        if Player.get_name(player) == 'computer':
            return note
        elif Player.get_name(player) != 'computer':
            return - note
        
def changeValue(situation, valueToPlay, comp):
    """
    plays the move the computer has chosen
    
    :param situation: the current situation
    :type situation: list
    :param valueToPlay: the value we want play
    :type valueToPlay: int
    :param comp: the computer player
    :type comp: player
    """
    y = valueToPlay
    for i in range(6):
        if situation[i][y] == ' ':
            if i == 5:
                situation[i][y] = Player.get_spec(comp)
            else:
                continue
        else:
            situation[i-1][y] = Player.get_spec(comp)
            break
    return situation

    
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
    for i in range(6):
        for j in range(7):
            if situation[i][j] == spec:
                for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
                    counter = 0
                    x, y = i, j
                    x += xdirection
                    y += ydirection
                    if isOnBoard(x, y) :
                        if situation[x][y] == spec:
                            counter += 1
                            x += xdirection
                            y += ydirection
                            while isOnBoard(x, y) and situation[x][y] == spec:
                                counter +=1
                                x += xdirection
                                y += ydirection
                                if counter == 3 :
                                    return player
    return None


def displaySituation(situation):
    """
    displays the situation

    :param situation: the situation to display
    :type situation: a game situation
    """
    TopLine = '  +---+---+---+---+---+---+---+'
    print('    0   1   2   3   4   5   6')
    print(TopLine)
    for x in range(6):
        print(x,end=' ')
        for y in range(7):
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
    y = _input_coords(situation, player)
    for i in range(6):
        if situation[i][y] == ' ':
            if i == 5:
                situation[i][y] = Player.get_spec(player)
            else:
                continue
        else:
            situation[i-1][y] = Player.get_spec(player)
            break
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
    coord = input("Enter number of a  column ? ")
    try :
        y = int(coord)
        if isValidMove(situation , y):  
            return (y)
    except :
        return _input_coords(situation,player)
    print('illegal play')
    return _input_coords(situation,player)

def isOnBoard(x,y):
    """
    tells whether a point is on board
    
    :param x: the x-coordinate of the point
    :type x: int
    :param y: the y-coordinate of the point
    :type y: int
    """
    return 0 <= x <= 5 and 0 <= y <= 6

def isValidMove(situation, y):
    """
    
    :param situation: the current situation
    :type situation: list
    :param y: the column
    :param y: int
    """
    c = 0
    if isOnBoard(0, y):
        for i in range(6):
            if situation[i][y] == ' ':
                c += 1
    return c >= 1


