casa(h1).
casa(h2).
casa(h3).
casa(h4).

condominio(c1).
condominio(c2).


{predicado(H, C): condominio(C)} :- casa(H).

:- predicado(H, C1), predicado(H, C2), C1 != C2.

#show predicado/2.

