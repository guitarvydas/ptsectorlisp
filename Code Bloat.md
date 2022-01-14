I measured that the same program compiled for 8-bit CPUs used less space than for 16-bit CPUs.  

8-bit code was 40% the size of 16-bit code.

One variant of Burroughs machines used Huffman encoding for opcodes.  The minimum opcode was 2 bits.

[[Anatomy of Lisp]]

# Closures
Closures were not necessary until we switched to *compile-everything* thinking (e.g. CL and Scheme and other more popular languages).

# Dynamic Scoping
Early lisps used dynamic scoping (called "specials" in Common Lisp).  

Switching to *compile-everything* forced us to re-think everything in terms of static scoping.  

(Inheritance is a kind of dynamic scoping).

Rhetorical Q: Did code bloat result from switching to *compile-everything* thinking?