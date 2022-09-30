import numpy as np
x=(1,2,3)
y=(1,2,3)
print(hash(x))
print(hash(y))
print(hash((1,2,3)))

def incorrect_rows(list, x):
    '''retorna la cantidad de filas con algún error'''
    num = 0
    as_matrix = np.array(list, dtype=int).reshape(x, x)
    print(as_matrix)
    for i in range(x):
        for j in range(x):
            if as_matrix[i][j] != i * x +j:
                num += 1
                break
    print(f"la cant de rows malas es {num}")
    return num

incorrect_rows([0,1,3,2,4,5,6,7,8,9,10,11,13,12,15,14], 4)

def manhattan_switch(list,x):
    '''es manhattan, pero además considera un costo extra por 
    tener dos piezas que deben hacer un switch de posiciones'''
    as_matrix = np.array(list, dtype=int).reshape(x, x)
    switches = 0
    for i in range(x):
        for j in range(x):
            try:
                if as_matrix[i+1][j] == i * x + j and as_matrix[i][j] == (i+1) * x + j:
                    switches += 1
            except IndexError:
                pass

            try:
                if as_matrix[i][j+1] == i * x + j and as_matrix[i][j] == i * x + (j+1):
                    print(i,j)
                    switches += 1
            except IndexError:
                pass
    return switches

print(manhattan_switch([0,1,3,2,4,5,6,7,8,9,10,11,13,12,15,14], 4))
puzzle=[[1,2,3], [4,5,6], [7,8,9]]
print([j for sub in puzzle for j in sub])