myNum1 = int(input("Yo, give me a number! "))
myNum2 = int(input("Throw another number at me! "))
modNums = myNum1 % myNum2
divBy41 = myNum1 % 4
divBy42 = myNum2 % 4
evenOrOdd1 = myNum1 % 2
evenOrOdd2 = myNum2 % 2
if modNums == 0:
    print (f"Your first number, {myNum1}, is evenly divisible by your second number, {myNum2}!")
elif myNum1 < myNum2:
    print (f"Your first number, {myNum1}, is less than your second number, {myNum2}, thus not divisible!")
else:
    print (f"Your first number, {myNum1}, is not evenly divisible by your second number, {myNum2}.  Your remainder is {modNums}!")

if divBy41 == 0:
    print (f"Your first number, {myNum1}, is even and divisible by 4")
elif evenOrOdd1 == 0:
    print (f"Your first number, {myNum1}, is even, but not divisible 4")
else:
    print (f"Your first number, {myNum1}, is odd!")

if divBy42 == 0:
    print (f"Your second number, {myNum2}, is even and divisible by 4")
elif evenOrOdd2 == 0:
    print (f"Your second number, {myNum2}, is even, but not divisible 4")
else:
    print (f"Your second number, {myNum2}, is odd!")
