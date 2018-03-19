#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`player` module

:author: `Mohamed Amine ELBACHRA`_

:date: November, 2015

Module for player representation.



"""




def new_player(name, spec = None):
    """

    creates a new player with 'name' and specification .
    :param name: the name of the player
    :type name: string
    """
    if name == 'computer':
        coef = 1
    else:
        coef = -1
    return {'name': name, 'spec' : spec , 'moves':[], 'coef' : coef}

def get_name (player):
    """

    gives the name of the player .
    :param player:
    :type player: player
    """
    return player['name']

def get_spec (player):
    """

    gives the specification of the player .
    :param player:
    :type player: player
    """
    return player['spec']

def set_name (player, name):
    """

    changes the name of the player.
    :param player:
    :type player: player
    :param name: the new name
    :type name: string
    """
    player['name'] = name


def set_spec (player, spec):
    """

    changes the specification  of the player .
    :param player:
    :type player: player
    """
    player['spec'] = spec
def get_coef (player):
    """

    gives the moves of the player .
    :param player:
    :type player: player
    """
    return player['coef']



