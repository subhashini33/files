# read file
f = open("sample.txt", "r",encoding="utf8",)
# print(f.readlines())

# get the number of lines
l1 = f.readlines()
print(l1)
print(len(l1))

# get linecount without empty lines
## option 1 using while
i = 0 # line index
c = 0 # line count without emty lines
while i<len(l1):
    if l1[i] != "\n":
        c += 1
    i += 1
print(f"no of lines {i}")
print(f"no of lines without empty lines {c}")

## option 2 using for

c = 0 # line count without emty lines
for line in l1:
    if line != '\n':
        c += 1
print(f"no of lines {len(l1)}")
print(f"no of lines without empty lines {c}")

## option 3 using list comprehension

l2 = [line for line in l1 if line != '\n']
print(f"no of lines {len(l1)}")
print(f"no of lines without empty lines {len(l2)}")

# get the lines in a list
l2 = [line for line in l1 if line != '\n']
print(f"no of lines without empty lines {l2}")
print(len(l2))

# add l1 elements to l2
l2=[]
n=len(l1)
for i in range(0,n):
    l2.append(l1[i])
    print(f"content in l2 is {l2}")


l3 = []
for j in l1:
    if j != "\n":
        l3.append(j)
print(f"l3 content is {l3}")

# get the number of words
newlist = []
for items in l1:
    # print(items.split(","))
    newlist+= items.split(" ")
print(newlist)
print(len(newlist))
        
   
 # get number of unique words into set excluding special characters
s1 = set()
list2 = []
for word in newlist:
    word=word.lower()
    if word != "—": 
        for ch in "[@_!#$%^&*()<>?/\|}{~:],.":
            word = word.replace(ch,"")
            word = word.replace("\n","")
        # s1.add(word)
        list2.append(word)
s1=set(list2) #to convert list to set
print(s1)
print(len(s1))

print(list2)
print(len(list2))
    

# get the number of words in a list
for k in newlist:
    print(k)

# craete a dict with word as key and no of occurences in the file as values
d = {}
for i in s1:
    d[i]=list2.count(i)
print(d)


print(len(list2))
print(sum(d.values()))
    

f.close()

## using NLTK
import nltk # nltk.word_tokenize
from nltk import * # all
from nltk import word_tokenize

f = open("sample.txt", "r",encoding="utf8")

raw = f.read()
res = word_tokenize(raw)

word_cnt = {}
for word in res :
    if word in word_cnt:
        word_cnt[word] += 1
    else:
        word_cnt[word] = 1

print(res)
print(word_cnt)
f.close()


with open("sample.txt", "r",encoding="utf8") as f:
    lines = f.readlines()
    print(lines)


from collections import Counter
c = Counter(res)
print(c)