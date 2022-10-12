# Peak Finder algorithms. Binary-search algorithm. Two-dimensional version:
# Worst case complexity: O(n*log m) (log base: 2)
import random

def binary_peak_finder(list):
    while (True):
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

def peak_finder(Matrix, i, j):
    half_colomn_cord = j // 2
    list = []
    for k in range(i):
        list.append(Matrix[k][half_colomn_cord])

    global_max_j = max(list)
    i_index = list.index(global_max_j)

    list.clear()
    for k in range(j):
        list.append(Matrix[i_index][k])

    return binary_peak_finder(list)



def main():
    i, j = 5, 5
    Matrix = [[0 for x in range(i)] for y in range(j)]

    for l in range(i):
        for m in range(j):
            Matrix[l][m] = random.randrange(1,101,1)
    print("Matrix: ")
    for value in range(i):
        print(Matrix[value])

    print("2D peak: ", peak_finder(Matrix, i, j))

main()
