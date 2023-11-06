#Make a function that takes two arguments (given name and family name), 
#the second of which is optional. Print a greeting according to which arguments are provided.
#Example output: “Hello Kenneth.” or “Hello there, Kenneth of Lim!” 

fname = str(input("Type first name?"))
lname = str(input("Type last name? Don't have to, can just press enter"))

def greeter(fname, lname):
    if lname == '':
        print("Hello, " + fname + ".")
    else:
        print("Hello, " + lname + " of " + fname +"!")
  
greeter(fname, lname)
  
