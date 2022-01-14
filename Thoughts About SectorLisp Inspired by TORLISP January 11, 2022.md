# Overview
Justine Tunney joined us and discussed Sector Lisp.

Sector Lisp is a Lisp that fits in one "disk sector" (i.e. < 512 bytes).

IMO, the most interesting aspect of SectorLisp is its Garbage Collector, 
developed by J. Tunney and needing only 40 bytes.   

Sector Lisp's GC is different from the GC used in McCarthy's original Lisp 1.5.

Sector Lisp's GC code is an illustration of how simple programs can be.  

Sector Lisp's GC code reminds us of the trade-offs in using more "modern" languages.

# README
[[README]]
[Sector Lisp Video](https://youtu.be/nZWR2ftBoA0)
[Sector Lisp GC Video](https://youtu.be/TF0FzcBkV60)
# FEXPRS
[[FEXPRS]]
# Backtracking, Early's Algorithm, PEG
[[backtracking, parsing, PEG]] 
Early's algorithm used to be verbotten, now common (PEG, PROLOG)

# Efficiency
[[Efficiency]]
# 2 Languages
1. Development
2. Production Engineering

# Compilation vs. Interpretation
All languages can be interpreted.

Only some languages can be compiled.

Going from interpretation to compilation involves trade-offs.  ATM, the trade-offs leak into the language design.  

ATM, compilable languages are "harder to use" than compiled languages.

# REPL (Read Eval Print Loop)

REPLs are easier to build in interpreted languages.

CL (and Scheme?), compiles statements entered interactively into the REPL, then executes the compiled code.

## Eval vs. Compilation
Compiler == Eval ().

## Compilation is an Optimization
[[Compilation is an Optimization]]

## Early Assumptions
- 1 cpu
- save memory (memory is expensive)
- must use text, since graphics is too expensive
## Re-Thinking Computing
I believe that we need to re-think computing due to new 
- hardware
- memory
- graphics
- browsers
- speed
- internet
- IoT

The old prejudices - memory is scarce, we have only 1 CPU - aren't true anymore.

We continue to use technologies that are based on these old prejudices.

Taken to the extreme, I argue that we *only* want to control computers.  From this perspective, this means that Languages and Operating Systems are not needed.

For example, functional programming is based on the notion of a shared stack (a global variable!).  We want thingies that are concurrent and that don't use a shared stack[^2].

[^2] I call these thingies *Components*.  Discussed elsewhere.
# Ideas
- SL as a spreadsheet language (no function > 127 bytes)
- SL as component language

# Garbage Collection
## Generational GC
Generational GC[^1] first appeared in Smalltalk.

[^1]: GC means  "Garbage Collection".

# Mark-and-sweep GC
	- stop the world
		- pass 1: CDR down OBLIST and set a mark on every cell in use
			- pass 1a: follow pointers from registers and mark every cell in use
		- pass 2: sweep through all memory and gather up (link together on a list) every cell that doesn't have a mark
		- pass 3: sweep through memory and unmark all cells
	- unstop the world

Various tricks were invented for collecting up garbage cells without blowing out all memory.  

For example, garbage cells are linked together by modifying their CDRs to point backwards to the rest of the garbage-list.  The cells are garbage anyway, so modifying their CDRs is no big deal.

# Compacting GC
Compacting is that act of de-fragmenting memory.

I first saw compaction in C's `free ()` function.  If a newly freed lump of memory was adjacent to another block of free memory, the lumps are coalesced into one lump.

# Reference Counting
Associates a `usage counter` with each datum.  

Every time a datum is freed, (e.g. by going out of scope), its `usage counter` is decremented.  

When the `usage count` reaches 0, the cell is deemed to be Garbage and immediately collected into the free list.

This spreads the cost of GC out, reducing the stop-the-world time to a very small amount of time (but, performed multiple times).

This method
- reduces the worst-case stop-the-world time
- increases the size of datums by including a `usage-counter`.
- is more space-costly than mark-and-sweep.  Mark-and-sweep needs only one bit (the mark), whereas the reference counting method requires a full number.
- hits the wall when the `usage counter` rolls over, e.g. when the `usage counter` can no long correctly represent the number of users of the datum, e.g. the 256'th user of a datum when the `usage count` is maintained as an Unsigned Byte

# Biblical flood
	- what UNIX does with C programs
	- when a program finishes, wipe the slate clean
	- don't waste time following pointers

Very time-efficient, but requires the use of an uber-operating-system that activates programs and knows when to wipe the slate clean.

[[GC Again]]

# GUIs
A number of programming languages evaporated because they relied on non-native GUIs and did not represent GUI widgets that had the look-and-feel provided by the operating system.

ParcPlace Smalltalk had this problem

Rebol 2.7.x had this problem.

Ironically, *now* we have but *one* kind of GUI - the Browser - and its API is the same on every operating system (the API is JavaScript and HTML).

ParcPlace Smalltalk and Rebol have not come back to life.

We see many new languages for handling the single-API - e.g. ClojureScript, ParenScript, etc., etc. - but, ParcPlace Smalltalk and Rebol have not made a come-back[^1].

[^1]: Rebol inspired JSON.  Rebol's inventor - Carl Sassenrath - has gone on to invent [ASON](https://altscript.com) with what he learned from writing Rebol.

## CLOG
HTML and JavaScript are low-level accessors to The Browser.

I am currently exploring/thinking-about [CLOG](https://github.com/rabbibotton/clog) as a somewhat simpler version of the API to the The Browser.


# Garbage Collection
[[Garbage Collection]]

# Macros, FEXPRs and Ohm-JS
[[Macros, FEXPRs and Ohm-JS]]

# Tiny Basic
[[Tiny Basic]]

# LAMBDA Means Stack Allocation
[[LAMBDA Means Stack Allocation]]

# Scheme vs. Early Lisp
Scheme was invented when OO[^5] was new.

In Racket, "Programs as Lists" has become "Programs as Objects" (syntax objects), with attendant increase in code bloat and checking.  Macros are no longer "simple".

Syntax Objects are a heavier concept than CONS cells.

[^5]: OO == Object Oriented