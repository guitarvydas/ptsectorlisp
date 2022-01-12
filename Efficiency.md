
stack allocation, in lieue of generalized heap (no cycles)

compiler writers want efficiency (space, speed)
	- willing to compromise language features

end-users want utility and ease-of-use
	- willing to compromise compilation features
	- willing to compromise front-end type checking
	- want error checking but only if it doesn't impact freedom

byte addresses
	- GC of byte-oriented pages ; reserve one byte to mean "off-page" connector (followed by mulitiple bytes for page location?)

obvious: bytes are more space-efficient 16-bit words 
	- 8 < 16 < 32 < 64


## Code Bloat
[[Code Bloat]]
