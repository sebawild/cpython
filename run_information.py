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
            

x = readFile("arrays.txt")
runs_list = []

for i in range(0,(len(x))):
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
    
    runs_list.append([int(a[0]),a[2],no_of_runs, no_of_runs2, max_len,max_len2, b, runs, runs2])
    
#now if we sort in terms of run length 
runs_list.sort(reverse = True)
print("the array prints them in the format: length, merge cost, no of runs (increasing only), no of runs (increasing and decreasing), max length (increasing only), max length (inc/dec), array, run_length array(inc), run len array (inc/dec) ")
print(runs_list[0])
