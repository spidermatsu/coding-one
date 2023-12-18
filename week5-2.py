#Implement a Caesar Cipher function that takes a string and shift amount, outputs the encrypted string.
#- Input: hello word
#- Shift by: 7
#- Output: olssv dvysk

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cipherInput = str(input("Enter a sentence")) 

cipherShift = int(input("Enter shift amount"))

#print(alphabet.index('b'))
sentenceList = []
for letter in cipherInput:
    sentenceList.append(letter)

i = 0 
newIndex = 0
newString = ""
for i in sentenceList:
    #print(alphabet.index(i))
    if i == ' ':
        newString = newString + ' '
    else:    
        newIndex = alphabet.index(i) + cipherShift
        newString = newString + alphabet[newIndex]

print(newString)
    
    