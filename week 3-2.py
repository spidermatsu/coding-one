inputString = input("Type a sentence")
String = inputString.split(" ")

for item in String:
    x = item[0]
    item = item[1:]
    print(item+x+"ay")
    
    
