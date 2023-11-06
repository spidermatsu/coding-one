#Write a program that given a list of 
#numbers, multiply all numbers in the list. Bonus for ignoring non-number element. 
#Example: input: [1, 2, 3, 4], output: 24

mylist = [10,20,30,40]

#result = mylist[i] * mylist[i+1]
value = 1
output = mylist[0]
i = 0
for i in range (0, len(mylist)-1, 1):
    output = mylist[i+1] * output
    
print(output)
  