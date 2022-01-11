# Code
From [code](https://justine.lol/sectorlisp2/#listing).

```
function Copy(x, m, k) {
  return x < m ? Cons(Copy(Car(x), m, k),
                      Copy(Cdr(x), m, k)) + k : x;
}

function Gc(A, x) {
  var C, B = cx;
  x = Copy(x, A, A - B), C = cx;
  while (C < B) Set(--A, Get(--B));
  return cx = A, x;
}
```


# GC Operation In Pictures
## Step 1
![[gc-GC 1.svg]]
## Step 1 Reformatted
![[gc-GC 2.svg]]
## Step 2 Copy Result Using Offsets
![[gc-GC 3.svg]]
## Step 3 Move & Discard
![[gc-GC 4.svg]]

# Notes
- 2 spaces
	1. atoms
	2. lists (aka "cons cells")
- all cons cells allocated in strict stack-like order
- therefore, all cells that are part of a list are allocated earlier in the stack than the list itself
- GC(A,x) where A is the previous SP and x points to the result cell
- the only function that can generate CONS cells is CONS()
	- CONS() is called by: PAIRLIS, EVLIS
	- user functions (LAMBDAs)
- any result is either (a) a pointer into Atom space, or, (b) a pointer into list space
- in the (b) case, the list can contain only pointers into Atom space or into list space ; pointers into list space will always be CONS cells that were allocated BEFORE the result pointer 
- every call to Eval does GC, hence, intermediate results in Evlis are always compacted
- Eval calls GC when it applies a function to args, it does not call GC when processing a special form
- Design Rule (prerequisite): no cycles in lists

# Marker Bit
One bit is need to mark cells as either
1. atom
2. list

In the code, the sign bit (`+` or `-`) is used as the mark.

All `+ve` indices point to atoms.

All `-ve` indices point to list cons cells.

# NIL

The index `0` is used as NIL.

NIL sits directly between both spaces (atom and list).

`0` was originally chosen because it was small (1 byte) and allowed the hardware sign bit to be used to separate the memory spaces. 

`0` fits in the CDR of a cell, so extra memory is not required to represent end-of-list.

[Note that C's NULL is chosen as 0x00 for the same reasons of reducing memory cost.  Strings contained 1-byte characters (ASCII, preceding the advent of unicode).  Arrays of characters could be stored contiguously in memory, using 0x00 as the terminator.[^1]].

[^1]: Arrays are simply optimized lists - no CDRs required.

# Implied Variables
The above assumptions are valid for 1-CPU (1-Thread).

For >1 CPUs (>1 Threads) we might make the STACK (bookmarks) explicit.

The stack is a free variable (aka global variable) which is inherited by all functions in the same Thread (CALL/RETURN uses this free variable).

Operating systems (e.g. Linux, Windows, MacOS, etc.) create objects (Threads) that implicitly provide one STACK free variable to all functions within the same objects (threads).

Corollary: we feel that "multitasking is hard" because the STACK is used like a global variable (implicit, not explicit).
