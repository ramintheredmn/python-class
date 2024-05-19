import math

meld: int = 0
inr: float = 0
cr: float = 0
bil: float = 0

inr = float(input("Enter the INR: "))
cr = float(input("Enter the serum cratinin: "))
bil = float(input("Enter the serum bil: "))

meld = round((9.57 * math.log(cr)) + (3.78 * math.log(bil)) + (11.2 * math.log(inr)))
print("meld score is: ", meld)
