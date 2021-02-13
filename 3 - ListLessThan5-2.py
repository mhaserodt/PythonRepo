allNums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lessThan=[]
greaterEqualThan=[]
myNum = int(input("Enter a number! "))
for element in allNums:
    if element < myNum:
        lessThan.append(element)
    else:
        greaterEqualThan.append(element)

print(f"Less than {myNum} = {lessThan}.")
print(f"Greater or equal to {myNum} = {greaterEqualThan}.")
