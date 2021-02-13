import secrets
from flag import *
from Crypto.Util.number import *

class LCG:
    def __init__(self):
        self._x = secrets.randbits(64)
        self._a = 2
        self._m = secrets.randbits(64)

        while self._m % 2 == 0:
            self._m = secrets.randbits(64)

        print("m =", self._m)
    
    def next(self):
        self._x = (self._x*self._a) % self._m
        return self._x

lcg = LCG()

assert b"kurenaifCTF" in flag
flag = bytes_to_long(flag)


length = flag.bit_length()
print("length =", length)

rand = 0
for i in range(length + 50):
    rand += (lcg.next() & 1) << i

print("cipher =", rand ^ flag)
