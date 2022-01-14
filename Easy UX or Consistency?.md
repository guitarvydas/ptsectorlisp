Hackers who use spreadsheets to program CRMs for dentists' offices don't care about self-consistent code.  They just want to "do it".

What are the trade-offs?

Easy UX vs. PhD-level consistency?

In other professions (e.g. building construction), this is the difference between Research and Engineering.

Engineers use whatever-is-available to build solutions.

Researchers figure out how to make more-consistency available to Engineers.

Engineers don't do the actual construction.  Engineers hand-off blueprints to construction workers.

In software, we might split development into various stages:
- Architecture, getting requirements from the customer(s) and story-boarding what is necessary.
- Engineering, fleshing out the details and creating detailed pseudo-progams (drawings, pseudo-code, etc.)
- Coding, writing the program(s)
- Production Engineering - re-writing the programs to be more "efficient" given some efficiency targets, e.g. speed of execution, or, size of resultant program(s), etc., etc.  Compiling the programs.
-  Q/A - thinking about how to test the program(s) using white-box and black-box perspectives.  Thinking about how to re-structure the programs to make them more testable
- Testing - actually performing the tests
- Maintenance - collecting bug reports, and fixing bugs from the field

# Completeness vs. Easy UX?
Compiler writers want efficiency (space, speed)
	- willing to compromise language features.

Completists want
	- end-to-end mathematical reasoning, even if it takes a PhD degree to understand
	- ignore the fact that all other technologies - e.g. building construction (houses, bridges, etc.) - do not check for errors automatically, but work nonetheless.

End-users want utility and ease-of-use
	- willing to compromise compilation features
	- willing to compromise front-end type checking[^1]
	- want error checking but only if it doesn't impact freedom
	- think that Spreadsheets are great, even though spreadsheet languages are not full-blown programming languages
	- use whiteboards instead of programming languages

[^1]: Compromising on front-end type checking means creating a good Q/A department.  From this perspective, front-end type checking can be seen as an optimization (it reduces the size of the Q/A department).  Fully automated type-checking is a laudable goal, but we haven't achieved it in some 70 years.  We have yet to begin formalizing requirements gathering - at best we are attacking how to automatically check the mapping of programmer-intent onto programs.  Mapping programmer-intent is not the same as mapping customer-intent.

[[Declaration Before Use]]

# Hacker Language
[[Hacker Language]]
