import sys
import math
import random

filename = "arrays.txt"
printNLongestLists = 1
# use command line to get file name
if len(sys.argv) > 1:
    filename = sys.argv[1]
if len(sys.argv) > 2:
    printNLongestLists = int(sys.argv[2])

print("Reading file: ", filename)
print("Printing ", printNLongestLists, " longest lists")

# A = [random.randint(0,1000) for x in range(10)]
global COMPARISONS
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


# def lgNFac(n):
#    s = 0
#    for i in range(2,n+1):
#        s += math.log2(i)
#    return s

def my_key(x):
    return CmpCounter(x)


# s = sorted(A, key=my_key, reverse=False)

def readFile(fileName):
    """Reads a file and returns an array of the lines in the file."""
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    return words


def find_runs(array, increasing_only=True):
    runs = []
    if increasing_only == True:
        i = 0
        while i < len(array):
            j = 1
            while i < (len(array) - 2) and array[i] <= array[i + 1]:
                i += 1
                j += 1
            runs.append(j)
            i += 1
    else:
        i = 0
        while i < len(array):
            j = 1
            if i < (len(array) - 2) and array[i] <= array[i + 1]:
                while i < (len(array) - 2) and array[i] <= array[i + 1]:
                    i += 1
                    j += 1
            elif i < (len(array) - 2) and array[i] > array[i + 1]:
                while i < (len(array) - 2) and array[i] > array[i + 1]:
                    i += 1
                    j += 1
            runs.append(j)
            i += 1

    return runs


runs_list = []

for line in readFile(filename):
    # Format of lines: length, rank-reduced array, merge cost, Powersort|Timsort
    # example: 10#9,3,8,4,0,5,1,2,7,6#0#Powersort
    a = line.split("#")
    length = int(a[0])
    mergecost = int(a[2])
    sort_type = a[3]
    COMPARISONS = 0
    r = [ int(s) for s in a[1].split(",") ]
    runs = find_runs(r, True)
    runs2 = find_runs(r, False)
    no_of_runs = len(runs)
    no_of_runs2 = len(runs2)
    max_len = max(runs)
    max_len2 = max(runs2)
    runs_sorted = sorted(r, key=my_key) # run sort to trigger comparisons
    compar = COMPARISONS
    # Append dictionary of stats
    runs_list.append({
        "length": length,
        "sort_type": sort_type,
        "merge_cost": mergecost,
        "no_of_runs (inc only)": no_of_runs,
        "no_of_runs (inc/dec)": no_of_runs2,
        "max_len (inc only)": max_len,
        "max_len (inc/dec)": max_len2,
        "comparisons": compar,
        "array": r,
        "runs (inc only)": runs,
        "runs (inc/dec)": runs2
    })
    #runs_list.append(int(a[0]), a[3], a[2], no_of_runs, no_of_runs2, max_len, max_len2, compar, b, runs, runs2])

# now if we sort in terms of run length
# sort runs_list by length
runs_list.sort(key=lambda x: x["length"], reverse=True)

for i in range(printNLongestLists):
    print(i)
    # Get dict without array
    d = runs_list[i].copy()
    del d["array"]
    del d["runs (inc only)"]
    del d["runs (inc/dec)"]
    print(d)
