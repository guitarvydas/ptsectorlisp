# Declaration Before Use
Declaration Before Use was invented based on early biases:
- multi-pass compilers took a long time to run
- it was considered wasteful to write "extra" code, since disk space was scarce.

Today, the ground rules are different:
- CPUs run much, much faster than in the early days
- Disk Space and memory space is abundant and cheap.

Declaration-before-use guarantees that the least important parts of the program appear earliest in the program.  This impacts understandability of the program - it is not possible to read the first few functions in a program and get a "birds-eye view" of what is going on.

Declaration-before-use encounters accidental complexity, in the form of forward-declarations.

# Declaration Anywhere
There is no need to demand declaration-before-use in programming languages.

Languages could be built with a "declaration anywhere in the program" policy, which could be resolved by multi-pass compilers.

# Declarations
We discovered that the use of declarations reduced the problem of typos.

From this perspective, programmers need to *declare* the existence of names (variables, functions, etc.) that they intend to use, but there is no substantial benefit to declaring such names earlier in the program code.

