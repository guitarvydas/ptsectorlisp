Pure functions, as characterize by LAMBDA in Sector Lisp and McCarthy's Lisp 1.5 guarantee that memory (CONS cells) is allocated in a stack-like manner.

All arguments to functions are evaluated before the function, itself, is called.

This approach of using pure functions - without state mutation - works in a stack-like manner, but does not allow the creation of cyclic lists.

We added mutation to languages due to concern for memory conservation.

Memory is abundant today.  The concern for memory conservation is no long valid for most programs.

Languages like Rust would not be needed, except for the cruft we historically built into programming.  

Rust fixes the problem of mutation, but, that problem is accidental complexity due to historical reasons. 

If we fixed the basis of the problem, we would not need Rust.

(I argue that functional programming is a bad idea for modern computing, elsewhere).