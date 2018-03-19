"""
 .. topic:: Module ``AlphaBeta``

   :author: `Mohamed Amine ELBACHRA`_

   :date:  2015, october

   This module defines an abstraction for two player games.
   This abstraction is used by :mod:`AlphaBeta` module.

   a slight derivation of the minmax algorithms

"""


import nim_game , tictactoe, othello, math
import player as Player

alpha = - float("inf")
beta =  float("inf")
def Mini (situation, comp, player, depth, module, alpha, beta):
    """
    returns the lowest score of the possible situations

    :param situation: the possible situation
    :type situation: game situation
    :param comp: the computer player
    :type comp: player
    :param player: the other player
    :type player: player
    :param depth: the depth of the recursive algortihm (can also represent the difficulty of the game)
    :type depth: int
    :param module: the module of the game
    :type module: str
    """
    if module.isFinished(situation) or depth == 0:
        return module.evalFunction(situation,comp)
    else:
        situations = module.nextSituations({"":0},situation, player)
        for sit in situations:
            tmp = Maxi (sit[0] ,comp, player, depth-1, module, alpha, beta)
            if tmp <= alpha :
                return alpha
            if tmp < beta :
                beta = tmp
    return beta
def Maxi (situation, comp, player, depth, module, alpha, beta):
    """
    returns the highest score of the possible situations
    
    :param situation: the possible situation
    :type situation: game situation
    :param comp: the computer player
    :type comp: player
    :param player: the other player
    :type player: player
    :param depth: the depth of the recursive algortihm (can also represent the difficulty of the game)
    :type depth: int
    :param module: the module of the game
    :type module: str
     """
    if module.isFinished(situation) or depth == 0 :
        return  module.evalFunction(situation, player)
    else:
        situations = module.nextSituations({"":0}, situation, comp)
        for sit in situations:
            tmp = Mini(sit[0], comp, player, depth-1, module, alpha, beta)
            if tmp >= beta :
                return beta
            if tmp > alpha:
                alpha = tmp
                
    return alpha
def IA(situation, comp, player, depth , module, alpha = alpha , beta = beta):
    """
    runs the artificial intellegince (the minmax algorithm)
    
    :param situation: the current situation
    :type situation: game situation
    :param comp: the computer player
    :type comp: player
    :param player: the other player
    :type player: player
    :param depth: the depth of the recursive algortihm (can also represent the difficulty of the game)
    :type depth: int
    :param module: the module of the game
    :type module: module
    """
    module.clean(situation)
    if module.isFinished(situation) or depth == 0 :
        return  module.evalFunction(situation, player)
    else:
        situations = module.nextSituations({"":0}, situation, comp)
        for sit in situations:
            tmp = Mini(sit[0], comp, player, depth-1, module, alpha, beta)
            if tmp > alpha :
                alpha = tmp
                valueToPlay = sit[1]
            if tmp >= beta:
                break
    situation = module.changeValue(situation, valueToPlay, comp)
    return situation

