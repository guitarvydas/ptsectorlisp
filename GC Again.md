      
My observations about sectorlisp just after I understood it and before the novelty of understanding it for the first time wears off:

# Stack Allocation
Most GPLs (General Purpose programming Languages) allocate locals on the stack.  And they GC (Garbage Collect) locals using the biblical-flood method - wipe the slate clean on RETURN.

I expected to see exactly this when I began examining SL (sector lisp).

Instead, I found something more profound.  SL provides a compacting GC (Garbage Collector).  

In only 40 bytes of code.

SL does not simply pop locals from the stack, it GCs them.

SL follows pointers and makes a copy of the result.  It GCs the other temporary cells (if any).

How does SL do this?  How does SL do this efficiently?

I examine these issues in this article...

# Functional Programming -> Stack Allocation
FP treats all code as functions.

The args to functions are evaluated before the function, itself, is called.

There can be no side-effects, e.g. NCONC, and, there can be no cycles in data.  

All data is created by function calls, e.g. CONS().  It is not possible to call a function without EVAL'ing its args first[^1].

Functions which EVAL their args automatically follow a strict stack-allocation policy.

And, strict stack-allocation makes it easy to build small GC's.

[^1]: [[FEXPRs as Macros]]
# Only 2 Datatypes
In SL, there are 2 - and only 2 - datatypes
1. atoms
2. lists.

Knowing that this is the rule, makes it possible to build effective GC.

The system - knowing the structure of datatypes - can examine and GC any data structure.

N.B.: user-defined data types defy this kind of simplicity.  IOW, adding user-defined data types to a language guarantees less-efficient implementation.

Having user-defined-datatypes makes it easier to create code that is self-consistent.

Having only 2 datatypes - and allowing the system to know this - makes it harder to create self-consistent code.

Hackers who use spreadsheets to program CRMs for dentists' offices don't care about self-consistent code.  They just want to "do it".

[[Easy UX or Consistency?]]
