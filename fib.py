# create a variale called N with type int and init value 0
from typing import Dict, List
N: int = 0
# get the user input and store the value in the N
N = int(input("Adad mored nazar ra vared konid : "))
# create a V a with type int init value 0
a = 0
# ...
b = 1
# create a variable called list_adad with type dict with init value {}
# dict_adad: Dict = {}
# for loop for n'th fib number
for n in range(N):
    # update the value of the a, b simultaneosly
    a, b = a + b, a
# output the n'th number to the user
# this must be outside of the for loop
print(f"the {N}th number in the fib", a)

# the range function create a generator integer numbers between 2 ints
print("range : ",range(N))
# one can access the numbers in the generator like othe iteratves using a for loop
for i in range(N):
    print(i)

