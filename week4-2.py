#Start with 4 words “comfortable”, “round”, “support”, “machinery”, return a list of all possible 2 word combinations. 
#Example: ["comfortable round", "comfortable support", "comfortable machinery", .....]

wordList = ["comfortable", "round", "support", "machinery"]

String = ""
i = 0
j = 0
for i in wordList:
    for j in wordList:
        print(i + " " + j)