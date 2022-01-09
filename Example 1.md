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