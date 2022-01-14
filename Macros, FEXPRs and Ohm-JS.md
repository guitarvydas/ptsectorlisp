It would be simple to change Sector Lisp to support functions whose arguments are not evaluated.

I call these *FEXPR*s (for historical reasons[^1]).

FEXPRs would give macros-for-free to Sector Lisp.

Yet, such macros would be based only on lisp lists.

Macros could be implemented in a more general manner by pattern-matching characters and rewriting strings.

`Prep`[^2], based on Ohm-JS, is a tool that does character-based pattern-matching and rewriting.  In essence, `prep` provides general macros to *any* programming language.

`Prep` could be used to overlay macros and syntax onto Sector Lisp, instead of relyin on FEXPRs.

[^1] The first Lisp that I built was the [Frits van der Wateren Lisp 1.5](https://github.com/guitarvydas/frits-van-der-wateren-lisp/blob/master/LISP.TXT), and, it tagged functions are being EXPRs and FEXPRs.  I think that early Lisps used the term FEXPR, also.

[^2] [prep](https://github.com/guitarvydas/prep) - documentation and videos to come.