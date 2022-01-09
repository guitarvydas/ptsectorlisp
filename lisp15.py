from os import CLD_EXITED


kQuote = 6
kEq = 0
kCond = 0
kCons = 0
kAtom = 0
kCar = 0
kCdr = 0

listindex = (-1)
cx = listindex

listmemory = [
  0, 0,  # fillers
  6, -4,
  30, 0
]

def putl (v):
  global listindex
  listmemory [listindex] = v
  listindex = listindex - 1


atommemory = [
  "N", 2,
  "I", 4,
  "L", 0,
  "Q", 8,
  "U", 10,
  "O", 12,
  "T", 14,
  "E", 0
  ]

def getmem (i):
  if (i >= 0):
    return atommemory [i]
  else:
    x = -i
    return listmemory [x]
    

def copy (x, m, k):
  if (x < m):
    return x
  else:
    return cons (copy (car (x), m, k), copy (cdr (x) , m , k)) + k

def gc (A, x):
  global cx
  B = cx
  x = copy (x, A, A - B)
  C = cx
  while (C < B):
    A = A - 1
    B = B - 1
    set (A, B)
  cx = A
  return x

def car (x):
  return getmem (x)

def cdr (x):
  if (x < 0):
    return getmem (x - 1)
  else:
    return getmem (x + 1)

def cons (a, b):
  putl (b)
  putl (a)

def eval (e, a):
  print (f'eval ({e}, {a})')
  A = cx
  if (e == 0):
      return e
  elif (e > 0):
      return assoc (e, a)
  elif (kQuote == car (e)):
      return car (cdr (e))
  elif (kCond == car (e)):
      return evcon (cdr (e), a)
  else:
      return gc (A, apply (car (e), evlis (cdr (e), a), a))

def evcon (c, a):
    print (f'evcon ({c}, {a})')
    if (eval (car (car (c)), a)):
        return eval (car (cdr (car (c))), a)
    else:
        return evcon (cdr (c), a)

def evlis (m, a):
    print (f'evlis ({m}, {a})')
    if (m == 0):
        return 0
    else:
        return cons (eval (car (m), a), evlis (cdr (m), a))

def assoc (x, y):
    print (f'assoc ({x}, {y})')
    if (x == car (car (y))):
        return cdr (car (y))
    else:
        return assoc (x, cdr (y))

def pairlis (x, y, a):
  print (f'pairlis({x}, {y}, {a})')
  if (x == 0):
    return 0
  else:
    return cons (cons (car (x), car (y)), pairlis (cdr (x), cdr (y), a))

def apply (f, x, a):
  print (f'apply ({f}, {x}, {a})')
  if (f < 0):
    return eval (car (cdr (cdr (f))), pairlis (car (cdr (f)), x, a))
  elif (f == kEq):
    return car (x) == car (cdr (x))
  elif (f == kCons):
    return cons (car (x), car (cdr (x)))
  elif (f == kAtom):
    return (car (x) >= 0)
  elif (f == kCar):
    return car (car (x))
  elif (f == kCdr):
    return cdr (car (x))
  else:
    return apply (assoc (f, a), x, a)

r = eval (-2, 0)
print (r)