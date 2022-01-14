
# Notes on SectorLisp GC
Comment before the novelty of just-understanding wears off:
- stack allocation of locals in most PLs
- but, this is an actual GC (compacting)
- GC follows pointers
- stack alloc easy due to FP eval order and fact that all CONS cells are alloc’ed by function calls (eval args before calling function)
- only 2 types: lists and atoms - interpreter knows how to follow pointers, cons always contains pointers
- user-defined types bring complexity to GC (can’t know how to follow pointers w/o checking type dynamically)
  

- Reminded of a Guy Steele trick: need bit(s) (1, 2, 3), use bottom bits 000 allows math ops w/o effect