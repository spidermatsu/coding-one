#Make a program that uses a lookup table to convert any set of alphabets into their corresponding NATO phonetic alphabets. Also implement the inverse function.
#- Input: cat
#- Output: charlie alfa tango

NATOAlphabet = {
  "a" : "Alpha", "b" : "Bravo", "c" : "Charlie", "d" : "Delta", "e" : "Echo", "f": "Foxtrot", "g" : "Golf", "h" : "Hotel",
  "i" : "India", "j" : "Juliet", "k" : "Kilo", "l" : "Lima","m" : "Mike", "n" : "November","o" : "Oscar", 
  "p" : "Papa", "q" : "Quebec", "r" : "Romeo", "s" : "Sierra", "t" : "Tango","u" : "Uniform", "v" : "Victor", "w" : "Whiskey", 
  "x" : "X-ray","y" : "Yankee", "z" : "Zulu", " " : " "
}

print(NATOAlphabet["a"])

myString = input(str("Type a word or sentence"))

stringList = []


for letter in myString:
	stringList.append(letter)
print(stringList)
i = 0 
for i in stringList:
    print(NATOAlphabet[i])
