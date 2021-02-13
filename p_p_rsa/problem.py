from Crypto.Util.number import *
from flag import *
import secrets

m = bytes_to_long(flag)

p = getPrime(256)
q = p # Oops!
N = p*q
e = 65537
print("e =", e)
print("N =", N)
print("c =", pow(m, e, N))

