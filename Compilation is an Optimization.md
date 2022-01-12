Dynamic languages can be type-safe.

Dynamic languages check types at runtime.

Compiled languages re-factor the language so that certain parts (e.g. the type checking) can be done "earlier".

A successful type-checking compiler does *all* of the type checking at "compile time" then produces code for "run time" that contains *no* type checking (an optimization - smaller, faster code).

(What we really want is a knob that we can turn to amp up the optimization.  During development, we leave the knob set at 0, during Production Engineering, we try turning the knob up to 10).