
#Given 3 positive integers, find the sum of all numbers 
#between the first two that are a multiple of the third.
# eg. Given "1, 10, 2", the expected output is "20".

num1 = 0
num2 = 0
num3 = 0


while True:
    try: 
        num1 = int(input("Enter first number"))
        num2 = int(input("Enter second number"))
        num3 = int(input("Enter third number"))
        break
    
    except ValueError:
        print("Not a number. Try again")
        
myoutput = num3
        
for i in range(num1, num2):
    myoutput = num3 + myoutput
    
    
print(myoutput)
        
