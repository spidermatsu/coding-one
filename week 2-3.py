#Implement division as a series of subtraction. The program should only deal with integers and report the remainder 
#if there is one. eg. 10/2 => 10-2-2-2-2-2=0, 10 minus 2 five times so the division result is 5 with a remainder of 0

num1 = int(input("input 1st number"))
num2 = int(input("input 2nd number"))
bool = False

while num1 > 0:
    if num1 >= num2:
        num1 = num1 - num2
        print(num1)
    elif num1 <= num2:
        print(num1)
        num1 = 0
    else:
        print(num1)
        num1 = 0
