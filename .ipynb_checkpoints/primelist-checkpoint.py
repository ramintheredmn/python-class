# import the function prime that we declared in the prime.py file
from prime import ifprime
from typing import List

# Create a variable called n with type int and the initValue 0
n: int = 0
# get the userinput then convert to int then store in the n
n = int(input("adad ra vared konid: "))
# create variable called list_avval_ha with type List[int] that will store the prime numbers in the range specified by the user
list_avval_ha: List[int] = []
# iterate over the integer numbers in the range [2, n) and append the number to the list_avval_ha if the number is prime
for i in range(2, n):
    if ifprime(i):
        list_avval_ha.append(i)
# output the list to the user
print(f"adad avval dar baze 0 ta {n}:", list_avval_ha)
