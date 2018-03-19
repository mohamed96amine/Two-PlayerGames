
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
.. topic:: Module ``nim_game``

   :author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

   :date:  2015, october

    This Module handles the two player game logic

"""
import sys, minmax, othello, nim_game, tictactoe, puissance, chess, AlphaBeta
import player as Player

def choose_game():
    """
    takes the input from user

    """
    game = input('choose a game :\n *TicTacToe (1)\n\n *Nim (2)\n\n *Othello (3)\n\n *Puissance4 (4)\n\n *chess (5)')
    if game == '1':
        return tictactoe
    elif game == '2':
        return nim_game
    elif game == '3':
        return othello
    elif game == '4':
        return puissance
    elif game == '5':
        return chess
    else:
        return choose_game()
    

def switch_player(current, player1, player2):
    """
    switches the current player to the other player .
    
    :param current: the current player
    :type current: player
    :param player1: the first player
    :type player1: player
    :param player2: the second player player
    :type player2: player
    """
    if current == player1:
        return player2
    else:
        return player1
def play(name1, name2 = 'computer'):
    """
    runs the game
    
    :param name1: name of the first player
    :param name2: name of the second player (default = computer)
    :type name1: str
    :type name2: str
    """
    module = choose_game()
    one = Player.new_player (name1,'X')
    two = Player.new_player (name2,'O')
    game = module.create_game()
    sit = module.initSituation(game)
    current = goesFirst(one, two)
    while not module.isFinished (sit):
        if module.playerCanPlay (game, sit, current):
            if Player.get_name(current) == 'computer':
                module.displaySituation(sit)
                sit = AlphaBeta.IA(sit, two, one, game['p'], module)
            if Player.get_name(current) != 'computer':
                module.displaySituation(sit)
                sit = module.humanPlayerPlays(game, current, sit)
        current = switch_player(current, one,two)
    winner = checkwinner (game, sit, current, one, two, module)
    module.displaySituation (sit)
    print(finalState(winner))


def checkwinner (game, sit, current,one, two, g):
    """
    checks the winner of the game
    
    :param game: the game
    :type game: game
    :param sit: the final situation
    :type sit: situation 
    :param current: the current player
    :type current: player
    :param one: the first player
    :type one: player
    :param two: the second player
    :type two: the second player
    """
    if g.getWinner(game, sit, current) == current:
        return current
    elif g.getWinner(game, sit, switch_player(current, one,two)) == switch_player(current, one,two) :
        return switch_player(current, one, two)
    else:
        return None
    
def goesFirst(player1, player2):
    """
    asks the player who starts the game
    
    :param player1: the first player
    :type player1: player
    :param player2: the second player
    :type player2: player
    :return: the player who starts
    """
    first = input('who goes first ? '+ Player.get_name (player1) +' or '+Player.get_name (player2)+' ?')
    if first == Player.get_name(player2) :
        return player2
    elif first == Player.get_name(player1) :
        return player1
    else:
        return goesFirst(player1, player2)
    
def finalState (winner):
    """
    returns the final message after a finished game , and tells whether the player wins , or a tie game
    
    :param winner: possible winner
    :type winner: player
    :return: return a message of the final state of the game
    :rtype: str
    """
    if winner == None:
        return "Tie Game"
    elif Player.get_name(winner) == 'computer':
        return "Sorry, you lose!"
    else:
        return "Congrats " + Player.get_name (winner) + " you won!"


if __name__ == '__main__':
    name1 = sys.argv[1]#
    if len(sys.argv) == 3 :
        name2 = sys.argv[2]
        play(name1, name2)
    else:
        play(name1)
    
