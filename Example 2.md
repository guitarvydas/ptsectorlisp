Trace evaluation of `((lambda (X) X) (QUOTE A))`.

# Input

![[SectorLisp-example 2 input.svg]]
![[11a Ex2 Intro Screen Recording 2022-01-09 at 5.48.21 PM.mp4]]

# READ
READ structure `((LAMBDA (X) X) (QUOTE A))`.

![[SectorLisp-Reading of trace 2.svg]]

![[11b Read Structured Screen Recording 2022-01-09 at 5.54.17 PM.mp4]]

READ flattened into memory:
![[SectorLisp-flattened read example 2.svg]]

[N.B. the above was manually drawn and probably contains inaccuracies (e.g. ordering of CONS cells).]

![[11c Read Flattened Screen Recording 2022-01-09 at 5.56.11 PM.mp4]]
# Trace
... only the first few steps ...

![[SectorLisp-trace -partial- example 2.svg]]

![[11d Ex2 Trace Screen Recording 2022-01-09 at 5.57.19 PM.mp4]]

# Manual Trace
```
((lambda (x) x) (quote A))
```
eval calls evlis ->
```
(A)
```
eval calls apply ->
```
(apply (lambda (x) x) (A))
```
Apply call:
```
f = (lambda (x) x)
x = (A)
a = ()
```
Apply builds up alist, then calls Eval:
```
e = (lambda (x) x)
a = ((x.A))
```
Apply returns
```
A
```
Eval returns
```
A
```
