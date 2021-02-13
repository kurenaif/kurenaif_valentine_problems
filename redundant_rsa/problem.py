from Crypto.Util.number import *
from flag import *
import secrets


leftDummy = secrets.token_bytes((500 - bytes_to_long(flag).bit_length()) // 8 // 2)
rightDummy = secrets.token_bytes((500 - bytes_to_long(flag).bit_length()) // 8 // 2)

# format: RANDOM_DATAkurenaifCTF{*}RANDOM_DATA
# please Extract kurenaifCTF{*} by manual work :)
m = bytes_to_long(leftDummy + flag + rightDummy)


p = getPrime(256)
q = getPrime(256)
N = p*q

# guarantee and hint 
assert GCD(m*m % N, N) == 1
assert GCD(m*m*m % N, N) == 1

# In CTF, 3 is sometimes used, but in general RSA, 65537 is used.
print("N =", N)
print("c3 =", pow(m, 3, N))
print("c65537 =", pow(m, 65537, N))
