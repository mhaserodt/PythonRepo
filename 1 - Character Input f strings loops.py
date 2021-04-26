#Using f strings, and inputs.  Returning name, the year one will turn 100, and look it X number of times.


from datetime import datetime
currentYear = datetime.now().year

name = str(input("Please enter your first name: "))
print(f"Well, howdy, {name}")
age = int(input("Do you think you could tell me your age? "))
print(f"Alright, {name}, you're {age} years old!")
birthday = str.lower(input("Have you already had your birthday this year? (Y/N) "))
choice = int(input("Ok, great! Now please pick a number! "))
x=0
while x < choice:
    if birthday == "y":
        print(f"Oh, and by they way, {name}, you'll be 100 years old in the year {(currentYear - age)+100}. This is loop {x+1}")
        
    else:
        print(f"Oh, and by they way, {name}, you'll be 100 years old in the year {(currentYear - age)+99}. This is loop {x+1}")
    x += 1


