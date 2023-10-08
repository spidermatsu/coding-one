
while True:
    
  #save ourselves from a value error -
  #'try' the value first then respond if
  # it's not an integer
    try:
        number = int(input("Enter a number and I'll say if it's odd or even."))
        break
    except ValueError:

        print("Not a number. Try again")
        
if number%2 == 0:
    print("Even")
else:
    print("Odd") 
        
     
         