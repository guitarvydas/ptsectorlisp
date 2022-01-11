# Example 1
![[SectorLisp-trace 1.svg]]

Pre-load NIL and QUOTE (and LAMBDA) into atom memory (`+`).

READ (QUOTE A)
- list creates 2 cons cells at -2 and -4
- A creates an atom at +30

The top level calls `eval(-2, 0)`.  
- -2 is the address of `(... ...)`
- the environment is nothing (0).

`Eval` handles `QUOTE` and returns `Car (Cdr (-2))` => +30 (the atom A).


![[10 Ex1 Intro Screen Recording 2022-01-09 at 5.42.25 PM.mp4]]
![[10a Ex1 Screen Recording 2022-01-09 at 5.44.02 PM.mp4]]

![[10b Ex1 Screen Recording 2022-01-09 at 5.47.00 PM.mp4]]