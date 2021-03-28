from collections import Counter

file = open('TestZadanie2')
words=[x.replace('\n','') for word in file for x in word.split(' ')]
print(Counter(words))
file.close()
