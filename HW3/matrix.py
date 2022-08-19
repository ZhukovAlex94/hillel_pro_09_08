import random

M = int(input("Type your M, M > 5:\n"))

matrix = [[random.randint(1, 50) for _ in range(M)] for _ in range(M)]


def print_matrix():
    sum_row = list(map(sum, zip(*matrix)))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]:<3}", end=" ")
        print()
    print("----"*M)
    for i in range(len(sum_row)):
        print(sum_row[i], end=" ")
    print("\n\n")


def bubble_sort():
    sum_row = list(map(sum, zip(*matrix)))
    length = len(sum_row)

    for i in range(length):
        for j in range(0, length-i-1):
            if sum_row[j] > sum_row[j+1]:
                for k in range(len(matrix)):
                    temp = matrix[k][j]
                    matrix[k][j] = matrix[k][j+1]
                    matrix[k][j+1] = temp
                temp = sum_row[j]
                sum_row[j] = sum_row[j + 1]
                sum_row[j + 1] = temp

    for k in range(len(matrix)):
        for i in range(length):
            for j in range(0, length-i-1):
                if matrix[j][k] > matrix[j + 1][k] if k % 2 else matrix[j][k] < matrix[j + 1][k]:
                    temp = matrix[j][k]
                    matrix[j][k] = matrix[j + 1][k]
                    matrix[j + 1][k] = temp


print_matrix()
bubble_sort()
print_matrix()
