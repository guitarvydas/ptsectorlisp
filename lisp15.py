from os import CLD_EXITED


kQuote = 6
kEq = 0
kCond = 0
kCons = 0
kAtom = 0
kCar = 0
kCdr = 0

listindex = None # this needs to be set before run
nextConsCell = None

example1_listmemory = [
  0, 0,  # fillers
  6, -4,
  28, 0
]

example2_listmemory = [
  0, 0,  # fillers
  6, -4,
  28, 0,
  16, -10,
  30, 0,
  -8, -12,
  30, 0,
  -6, -16,
  -2, 0,
  0, 0,
  0, 0,
  0, 0,
  0, 0,
  0, 0,
  0, 0,
  0, 0,
]

listmemory = example2_listmemory

def putl (v):
  global listindex
  global listmemory
  assert (listindex < 0)
  index = -listindex
  listmemory [index] = v
  listindex = - (index + 1)

atommemory = ['N', 2,
'I', 4,
'L', 0,
'Q', 8,
'U', 10,
'O', 12,
'T', 14,
'E', 0,
'E', 18,
'Q', 0,
'C', 22,
'O', 24,
'N', 26,
'D', 0,
'C', 30,
'O', 32,
'N', 34,
'S', 0,
'A', 38,
'T', 40,
'O', 42,
'M', 0,
'C', 46,
'A', 48,
'R', 0,
'C', 52,
'D', 54,
'R', 0,
0, 0,
0, 0,
0, 0,
0, 0,
0, 0,
0, 0,
0, 0,
0, 0,
0]

atomindex = 56

def puta (c, cdrValue):
  # put (c . cdrValue) into atom memory
  global atomindex
  global atommemory
  assert (atomindex > 0)
  assert (cdrValue == 0 or cdrValue == atomindex + 1)
  assert ((2 + atomindex) < atommemory.__len__ ())
  atommemory [atomindex] = c
  atomindex += 1
  atommemory [atomindex] = cdrValue
  atomindex += 1

def nila ():
  # null out the cdr of the newest atom
  global atomindex
  global atommemory
  assert (atomindex > 0)
  atommemory [atomindex - 1] = 0



def getmem (i):
  if (i >= 0):
    return atommemory [i]
  else:
    x = -i
    return listmemory [x]
    
def isNull (x):
  return (x == 0)

def isList (x):
  return (x < 0)

def isAtom (x):
  return (x >= 0)

def allocatedEarlier (x, other):
  return (x <= other)

def terpri ():
  print ("")

def printc (x):
  print (x, end="")

def pratom (x):
  while (not isNull (x)):
    printc (car (x))
    x = cdr (x)
  
def prlpar ():
  print ("(", end="")

def prrpar ():
  print (")", end="")

def prdot ():
  print (" . ", end="")

def prspaced (x):
  print (" ", end="")
  pr (x)

def mapc_prspaced (x):
  while (not isNull (x)):
    carx = car (x)
    cdrx = cdr (x)
    prspaced (carx)
    x = cdrx

def prlist (x):
  prlpar ()
  pr (car (x))
  if (isNull (cdr (x))):
    prrpar ()
  elif (isAtom (cdr (x)) and (not isNull (cdr (x)))):
    prdot ()
    pr (cdr (x))
    prrpar ()
  else:
    mapc_prspaced (cdr (x))
    prrpar ()


def lispPrint (x): # pr
  if (isAtom (x)):
    pratom (x)
  else:
    prlist (x)

def pr (x):
  lispPrint (x)

def copy (x, m, k):
  # print (f'copy {x} {m} {k}')
  if (isAtom (x)):
    return x
  if (allocatedEarlier (x, m)):
    return x
  else:
    return cons (copy (car (x), m, k), copy (cdr (x) , m , k)) + k

def moveListMemory (Dest, Src, blockSize):
  i = blockSize
  while (i > 0):
    listmemory [Dest + i] = listmemory [Src + 1]
    i = i - 1
  return Dest

def gc (A, result):  
  global nextConsCell
  # print (f'gc {A} {nextConsCell}')
  if (isAtom (result)):
    return result
  else:
    # atomic
    B = nextConsCell
    offset = abs (A - B)
    copy (result, A, offset)
    C = nextConsCell
    # begin scope
    newResult = C
    blockSize = abs (nextConsCell - B)
    Aprime = moveListMemory (A + blockSize, nextConsCell, blockSize)
    assert (newResult == Aprime)
    nextConsCell = Aprime
    # end scope
    return newResult
    # end atomic

def car (x):
  return getmem (x)

def cdr (x):
  if (x < 0):
    return getmem (x - 1)
  else:
    return getmem (x + 1)

def cons (a, b):
  global listindex
  p = listindex
  putl (a)
  putl (b)
  return p

def eval (e, a):
  global nextConsCell
  # print (f'eval ({e}, {a})')
  # lispPrint (e)
  # terpri ()
  A = nextConsCell
  if (e == 0):
      return e
  elif (isAtom (e)):
      return assoc (e, a)
  elif (kQuote == car (e)):
      return car (cdr (e))
  elif (kCond == car (e)):
      return evcon (cdr (e), a)
  else:
    evl = evlis (cdr (e), a)
    # print ("Evlis returned to Eval")
    # lispPrint (evl)
    # terpri ()
    returnFromApply = apply (car (e), evl, a)
    # print ("Apply returned to Eval")
    # lispPrint (returnFromApply)
    # terpri ()
    returnFromEval = gc(A, returnFromApply)
    # print ("Eval returns")
    # lispPrint (returnFromEval)
    # terpri ()
    return returnFromEval

def evcon (c, a):
    # print (f'evcon ({c}, {a})')
    # lispPrint (c)
    # terpri ()
    if (eval (car (car (c)), a)):
        return eval (car (cdr (car (c))), a)
    else:
        return evcon (cdr (c), a)

def evlis (m, a):
    # print (f'evlis ({m}, {a})')
    # lispPrint (m)
    # terpri ()
    if (m == 0):
        return 0
    else:
        exprFirst = eval (car (m), a)
        exprRest = evlis (cdr (m), a)
        result = cons (exprFirst, exprRest)
        return result

def assoc (x, y):
    # print (f'assoc ({x}, {y})')
    # lispPrint (x)
    # terpri ()
    # lispPrint (y)
    # terpri ()
    if (x == car (car (y))):
        return cdr (car (y))
    else:
        return assoc (x, cdr (y))

def pairlis (formals, actuals, a):
  # print (f'pairlis({formals}, {actuals}, {a})')
  if (formals == 0):
    return 0
  else:
    firstBinding = cons (car (formals), car (actuals))
    restBindings = pairlis (cdr (formals), cdr (actuals), a)
    return cons (firstBinding, restBindings)

def apply (f, x, a):
  # print (f'apply ({f}, {x}, {a})')
  # lispPrint (f)
  # terpri ()
  # lispPrint (x)
  # terpri ()
  # lispPrint (a)
  # terpri ()
  if (isList (f)):
    newEnv = pairlis (car (cdr (f)), x, a)
    lambdaForm = car (cdr (cdr (f)))
    return eval (lambdaForm, newEnv)
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

def Read (s):
  arr = list(s)
  index = 0
  input = {"index": index, "characters": arr}
  if ("(" == arr [index]):
    modifiedInput = ReadList (input)
  else:
    modifiedInput = ReadAtom (input)

def ReadAtom (input):
  while (not terminated (input)):
    ReadAtom1 (input)
  nila ()
  return input

def ReadAtom1 (input):
  cs = input["characters"]
  index = input["index"]
  if (terminated (input)):
    return input
  elif ("(" == cs [index]):
    return input
  elif (")" == cs [index]):
    return input
  else:
    pokeAtom (cs [index])
    input["index"] = input["index"] + 1
    ReadAtom1 (input)

def terminated (input):
  if (-1 == input["index"]):
    return True
  elif (input["index"] == len (input ["characters"])):
    input["index"] = -1
    return True
  else:
    return False

def pokeAtom (c):
  puta (c, atomindex + 1)

def ReadList (input):
  assert False

#listindex = -6 # example 1
#r = eval (-2, 0) # example 1

#listindex = -18
#nextConsCell = listindex
#r = eval (-14, 0) # example 2
#lispPrint (r)
#terpri ()

Read ("BCD")
pr (0)