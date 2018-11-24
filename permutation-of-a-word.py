from itertools import permutations 
  
def allPermutations(str): 
       
    # Get all permutations of string 'ABC' 
    permList = permutations(str) 
    # print all permutations 
    for perm in list(permList):
        list1.append((''.join(perm)))
    return list1
        
# Driver program 
if __name__ == "__main__": 
    str = 'bin'
    list1 = []
    allPermutations(str) 
    print(list1)
