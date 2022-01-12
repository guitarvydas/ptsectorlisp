[[FEXPRS]]
we need to re-think computing due to new hardware, memory, speed, internet, IoT
Early's algorithm used to be verbotten, now common (PEG, PROLOG)
stack allocation, in lieue of generalized heap (no cycles)
byte addresses
spreadsheet language
component language
mark-and-sweep gc
byte-oriented pages
generational GC - first appeared in Smalltalk <--
GUIs - ParcPlace Smalltalk died off because of inability to look-and-feel like underying os
	- irony: now we have 1 GUI - the browser
	- see CLOG for inspiration on GUI building
we gave up a lot of efficiency for compilability, 
we gave up a lot of "hacker" features in switch to CL and Scheme
hacker language
lambda means implicit stack - good for 1 cpu (1 thread) not good for distributed, choose new notation (FP in crazy-land, need a PhD to understand it (fails promise of "easier to reason about"))
fexpr <= rewrite EVLIS to not eval args <= instant macros (NEVLIS?, LIS?)
Ohm-JS "better" macros than Lisp (character-based instead of cons-cell based)
worlds
Tiny Basic - DDJ, 2K basic, bytecodes
eval == compile
production code should never call eval <= let Production Engineers refactor the code and switch languages
dynamic binding vs static binding, CL "special" variables
surprised to see how efficient sl is, opened my eyes to how much we pay for switch to production engineering languages
hacker language => allows fresh ideas quickly, no limits, no Production Engineering while trying to design
efficiency depends on what you are trying to do - Design vs. Production Engineering
my (1) .md's about sectorlisp, (2) video / youtube (3) lisp15.py
two memory spaces <= two lists, insert 2 sentinel bytes at front of memory list <= -ve address work (using abs())
I built forward-chaining AI in AshtonTate Framework spreadsheet language (<= lots can be achieved if you stop being hackled by compiler-only mentality)
FvdW Lisp on my github
old worries / assumptions that need to be re-examined in new light: 1 CPU, Reclaim Memory
best/cheapest GC - biblical flood (UNIX & C had it)
memory leaks weren't a problem until O/Ss showed up (what were the trade-offs?)
idea: is SL an embeddable hacker language?
Scheme was invented when OO-thinking was new
	- "programs are lists" was replaced by syntax objects (much heavier than CONS cell-based programs)
we don't see the cost of switching from a hacker language to a compilable language, but we live with the trade-offs every day
Anatomy of Lisp, J.R. Allen (lisp compiler in pre-CL lisp, modulo typos)
(FUNCTION ...) quote (aka #' in Racket)
smallness == early issues of DDJ (TinyBasic)
CLOG
ASON

fexprs == macros for free (minor change to EVLIS)
efficiency
DDJ and Byte were "hackers" magazines (like Make today?)
BASIC = many systems were built by hackers in other fields, e.g. accounting for medical offixes
future: (1) SS language, Component language
niche for hacker language? instead of full-blown Production Engineering language?

## FEXPRS
[[FEXPRS]]
## Backtracking, Early's Algorithm, PEG
[[backtracking, parsing, PEG]] 
Early's algorithm used to be verbotten, now common (PEG, PROLOG)

## Efficiency
[[Efficiency]]
## 2 Languages
1. Development
2. Production Engineering

## Compilation vs. Interpretation
All languages can be interpreted.

Only some languages can be compiled.

Going from interpretation to compilation involves trade-offs.  ATM, the trade-offs leak into the language design.  

ATM, compilable languages are "harder to use" than compiled languages.

## REPL (Read Eval Print Loop)

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
we need to re-think computing due to new 
- hardware
- memory
- graphics
- browsers
- speed
- internet
- IoT

# Ideas
- SL as a spreadsheet language (no function > 127 bytes)
- SL as component language

# Garbage Collection
mark-and-sweep gc
	- stop the world
		- pass 1: CDR down OBLIST and set a mark on every cell in use
			- pass 1a: follow pointers from registers and mark every cell in use
		- pass 2: sweep through all memory and gather up (link together on a list) every cell that doesn't have a mark
		- pass 3: sweep through memory and unmark all cells
	- unstop the world
generational
compacting
C
biblical flood
	- what UNIX does with C programs
	- when program finishes, wipe the slate clean
	- don't waste time following pointers
