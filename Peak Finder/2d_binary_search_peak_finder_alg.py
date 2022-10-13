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

def peak_finder(Matrix, i, j):  # algorithm for odd matrix (like 5x5,7x7)
    half_colomn_cord = j // 2

    ################ looking for a 2D peak in a colomn and in a row ##################

    list = []  # colomn of half_colomn_cord
    for k in range(i):
        list.append(Matrix[k][half_colomn_cord])

    global_max_j = max(list)
    i_index_of_global_max_j = list.index(global_max_j)  # index of global_max_j compared to rows.

    list.clear()
    for k in range(j):
        list.append(Matrix[i_index_of_global_max_j][k])  # list of i's row

    possible_2d_peak = binary_peak_finder(list)
    ################ looking for a 2D peak in a colomn and in a row ##################

    if(half_colomn_cord != 1):
        if (list.index(global_max_j) > list.index(possible_2d_peak)):
            # range_j = j - (j - list.index(possible_2d_peak) + 1)  - for even matrix
            range_j = j - (list.index(possible_2d_peak) + 1)
            new_Matrix = [[0 for x in range(range_j)] for y in range(i)]
            for l in range(i):
                for m in range(range_j):
                    new_Matrix[l][m] = Matrix[l][m]
            return peak_finder(new_Matrix, i, range_j)

        elif (list.index(global_max_j) < list.index(possible_2d_peak)):
            # range_j = j - (list.index(possible_2d_peak) + 1) - for even matrix
            range_j = j - (list.index(global_max_j) + 1)
            new_Matrix = [[0 for x in range(range_j)] for y in range(i)]
            for l in range(i):
                for m in range(range_j):
                    new_Matrix[l][m] = Matrix[l][list.index(binary_peak_finder(list)) + m]
            return peak_finder(new_Matrix, i, range_j)
        else:
            return possible_2d_peak
    else:
        return possible_2d_peak


def main():
    i, j = 7, 7  # algorithm works for an odd matrix, otherwise: change choose conditions in '#' in 'if else' clause
    Matrix = [[0 for x in range(i)] for y in range(j)]

    for l in range(i):
        for m in range(j):
            Matrix[l][m] = random.randrange(1,101,1)
    print("Matrix: ")
    for value in range(i):
        print(Matrix[value])

    matrix_size = "({0}x{1})".format(i,j)
    print("2D peak of odd matrix {0}: {1}".format(matrix_size, peak_finder(Matrix, i, j)))

main()
