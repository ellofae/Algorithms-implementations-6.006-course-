# Peak Finder algorithms. Staight-forward-search algorithm. Two-dimensional version:
# Worst case complexity: O(n*m)

import random

def peak_finder(Matrix):
    init_colomn = random.randrange(5)
    init_row = random.randrange(5)
    current_num = Matrix[init_row][init_colomn]
    count = 0
    while(True):
        current_num = Matrix[init_row][init_colomn]
        print("\nmatric coef: ", current_num)
        print("coords: ", init_row, ";", init_colomn)

        if init_colomn > 0:
            if current_num <= Matrix[init_row][init_colomn - 1]:
                init_colomn = init_colomn - 1
                continue
            else:
                pass
        if init_colomn < 4:
            if current_num <= Matrix[init_row][init_colomn + 1]:
                init_colomn = init_colomn + 1
                continue
            else:
                pass
        if init_row > 0:
            if current_num <= Matrix[init_row - 1][init_colomn]:
                init_row = init_row - 1
                continue
            else:
                pass
        if init_row < 4:
            if current_num <= Matrix[init_row + 1][init_colomn]:
                init_row = init_row + 1
                continue
            else:
                pass

        return current_num
        break;

def main():
    n, m = 5, 5
    Matrix = [[0 for x in range(n)] for y in range(m)]

    for i in range(5):
        for j in range(5):
            Matrix[i][j] = random.randrange(1,101,1)
    print("Matrix: ")
    for i in range(n):
        print(Matrix[i])

    print("2D peak: ", peak_finder(Matrix))

main()
