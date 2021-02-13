import os
import math
import binascii
import random
from Crypto.Util.number import *
from Crypto.Cipher import AES
from flag import *

class MyLCG:
    def __init__(self, S):
        self.A = int(binascii.hexlify(os.urandom(16)), 16)
        self.B = int(binascii.hexlify(os.urandom(16)), 16)
        self.M = getPrime(16*8)

        self.x = (S % self.M)
    def next(self):
        self.x = ((self.A * self.x) + self.B) % self.M
        return self.x

r = MyLCG(int(binascii.hexlify(os.urandom(16)), 16))
# print("A = " + str(r.A))
# print("B = " + str(r.B))
# print("M = " + str(r.M))
print("# M is prime number!")

cnt = 5
for i in range(cnt):
    print("X[{}] = {}".format(i,r.next()))

print("X[{}] = ?".format(cnt))

key = r.next()
cipher = AES.new(long_to_bytes(key), AES.MODE_CTR)
nonce = cipher.nonce
ct_bytes = cipher.encrypt(flag)
print("nonce = ", nonce)
print("ct_bytes = ", ct_bytes)

# decrypt
# cipher_dec = AES.new(long_to_bytes(key), AES.MODE_CTR, nonce=nonce)
# print(cipher_dec.decrypt(ct_bytes))
