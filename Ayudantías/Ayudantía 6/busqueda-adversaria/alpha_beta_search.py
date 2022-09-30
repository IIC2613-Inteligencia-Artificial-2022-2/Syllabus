""" Alpha-beta search implementation """
from math import inf


def alpha_beta_search(game, state):
    """Finds optimal move using minimax value. Optimizes search with alpha-beta prunning"""
    player = game.to_move(state)
    if player == "x":
        value, move = max_value(game, state, -inf, inf)
    elif player == "o":
        value, move = min_value(game, state, -inf, inf)
    return move


def max_value(game, state, alpha, beta):
    if game.is_terminal(state):
        return (game.utility(state), None)
    value = -inf
    move = None
    for action in game.actions(state):
        value_2, action_2 = min_value(game, game.result(state, action), alpha, beta)
        if value_2 > value:
            value, move = (value_2, action)
            alpha = max(alpha, value)
        if value >= beta:
            return value, move
    return value, move


def min_value(game, state, alpha, beta):
    if game.is_terminal(state):
        return (game.utility(state), None)
    value = inf
    move = None
    for action in game.actions(state):
        value_2, action_2 = max_value(game, game.result(state, action), alpha, beta)
        if value_2 < value:
            value, move = (value_2, action)
            beta = min(beta, value)
        if value <= alpha:
            return value, move
    return value, move
