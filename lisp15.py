listmemory = []
atommemory = []

def getmem (i):
  if (i >= 0):
    return atommemory [i]
  else:
    return listmemory [-i]
    
def car (x):
  return getmem (x)

def cdr (x):
  return getmem (x + 1)

def cons (a, b):

def eval (e, a):
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
    if (eval (car (car (c)), a)):
        return eval (car (cdr (car (c))), a)
    else:
        return evcon (cdr (c), a)

def evlis (m, a):
    if (m == 0):
        return 0
    else:
        return cons (eval (car (m), a), evlis (cdr (m), a))

def assoc (x, y):
    if (x == car (car (y)):
        return cdr (car (y))
    else:
        return assoc (x, cdr (y))

  def pairlis (x, y, a):
    if (x == 0):
      return 0
    else:
      return cons (cons (car (x), car (y)), pairlis (cdr (x), cdr (y), a))

  def apply (f, x, a):
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
