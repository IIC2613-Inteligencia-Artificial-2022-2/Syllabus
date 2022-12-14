import sys
import random
import copy
import numpy as np


class Puzzle:
    def __init__(self, board=None, blank=-1):
        if not board:
            self.x = 3
            self.size = 9
            self.board = [i for i in range(0, self.size)]
            self.blank = 0
        else:
            self.board = board
            if len(self.board) == 9:
                self.x = 3
                self.size = 9
            elif len(self.board) == 16:
                self.x = 4
                self.size = 16
            else:
                print('puzzle size not supported')
                sys.exit(1)
            if blank == -1:
                self.blank = board.index(0)
        self.goal = list(range(0, self.size))

    def set_heuristic(self, heur='incorrect'):
        if heur == 'incorrect':
            Puzzle.heuristic = Puzzle.incorrect_tiles
        elif heur == 'manhattan':
            Puzzle.heuristic = Puzzle.manhattan
        elif heur == 'zero':
            Puzzle.heuristic = Puzzle.zero_heuristic
        elif heur == 'euclidean':
            Puzzle.heuristic = Puzzle.euclidean
        elif heur == "inc_rc":
            Puzzle.heuristic = Puzzle.incomplete_rc
        elif heur == "manh_switch":
            Puzzle.heuristic = Puzzle.manhattan_switch
        else:
            print('Unsupported heuristic')
            sys.exit(1)

    def __hash__(self):
        return hash(tuple(self.board))

    def __eq__(self, other):
        return self.board == other.board

    def __repr__(self):
        def tostr(d):
            if d > 0:
                return "%2d" % (d)
            else:
                return "  "

        s = '\n'
        for i in range(0, self.x):
            s += "|"
            s += "|".join([tostr(d) for d in self.board[i*self.x:i*self.x+self.x]])
            s += "|\n"
        return s

    def zero_heuristic(self):
        return 0

    def incorrect_tiles(self):
        '''
            retorna el numero de piezas que no estan en la posicion correcta
        '''
        num = 0
        for i in range(0, self.size):
            if self.board[i] == 0:
                continue
            else:
                if self.board[i] != i:
                    num += 1
        return num

    def manhattan(self):
        '''
            retorna la suma de distancias manhattan de cada pieza a su
            posicion final
        '''
        num = 0
        for i in range(0, self.size):
            if self.board[i] == 0:
                continue
            else:
                num += abs(i % self.x - self.board[i] % self.x)
                num += abs(i // self.x - self.board[i] // self.x)
        return num

    def euclidean(self):
        '''retorna la suma de distancias euclideanas de cada pieza a su
        posici??n final'''
        num = 0
        for i in range(0, self.size):
            if self.board[i] == 0:
                continue
            else:
                x_dist = abs(i % self.x - self.board[i] % self.x)
                y_dist = abs(i // self.x - self.board[i] // self.x)
                num += (x_dist**2 + y_dist**2)**(1/2)
        return num
    
    def incomplete_rc(self):
        '''retorna la cantidad de filas + columnas incompletas'''
        num = 0
        as_matrix = np.array(self.board, dtype=int).reshape(self.x, self.x)

        for i in range(self.x):
            for j in range(self.x):
                if as_matrix[i][j] != i * self.x + j:
                    num += 1
                    break

        for j in range(self.x):
            for i in range(self.x):
                if as_matrix[i][j] != i * self.x + j:
                    num += 1
                    break
        return num

    def manhattan_switch(self):
        '''es manhattan, pero adem??s considera un costo extra por 
        tener dos piezas que deben hacer un switch de posiciones'''
        num = self.manhattan()
        as_matrix = np.array(self.board, dtype=int).reshape(self.x, self.x)
        switches = 0
        for i in range(self.x):
            for j in range(self.x):
                if as_matrix[i][j] == 0:
                    continue
                try:
                    if as_matrix[i+1][j] == i * self.x + j and as_matrix[i][j] == (i+1) * self.x + j and as_matrix[i+1][j] != 0:
                        switches += 1
                except IndexError:
                    pass

                try:
                    if as_matrix[i][j+1] == i * self.x + j and as_matrix[i][j] == i * self.x + (j+1) and as_matrix[i][j+1] != 0:
                        switches += 1
                except IndexError:
                    pass
        return num + switches

    def successors(self):
        '''
            Crea una lista de tuplas de la forma (estado, accion, costo)
            donde estado es el estado sucesor de self que se genera al ejecutar
            accion (un string) y costo (un numero real) es el costo de accion
        '''
        def create_child(newblank):
            child = copy.deepcopy(self)
            child.blank = newblank
            child.board[child.blank] = 0
            child.board[self.blank] = self.board[newblank]
            return child

        succ = []
        if self.blank > self.x - 1:
            c = create_child(self.blank-self.x)
            succ.append((c, 'up', 1))
        if self.blank % self.x > 0:
            c = create_child(self.blank-1)
            succ.append((c, 'left', 1))
        if self.blank % self.x < self.x - 1:
            c = create_child(self.blank+1)
            succ.append((c, 'right', 1))
        if self.blank < self.size - self.x:
            c = create_child(self.blank+self.x)
            succ.append((c, 'down', 1))
        return succ

    def is_goal(self):
        return self.board == self.goal

    def random_walk(self, steps):
        state = self
        seen = [self]
        for i in range(0, steps):
            state = random.choice(state.successors())[0]
            while state in seen:
                state = random.choice(state.successors())[0]
            seen.append(state)
        return state
