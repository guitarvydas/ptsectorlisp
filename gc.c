// Attempt to understand GC and Copy

function Copy(x, m, k) {
  return x < m ? Cons(Copy(Car(x), m, k),
                      Copy(Cdr(x), m, k)) + k : x;
}

function Gc(A, x) {
  var C, B = cx;
  x = Copy(x, A, A - B), C = cx;
  while (C < B) Set(--A, Get(--B));
  return cx = A, x;
}

// 1. remove comma operators
function Gc(A, x) {
  var C;
  var B = cx;
  Copy(x, A, A - B);
  C = cx;
  x = C;
  while (C < B) Set(--A, Get(--B));
  cx = A;
  return x;
}

// 2. insert explicit {}
function Gc(A, x) {
  var C;
  var B = cx;
  Copy(x, A, A - B);
  C = cx;
  x = C;
  while (C < B) {
    Set(--A, Get(--B));
  }
  cx = A;
  return x;
}

// 3. replace "cx" by "nextConsCell"
function Gc(A, x) {
  var C;
  var B = nextConsCell;
  Copy(x, A, A - B);
  C = nextConsCell;
  x = C;
  while (C < B) {
    Set(--A, Get(--B));
  }
  nextConsCell = A;
  return x;
}

// 4. single assigment (x = C --> xPrime = C)
function Gc(A, x) {
  var C;
  var B = nextConsCell;
  Copy(x, A, A - B);
  C = nextConsCell;
  {
    var xPrime = C;
    while (C < B) {
      Set(--A, Get(--B));
    }
    nextConsCell = A;
    return xPrime;
  }
}

// 5. replace "x" by "result"

function Copy(x, m, k) {
  return x < m ? Cons(Copy(Car(x), m, k),
                      Copy(Cdr(x), m, k)) + k : x;
}

function Gc(A, result) {
  var C;
  var B = nextConsCell;
  Copy(result, A, A - B);
  C = nextConsCell;
  {
    var resultPrime = C;
    while (C < B) {
      Set(--A, Get(--B));
    }
    nextConsCell = A;
    return resultPrime;
  }
}

// 6. Gc cannot be interrupted, because intermediate results are inconsistent
//    (copied result contains pointers with offsets)
function Copy(x, m, k) {
  return x < m ? Cons(Copy(Car(x), m, k),
                      Copy(Cdr(x), m, k)) + k : x;
}

function Gc(A, result) {
  atomic {
    var C;
    var B = nextConsCell;
    Copy(result, A, A - B);
    C = nextConsCell;
    {
      var resultPrime = C;
      while (C < B) {
	Set(--A, Get(--B));
      }
      nextConsCell = A;
      return resultPrime;
    }
  }
}

// 7. rename (A - B)
function Copy(x, m, k) {
  return x < m ? Cons(Copy(Car(x), m, k),
                      Copy(Cdr(x), m, k)) + k : x;
}

function Gc(A, result) {
  atomic {
    var C;
    var B = nextConsCell;
    var offset = A - B;
    Copy(result, A, offset);
    C = nextConsCell;
    {
      var resultPrime = C;
      while (C < B) {
	Set(--A, Get(--B));
      }
      nextConsCell = A;
      return resultPrime;
    }
  }
}

// 8. lasso move
function Copy(x, m, k) {
  return x < m ? Cons(Copy(Car(x), m, k),
                      Copy(Cdr(x), m, k)) + k : x;
}

function moveMemory (Dest, Src, blockSize) {
  return memcpy (Dest, Src, blockSize);
}

function Gc(A, result) {
  atomic {
    var C;
    var B = nextConsCell;
    var offset = abs (A - B);
    Copy(result, A, offset);
    C = nextConsCell;
    {
      var newResult = C;
      var blockSize = abs (nextConsCell - B);
      var Aprime = moveMemory (A + blockSize, nextConsCell, blockSize);
      assert (newResult == Aprime);
      nextConsCell = Aprime;
      return newResult;
    }
  }
}




