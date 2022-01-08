# URL
[sector lisp](https://justine.lol/sectorlisp2/#listing)
# Overview
`M` is memory
	- can be thought of as an array of `Cons` cells
	- each `Cons` Cell has 2 slots `car`, `cdr`

`Cons` cells are kept on a stack.

`Strings` are kept in memory, zero-terminated, using cells.  The `Car` contains one (two? more?) characters, the `Cdr` points to the next Cons Cell in the string.

[The "pointer" is an index into Memory].

Cons cells grow in address away from 0000, Strings (atoms) grow away from 0000 in the other direction.

`Cons` Cells are allocated on a stack - not a heap.  If Lists are guaranteed to be acyclic and no mutation is allowed, then a strict stack-based allocation/deallocation scheme can be used.  Results of evaluation are copied and the rest of the cells are de-allocated.  The stack pointer is bumped to preserve results and to make them available to the caller.

This scheme does not result in defragmented memory.
# Lessons
8-bit (byte) addresses are more efficient (space-wise) than 16-bit addresses, than 32-bit addresses than 64-bit addresses.

8-bit FP can be fitted into <512 bytes.  Conclusion: use full-blown 64-bit workstation to develop program, then apply Production Engineering, e.g. re-cast solution as 8-bit (or 16-bit, etc.).

Bytecodes are based on 8-bit bytes for a reason.

Use PEG to write an SCN.  Develop in 64-bit, revamp SCN back-end to emit 8-bit code during Production Engineering.

"Compile away" 64-bit inefficiency during Production Engineering by tinkering with back-end of SCN.

Two languages (at least) for every project
1. Development language
2. Production Engineering language.

# Minimal Lisp
A function is a list of 3 items `(lamdba (x y) body)`
1. the keyword `lambda`
2. the formal parameters as a list
3. the body of the function.

If `f = (lambda (x y) body)`, we can
- get the formals as `(car (cdr f))`
- get the body as `(car (cdr (cdr f))`


The 6 basic functions of lisp are:
- Eval (e, env)
- Apply (f, e, env)
- Evcon (list, env)
- Evlis (list, env)
- Assoc (e, env)
- Pairlis (name-list, value-list, env).

`Env` is a table that maps names to values.  In Lisp 1.5, `Env` is an `alist`, `((name1 . value1) (name2 . value2) ...)`

`Eval` gets the value of an expression, given an environment.

`Apply` calls a function on an expression, given an environment.

`Evcon` evaluates a list conditionally, e.g. ((e1 . body1) (e2. body2) ...).  It returns the `Eval` of the first body whose condition is non-false.  (False is NIL is 0, everything else isn't false).

`Evlis` evaluates a list by evaluating the first item in the list, then `Evlis`ing the rest of the list.

`Assoc` looks up `e` in the mapping table (`env`).  It returns the value of `e`.

`Pairlis` tacks pairs, (name . value), onto the environment, one pair for each element of e-list.  It does nothing if e is NIL.  It returns the new (/ old) environment. [Assumed[^1] name-list and value-list have exactly the same length.][^2]

[^1]: Error checking omitted to decrease size.  Only pre-checked programs are executed by SectorLisp

[^2]:: Questions to the reader.  If there are fewer names on the list than values, the extra values are ignored.  What happens if there are fewer values than names?  What happens if any name is a list?

`Quote` and `cond` are handled in `Eval` ().  The are "special forms".

`Apply` handles 5 builtin functions and `lambda` forms.  The builtins are 
- `eq`
- `cons`
- `atom`
- `car`
- `cdr`

`Lambda` does not appear explicitly in this code, but, is assumed in the `(f < 0)` case of `apply`.  In this case (i.e. f is a list), `apply` extracts the body of the function (`(car (cdr (cdr f)))`) and extends the environment using `Pairlis`, mapping formals to actual values.  This process of putting name-value pairs onto the environment is call `binding`.

If `f` is an atom (i.e. not a list) but is not one of the builtins, `Apply` assumes that `f` is a bound parameter.  It looks up the value of `f` in the environment, then tries again (applying the value-of-f to e in the same environment).

 ## GC

Stack before evaluation == `A`
Stack after evaluation == `B`


# JS
[scroll down](https://justine.lol/sectorlisp2/lisp.js)
# C
[lisp.c](https://github.com/jart/sectorlisp/blob/main/lisp.c)

commentary
## Begin at Line
- 159

Function `Car(x)` returns the .car slot of x.

Function `Cdr(x)` returns the .cdr slot of x.  The `cdr` is at `x+1` (`+1` must be appropriately scaled).

Function `Cons(car, cdr)`
	- uses global variable `cx`
	- `cx` points to next free location in memory
	- write `Cdr` into memory
	- then, write `Car` into memory
	- increment `cx` by 2 units
	- return `cx`.