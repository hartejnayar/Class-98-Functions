# WAP which takes a path of a file from the user and outputs the number of words in the file.
def splitWords():
    s = input("Enter the file name:")
    f = open(s,'r')
    countWords = 0
    for line in f:
        spl = line.split()
        countWords = countWords + len(spl)
    print("number of words:", countWords)

splitWords()    
