`All data is created by function calls, e.g. CONS().  It is not possible to call a function without EVAL'ing its args first.`

This applies to MACROs implemented as FEXPRs.  (I think).

FEXPRs must produce lists that are fed to the compiler.  

FEXPRs must be fully EVALed ("called") before the parent function is called.  

# Am I Wrong?
Maybe I'm wrong and have missed an edge-case.  

# Design Rules - Not Language Extensions
If so, the solution is *not* to alter the language, but to provide a check - a lint-like thing - that alerts progammers of such cases.  

Programmers must change the code so that it passes the checks.  

There is no good reason to change the language - we simply need to provide "design rules" and design rule checkers (like type systems, but better).