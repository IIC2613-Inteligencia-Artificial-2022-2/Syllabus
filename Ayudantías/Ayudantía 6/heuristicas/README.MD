Este código está basado en el que usaron en clases para correr el puzzle de 8. La idea es que compara una heurística de entrada
contra la suma de distancias manhattan como baseline.

Se corre con el comando ``python test_astar.py``. Además pueden agregar los siguentes parámetros adicionales

* ``-hr heuristic`` donde heristic puede ser zero, euclidean, manh_switch, incorrect o inc_rc. 
* ``-p N`` donde N es la cantidad de puzzles a generar.
* ``-w N`` donde N es el peso que quieren asignar a las heurísticas, por default es 1.

La heurística manh_switch es la suma de distancias manhattan y agrega 1 por cada dos piezas vecinas que se deban intercambiar para llegar a la posición correcta.

La heurística inc_rc entrega la cantidad de filas + columnas incompletas respecto a la solución.
