
# -*- coding: utf-8 -*-

"""
 .. topic:: Module ``minmax``

   :author: `Mohamed Amine ELBACHRA`_

   :date:  2015, october

   this module handles

"""

import nim_game , tictactoe, othello
import player as Player

def Mini (situation, comp, player, depth, module):
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
    mini = 100000
    if module.isFinished(situation) or depth == 0:
        return module.evalFunction(situation,comp)
    else:
        situations = module.nextSituations({"":0},situation, player)
        for sit in situations:
            tmp = Maxi (sit[0] ,comp, player, depth-1, module)
            if tmp < mini :
                mini = tmp
    return mini
def Maxi (situation, comp, player, depth, module):
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
    maxi = -100000
    if module.isFinished(situation) or depth == 0 :
        return  module.evalFunction(situation, player)
    else:
        situations = module.nextSituations({"":0}, situation, comp)
        for sit in situations:
            tmp = Mini(sit[0], comp, player, depth-1, module)
            if tmp > maxi :
                maxi = tmp
    return maxi
def IA(situation, comp, player, depth , module):
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
    n = -100000
    module.clean(situation)
    situations = module.nextSituations({"":0}, situation, comp)
    for sit in situations:
        tmp = Mini (sit[0], comp, player, depth-1,module)
        if tmp > n :
            n = tmp
            valueToPlay = sit[1]
    situation = module.changeValue(situation, valueToPlay, comp)  
    return situation

