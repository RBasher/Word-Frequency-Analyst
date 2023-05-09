#1. Open the file "text.txt"
f=open("text.txt")
#2. Read the file and store the lines into a string
textStr=f.read()
print(textStr)
#3. Split the string into a list of words
word_list=textStr.split(" ")
print(word_list)
