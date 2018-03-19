# -*- coding: utf-8 -*-


"""
 .. topic:: Module ``TicTacToe``

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



import player as Player

def create_game(depth = 12):
    """
    initiates the game
    
    :param depth: the depth of the recursive minmax program (default = 12)
    :type depth: int
    """
    return {"p": depth}

def initSituation(game):
    """
    builds the initial situation for the game. 

    :param game: the game for which the initial situation is created
    :type game: game
    :returns: *(situation)* the siutation at the beginning of the game
    """
   
    situation = [ ['' for x in range (3) ] for y in range (3) ]
    return situation
def clean(situation):
    """
    cleans the situation
    
    :param situation: situation: the current situation
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
    booleen = True
    for i in range(3):
        if situation[i][0] == situation[i][1] == situation[i][2] != '' :
            return True
        for j in range(3):
            if i == 0:
                if situation[i][j] == situation[i+1][j] == situation[i+2][j] != '' :
                    return True
                if j == 0 or j == 2 :
                    if situation[i][j] == situation[i+1][abs(j-1)] == situation[i+2][abs(j-2)] != '':
                        return True
            if situation[i][j] == '':
                booleen = False
    if booleen == True:
        return True
    else:
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
    spec = Player.get_spec(player)
    sits = []
    for i in range(3):
        for j in range(3):
            if situation[i][j] == '':
                sit = initSituation([])
                for x in range(3):
                    for y in range(3):
                        sit[x][y]= situation[x][y]
                sit[i][j] = spec
                sits.append((sit,(i,j)))
    return sits
    
def changeValue(situation , valueToPlay, player):
    """
    plays the move the computer has chosen
    
    :param situation: the current situation
    :type situation: list
    :param valueToPlay: the value we want play
    :type valueToPlay: int
    :param comp: the computer player
    :type comp: player
    """
    situation[valueToPlay[0]][valueToPlay[1]] = Player.get_spec(player)
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
    for i in range(len(situation)):
        if situation[i][0] == situation[i][1] == situation[i][2] == spec :
            return player
        if i == 0:
            for j in range(3):
                if situation[i][j] == situation[i+1][j] == situation[i+2][j] == spec :
                    return player
                if j == 0 or j == 2 :
                    if situation[i][j] == situation[i+1][abs(j-1)] == situation[i+2][abs(j-2)] == spec :
                        return player
    return None
            


def displaySituation(situation):
    """
    displays the situation

    :param situation: the situation to display
    :type situation: a game situation
    """
    for i in situation :
        print('|',end='')
        for cell in i :
            if cell != '':
                print(cell, end='')
            if cell == '':
                print('_', end="")
            print('|',end='')
        print('\n')
        
def evalFunction(situation, joueur):
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
    number_moves = 0
    for i in range(3):
        for j in range(3):
            if situation[i][j] != '':
                number_moves += 1
    winner = getWinner({"":0},situation, joueur)
    if winner != None:
        if Player.get_name(joueur) == Player.get_name(winner)== 'computer' :
            return 1000-number_moves
        if Player.get_name(joueur) != 'computer' and Player.get_name(joueur) == Player.get_name(winner) :
            return -1000 + number_moves
    if winner== None:
        return 0
        
    
def humanPlayerPlays(game, player, situation):
    """
    makes the human player plays for given situation in the game

    :param game: the game 
    :type game: game
    :param player: the human player
    :type player: player
    :param situation: the current situation
    :type situation: a game situation
    :returns: *(game situtation)* -- the game situation reached after the human player play
    """
    game = situation 
    x,y = _input_coords (situation, player)
    situation[x][y] = Player.get_spec(player)
    return situation 
    

    
def _input_coords(game,player):
    """
    manage the interaction with the human player

    :param situation: the current situation
    :type situation: list
    :param player: player
    :type player: player
    """
    print(Player.get_name(player)+'('+Player.get_spec(player)+')'+" it's your turn")
    coords = input("coords of cell? ")
    coords = coords.split(',')
    try :
        x = int(coords[0])
        y = int(coords[1])
        if game[x][y] == '' :  
            return (x,y)
    except :
        return _input_coords(game,player)
    print('illegal play, choose an empty cell')
    return _input_coords(game,player)
