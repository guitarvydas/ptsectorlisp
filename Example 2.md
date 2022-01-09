Trace evaluation of `((lambda (X) X) (QUOTE A))`.

# Input

![[SectorLisp-example 2 input.svg]]

# READ
READ structure `((LAMBDA (X) X) (QUOTE A))`.

![[SectorLisp-Reading of trace 2.svg]]


READ flattened into memory:
![[SectorLisp-flattened read example 2.svg]]

[N.B. the above was manually drawn and probably contains inaccuracies (e.g. ordering of CONS cells).]
# Trace
... only the first few steps ...

![[SectorLisp-trace -partial- example 2.svg]]