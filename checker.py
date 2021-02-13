import hashlib
import sys

if len(sys.argv) < 2:
    print("usage: python3 checker.py kurenaifCTF{??????}")
    exit(1)

flags = {
'752386beff147029ca4a226eb9be49a6b52eb2c0674ba5d26fa4b7f88907b50fc0bbfc75a6c640a11d4f39ea66a7880897f237d109608632c7b6fba749e025a6': 'p_p_rsa',
'4ee96144f10f9589b3942e7b8a614496bf6e45790366e215d42e91706881baef96f0e0775ba43812ce63dba6fe83db3d855eb2f3b3959f6ec62912d1be135d8c': 'redundant_rsa',
'18de65287bb71c248d02251bd8eab636a53b9d896c25142ae863a7ece47ebb5212e77f270d5a249b37dd1925330876a487b2c70f238609cd0c381dfb6e80e523': 'the_big_five',
'c77fb126b92a0cdf25173cd405b02971cda6fc508efff498796412112dc4afc69424c123cc371fad730dc2a9818ec092de45f4f3b652d52e4ad65ec66b65baa7': 'the_onetime_pad',
'4a1232e682f84b4064caba8db7e976d9d2bbf1d9f4b107f2b9bd9f78dea14b21202a5edaecb4b4c0dad08b18963d4c482d1fe542ed24339913e3809bb66b7a30': 'three_values_twister',
}

text=sys.argv[1]
h = hashlib.sha512(text.encode('utf-8')).hexdigest()
if h not in flags:
    print("wrong...")
else:
    print("correct {}! please write up your solution!".format(flags[h]))
