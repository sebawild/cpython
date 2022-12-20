#import math
#import random 
#A = [random.randint(0,1000) for x in range(10)]
"""
has to be ran using python3
if print to file true then prints if not then it doesn't   
"""
printToFile = False
printArray = False 
fileName = "arrays.txt"
filePrintName ="pyflate_longest_array.txt"



COMPARISONS = 0
class CmpCounter:
    def __init__(self, value):
        self._value = value
    def __lt__(self, other):
        if not isinstance(other, CmpCounter):
            raise NotImplementedError
        global COMPARISONS
        COMPARISONS += 1
        return self._value < other._value
    def __eq__(self, other):
        raise NotImplementedError
    def __gt__(self, other):
        raise NotImplementedError
    def __le__(self, other):
        raise NotImplementedError
    def __ge__(self, other):
        raise NotImplementedError
    def __ne__(self, other):
        raise NotImplementedError
    def __str__(self):
        return self._value.__str__()
    
#def lgNFac(n):
#    s = 0
#    for i in range(2,n+1):
#        s += math.log2(i)
#    return s

def my_key(x) :
    return CmpCounter(x)

#s = sorted(A, key=my_key, reverse=False)

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words


def find_runs(array, increasing_only = True):

    runs = []
    if increasing_only == True: 
        i = 0 
        while i < len(array):
            j=1
            while i < (len(array)-2) and array[i] <= array[i+1] :
                i += 1
                j += 1                
            runs.append(j)
            i += 1
    else: 
        i = 0 
        while i < len(array):
            j=1
            if i < (len(array)-2) and array[i] <= array[i+1]:
                while i < (len(array)-2) and array[i] <= array[i+1] :
                    i += 1
                    j += 1 
            elif i < (len(array)-2) and array[i] > array[i+1]:
                while i < (len(array)-2) and array[i] > array[i+1] :
                    i += 1
                    j += 1
            runs.append(j)
            i+=1
                
                
    return runs
 
x = readFile(fileName)
runs_list = []

for i in range(0,(len(x))):
    COMPARISONS = 0
    a = x[i].split("#")
    b = a[1].split(",")
    for j in range(0, len(b)):
        b[j] = int(b[j]) 
    runs = find_runs(b,True)
    runs2 = find_runs(b,False)
    no_of_runs = len(runs)
    no_of_runs2 = len(runs2)
    max_len = max(runs)
    max_len2 = max(runs2)
    runs_sorted = sorted(b, key=my_key, reverse=False)
    compar = COMPARISONS

    
    runs_list.append([ int(a[0]),a[3],a[2],no_of_runs, no_of_runs2, max_len,max_len2, compar, b, runs, runs2])
    
#now if we sort in terms of run length 
runs_list.sort(reverse = True)
#print("the array prints them in the format: length,sort_type,  merge cost, no of runs (increasing only), no of runs (increasing and decreasing), max length (increasing only), max length (inc/dec), comaprisons, array, run_length array(inc), run len array (inc/dec) ")
#print(runs_list[0][:8])
#print(runs_list[0][0])
print("The length of the array is", runs_list[0][0])
print("The sort method used was:", runs_list[0][1])
print("The mergecost is:", runs_list[0][2])
print("The number of runs (increasing only) is:", runs_list[0][3])
print("The number of runs (increasing and decreasing) is:", runs_list[0][4])
print("The max length of a run (increasnig only) is:", runs_list[0][5])
print("The max length of a run (increasing and decreasing) is:", runs_list[0][6]) 
print("The number of comparisons when sorting is:", runs_list[0][7])
if printArray == True: print("The Array is:", runs_list[0][8])

if printToFile == True: 
	print("File has with longest array printed to" , filePrintName)
	f = open(filePrintName, 'w')
	for i in runs_list[0][8]:
		f.write(str(i))
		f.write(",")

	f.close()
	print("The arrays has been printed to file:", filePrintName)

