Early Lisp had the concept of 
FEXPRs <-- change EVLIS to NOT eval args
=> programs call EVAL explicitly
=> Macros for free

FvdW[^1] Lisp had 2 kinds of functions:
EXPR - APPLY calls EVLIS <= evals args
FEXPR - APPLY calls modified evlis <= does not eval args

idea: LAMBDA and FLAMBDA in SL[^2]?

"don't use EVAL" is the same as "don't execute arbitrary input from arbitrary users"

yet, compiler == EVAL

[^1]: FvdW Lisp == abbreviation for Frits van der Wateren Lisp (1.5) for MC6800 - source code (by permission) at [FvdW Lisp 1.5](https://github.com/guitarvydas/frits-van-der-wateren-lisp/blob/master/LISP.TXT) and [scan](https://github.com/guitarvydas/frits-van-der-wateren-lisp)
[^2]: SL == abbreviation for "Sector Lisp"

FEXPRs were shunned because they were impossible to generalize and to compile, but, now same  is true of Python
