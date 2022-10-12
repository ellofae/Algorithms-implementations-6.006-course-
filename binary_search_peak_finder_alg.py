# Peak Finder algorithms. Binary-search algorithm. One-dimensional version:
# Worst case complexity: O(log n) (log base: 2)

import random
import math

def peak_finder(arg):
    list = arg

    while(True):
        half = len(list) // 2
        if half != 1:
            if (list[half] <= list[half - 1]):
                list = list[:half]
            elif (list[half] <= list[half + 1]):
                list = list[half + 1:]
            else:
                return list[half]
                break;
        else:
            if list[0] != list[1]:
                return max(list)
                break;
            else:
                print("Not found")
                break

def main():
    list = []
    for i in range(10):
        list.append(random.randrange(1,101,1))

    #list = [88, 73, 39, 96, 53, 36, 19, 17, 50, 2]

    print("\nlist: ", list)
    print("The peak is(not nesseserely the most interesting one): ", peak_finder(list))

main()

