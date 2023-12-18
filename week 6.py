#L-systems are a fractal - like model, used to look at things like algae.
# Set initial state of l-system
#0th generation
initial = "AB"

# Rules for the l-system, that next generations will follow
rules = {
	"A": "AB",
	"B": "A"
}

# L-system function takes 3 paramaters, the initial state,
# the rules of which to change the initial state value the desired number of generations
def l_system(initial, rules, generation):
   # passes by value 
	current = initial

# for loop to loop for the amount of times in the generation value -1
	for _ in range(0, generation):
     #empties result value
		result = ""
#The two states get passed through the 'rules' dictionary to access their corresponding value
#For example changing AB to ABA - 
#this is because the first A in inital gets changed to AB and B changed to A
#Which then gets appended to the result value creating an extended string of results
# then for each iteration in the loop, every number in the result is run through the dictionary
		for state in current:
			result += rules.get(state, state)

		current = result
#returns the string
	return current

#prints the results 10x
#in a way that makes each n of the recursion be the start of each line 
# and runs the function using each i as the generation number
for i in range(0, 10):
	print( "{}: {}".format(i, l_system(initial, rules, i)) )
