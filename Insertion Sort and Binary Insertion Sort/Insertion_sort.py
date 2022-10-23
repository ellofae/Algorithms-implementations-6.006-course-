# Insertion sort algorithm implementation
# Worst Complexity of an algorithm: O(n^2)
# Best Complexity of an algorithm: O(n)
#
# Complexity for Comparing: O(n^2)
#            for Swaping: O(n^2)
#
# T(n) = c1*n * c2*(n-1) = n * (n-1) = n^2 - n = n^2 => O(n^2)

import sys
import random

def InsertionSort(list):
    if len(list) == 0:
        sys.exit()

    for i in range(1,len(list)): # O(n)
        key = i
        count = 0
        while count < key: # O(n)
            if list[key-count] < list[key - count - 1]:
                (list[key-count], list[key-count-1]) = PairwiseSwap(list[key-count], list[key - count - 1])
                count += 1
            else:
                break
    
    return list
                
            
def PairwiseSwap(a,b):
    temp = a
    a = b
    b = temp
    return (a, b)     
            

def main():
    arr = []
    for i in range(20):
        arr.append(random.randint(0,100))

    print(f"initial array(size - {len(arr)}): {arr}")
    print(f"sorted array(size - {len(arr)}): {InsertionSort(arr)}")

main()
