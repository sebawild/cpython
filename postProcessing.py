from collections import Counter 

def readFile(fileName):
	fileObj = open(fileName, "r") 
	words = fileObj.read().splitlines()
	fileObj.close()
	return words 

def printCounter(fileName): 
	x = readFile(fileName)
	y = Counter(x)
	print(y) 

def printSortedCounter(fileName): 
        x = readFile(fileName)
        y = Counter(x)
        print(sorted(y.items()))

def returndict(fileName): 
	x = readFile(fileName)
	z = dict((y,x.count(y)) for y in set(x))
	return z 

def sortedList(fileName):
	x = returndict(fileName)
	dic = {}
	for i in x:
		dic[int(i)] = x[i]
	print(sorted(dic.items())) 

sortedList("output.txt")

