# SectorLisp
- a lisp that fits in less than 512 bytes (a disk sector)
- [sector lisp](https://justine.lol/sectorlisp2/#listing)

![[1 Screen Recording 2022-01-09 at 4.29.17 PM.mp4]]


![[2 Screen Recording 2022-01-09 at 4.30.36 PM.mp4]]

# Overview
![[3 Overview Screen Recording 2022-01-09 at 4.31.50 PM.mp4]]
## Memory
`M` is memory
	- can be thought of as an array of `Cons` cells
	- each `Cons` Cell has 2 slots `car`, `cdr`

![[4 Memory Screen Recording 2022-01-09 at 4.36.15 PM.mp4]]

## Cons Cells
`Cons` cells are kept on a stack.

`Cons` <- *CONStruct*

![[5 Cons Screen Recording 2022-01-09 at 4.37.47 PM.mp4]]

## Strings
`Strings` are kept in memory, zero-terminated, using cells.  The `Car` contains one (two? more?) characters, the `Cdr` points to the next Cons Cell in the string.

[The "pointer"/"address" is an index into Memory].

![[6a Strings Screen Recording 2022-01-09 at 4.39.14 PM.mp4]]
![[6b Strings Screen Recording 2022-01-09 at 4.40.46 PM.mp4]]
## Memory Allocation
Cons cells grow in address away from 0000, Strings (atoms) grow away from 0000 in the other direction.

`Cons` Cells are allocated on a stack - not a heap.  If Lists are guaranteed to be acyclic and no mutation is allowed, then a strict stack-based allocation/deallocation scheme can be used.  Results of evaluation are copied and the rest of the cells are de-allocated.  The stack pointer is bumped to preserve results and to make them available to the caller.

This scheme does not result in defragmented memory.

![[7 Allocation Screen Recording 2022-01-09 at 4.44.04 PM.mp4]]
# Lessons
8-bit (byte) addresses are more efficient (space-wise) than 16-bit addresses, than 32-bit addresses than 64-bit addresses.

![[8a Lessons Screen Recording 2022-01-09 at 4.46.28 PM.mp4]]
8-bit FP (Functional Programming) can be fitted into <512 bytes.  Conclusion: use full-blown 64-bit workstation to develop program, then apply Production Engineering, e.g. re-cast solution as 8-bit (or 16-bit, etc.).

![[8b Screen Recording 2022-01-09 at 4.59.25 PM.mp4]]

Bytecodes are based on 8-bit bytes for a reason.

![[8c Screen Recording 2022-01-09 at 5.02.18 PM.mp4]]


Use PEG to write an SCN.  Develop in 64-bit, revamp SCN back-end to emit 8-bit code during Production Engineering.

"Compile away" 64-bit inefficiency during Production Engineering by tinkering with back-end of SCN.

Two languages (at least) for every project (using the same top-level source code)
1. Development language
2. Production Engineering language.

![[8d Screen Recording 2022-01-09 at 5.03.26 PM.mp4]]



# Minimal Lisp

![[9a Minimal Lisp Intro Screen Recording 2022-01-09 at 5.17.55 PM.mp4]]

## A Function as a List
A function is a list of 3 items `(lamdba (x y) body)`
1. the keyword `lambda`
2. the formal parameters as a list
3. the body of the function.

![[9b Function as List Screen Recording 2022-01-09 at 5.18.35 PM.mp4]]

## Function Formals and Body

If `f = (lambda (x y) body)`, we can
- get the formals as `(car (cdr f))`
- get the body as `(car (cdr (cdr f))`

![[9c Function Formals Screen Recording 2022-01-09 at 5.19.11 PM.mp4]]


## 6 Basic Functions of Lisp 1.5
The 6 basic functions of lisp are:
- Eval (e, env)
- Apply (f, e, env)
- Evcon (list, env)
- Evlis (list, env)
- Assoc (e, env)
- Pairlis (name-list, value-list, env).

![[9d 6 Basic Functions Intro Screen Recording 2022-01-09 at 5.20.18 PM.mp4]]

### Environment
`Env` is a table that maps names to values.  In Lisp 1.5, `Env` is an `alist`, `((name1 . value1) (name2 . value2) ...)`

![[9e Environment Screen Recording 2022-01-09 at 5.21.22 PM.mp4]]



### Eval
`Eval` gets the value of an expression, given an environment.

### Apply
`Apply` calls a function on an expression, given an environment.

![[9f Eval Apply Screen Recording 2022-01-09 at 5.24.05 PM.mp4]]

### Evcon
`Evcon` evaluates a list conditionally, e.g. ((e1 . body1) (e2 . body2) ...).  It returns the `Eval` of the first body whose condition is non-false.  (False is NIL is 0, everything else isn't false).

### Evlis
`Evlis` creates a list of values that will be bound to the formals of a LAMBDA.

`Evlis` evaluates a list by evaluating the first item in the list, then `Evlis`ing the rest of the list.

![[9g Evcon Evlis Screen Recording 2022-01-09 at 5.25.09 PM.mp4]]
### Assoc
`Assoc` looks up `e` in the mapping table (`env`).  It returns the value of `e`.

### Pairlis
`Pairlis` tacks pairs, (name . value), onto the environment, one pair for each element of e-list.  It does nothing if e is NIL.  It returns the new (/ old) environment. [Assumed[^1] name-list and value-list have exactly the same length.][^2]

[^1]: Error checking omitted to decrease size.  Only pre-checked programs are executed by SectorLisp

[^2]:: Questions to the reader.  If there are fewer names on the list than values, the extra values are ignored.  What happens if there are fewer values than names?  What happens if any name is a list?


![[9h Assoc Pairlis Screen Recording 2022-01-09 at 5.27.07 PM.mp4]]
### Special Forms in Eval
`Quote` and `cond` are handled in `Eval` ().  The are "special forms".

![[9i Eval Special Forms Screen Recording 2022-01-09 at 5.28.55 PM.mp4]]

### Builtin Functions in Apply
`Apply` handles 5 builtin functions and `lambda` forms.  The builtins are 
- `eq`
- `cons`
- `atom`
- `car`
- `cdr`

![[9j Apply Builtins Screen Recording 2022-01-09 at 5.29.34 PM.mp4]]

### Lambda
`Lambda` does not appear explicitly in this code, but, is assumed in the `(f < 0)` case of `apply`.  In this case (i.e. f is a list), `apply` extracts the body of the function (`(car (cdr (cdr f)))`) and extends the environment using `Pairlis`, mapping formals to actual values.  This process of putting name-value pairs onto the environment is call `binding`.

If `f` is an atom (i.e. not a list) but is not one of the builtins, `Apply` assumes that `f` is a bound parameter.  It looks up the value of `f` in the environment, then tries again (applying the value-of-f to e in the same environment).

![[9k Lambda Screen Recording 2022-01-09 at 5.31.28 PM.mp4]]

# Examples
## Example 1
(QUOTE A)
[[Example 1]]

## Example 2
((LAMBDA (X) X) (QUOTE A))
[[Example 2]]

# Full Video

# Errata
Evcon should show `((e1 . body1) (e2 . body2) ...)`.  Dots must have spaces around them.  In the video, I show `e2.` which should be `e2 .`.

The addresses in the example 2 video are incorrect - they have been corrected in sectorlisp.drawio.  Notably, Eval should be called with -14, not -16.


# Garbage Collection
[[Garbage Collection]]
