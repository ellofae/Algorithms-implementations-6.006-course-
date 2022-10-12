# Peak Finder algorithms. Straight-forward algorithm. One-dimensional version:
# Worst case complexity: O(n)

import random

def peak_finder(list):
    for i in range(0, len(list)-1):
        if i != 0 and i != len(list)-1:
            if list[i] >= list[i-1] and list[i] >= list[i+1]:
                return list[i]
        else:
            if i == 0:
                if list[i] >= list[i + 1]:
                    return list[i]
            else:
                if (list[i] >= list[i - 1]):
                    return list[i]

def main():
    list = []
    for i in range(10):
        list.append(random.randrange(1,101,1))

    print("\nlist: ", list)
    print("The peak is(not nesseserely the most interesting one): ", peak_finder(list))

main()

