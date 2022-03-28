
from fractions import Fraction

def Q2cf(x):
    A = []
    while x > 0:
        a = x.__floor__()
        x = x - a
        if x > 0:
            x = 1/x
        A.append(a)
    return A

def cf2Q(A):
    x = None
    for i in range(len(A)-1,-1,-1):
        x = Fraction(A[i],1) if x is None else A[i] + 1/x
    return x



