% Minimalidad
% Se ganaron un viaje a BRASIL CON TODO PAGADO:

%sorteo_realizado.
%martin; julia; raul; paula :- sorteo_realizado.

%amor; juego :- buenasuerte.
%----------------------------------------------


%reducción 
perro :- not reptil, mamifero, not volador, cuadrupedo.
mamifero.
cuadrupedo.

pato :- not mamifero, not volador. 
%eliminar o simplificar?

%------------------------
%cntrl K (C;U)

%negacion
persona(javier).
%persona(rafa).
%persona(maca).
persona(alonsito).
%persona(consuelo).
menor_de_edad(alonsito).

quiere_carrete(P) :- persona(P).
2{entra_a_la_disco(P): persona(P)}2.

entra_a_la_disco(P) :- quiere_carrete(P), not menor_de_edad(P).


:- entra_a_la_disco(P), persona(P),  menor_de_edad(P).
entra_a_la_disco(P) :- persona(P), not menor_de_edad(P).

#show entra_a_la_disco/1.
%-----------------------------------------------------

% persona(juan).
% persona(luis).
% persona(alo).


% amigo(juan, luis).
% amigo(juan, alo).

% not_superamigo(P) :- persona(P), not amigo(P, Pp), P!=Pp, persona(Pp).
% supeeramigo(P) :-  persona(P), not not_superamigo(P).
%-----------------------------------------------------


%cardinalidad: 
%multi_nacionalidad
pais(chile).
pais(argentina).
pais(kazajstan).
pais(vaticano).

persona(juan).
persona(luis).
persona(alo).


1{nacionalidad(P, X): pais(X)}3 :- persona(P).

%------------------
persona(rorro).
persona(carmela).

ecologista(carmela).

auto(ferrari).
auto(tesla).
auto(citroneta).
auto(tractor).

{tiene(P,A): auto(A)} :- persona(P).

:- tiene(P,A), ecologista(P), A!=tesla.







