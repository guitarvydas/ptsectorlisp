
Sector Lisp uses stack allocation, in lieue of using a generalized heap (no cycles).

This make Garbage Collection easier and smaller
 [[Garbage Collection]]


# Byte addresses

[[Byte Addresses]]

obvious: bytes are more space-efficient 16-bit words 
	- 8 < 16 < 32 < 64


# Code Bloat
[[Code Bloat]]

# Compilation is an Optimization
[[Compilation is an Optimization]]

# Hacker Language vs. Purist Language
We traded off a lot of "hacker" features for compilability.

We traded off a lot of space efficiency for compilability.  For example, user-defined types defy simple GC, which leads to more code.  For example, trying to sub-divide atoms into classes (int, char, etc.) uses up more memory in each datum, then incurs a speed penalty, since the checking is more elaborate.  

This kind of compilability is good for Production Engineering.  Q: Is compilability good for program Brainstorming and Documentation? 

Is Sector Lisp an embeddable hacker language?

[[Dynamic Scoping vs. Static Scoping]]

# What Are You Doing?
The meaning of "Efficiency" depends on what you are trying to accomplish.

1. Design and Brainstorming
	- During the Design phase, "efficiency" means not blocking ideas
	- ideas are blocked by having to specify too much detail
	- ideas are blocked by poor turn-around and slow tooling
	- ideas are blocked by asking too many questions, like "which File do you want to ultimately save this in?", "do you want to build a mind-map with edges as sharp corners or rounded corners?"
	- ideas are blocked by live-marking spelling errors (e.g. squiggly red lines) when spelling doesn't matter as much as content
	- ideas are blocked by Modes[^1] (the tool needs to know what you are doing, and gets in the way)
	- type checking only matters if it helps flow of thoughts
	- (type checking is often claimed to help the Design Process, but, that generalizes to "trying things out" as a way to think about problems ; REPLs help in this way, also ; thinking things through by designing a type system is akin to using a REPL)
2. Production Engineering
	- dot all the I's and cross all the T's
	- details matter
	- type checking matters
	- self-consistency matters
	- optimizing the result is more important than human resource usage
	- tool efficiency is less important than completeness
	- the result does not need to be more efficient than what is required by the customer (product must fit on customers' machines ; product must run "fast enough" from customers' perspective ; for cost-sensitive customers, the product needs to be squeezed to fit and run on inexpensive machines)

When Design and Production Engineering are not separated, accidental complexity often results.  Paying Designers to Production Engineer programs is a waste of money, yet, we do this every day, by insisting that Designers use Production Engineering languages like Haskell, Rust, Python, C++, JavaScript, etc.
[^1]: See also [Humane Interface](https://www.amazon.ca/Humane-Interface-Directions-Designing-Interactive/dp/0201379376)

