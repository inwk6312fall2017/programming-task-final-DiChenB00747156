#Question :Find the longest word used in each book
import string
def longest(filename):
    longest = ''
    list = []
    with open(filename,'r') as fin1:
        for line in fin1:
            wordlist = line.strip()
            wordlist1 = wordlist.strip(string.punctuation)
            wordlist2 = wordlist1.split()
            for word in wordlist2:
                list.append(word) #get a list that including all words in this book

    list1 = sorted(list, key = len)#sord this list according to length
    print("In this book, the longgest word is :")
    print(list1[-1])#The last word is definitely longgest!



print(longest("book1.txt"))
print(longest("book2.txt"))
print(longest("book3.txt"))
