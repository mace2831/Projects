
#Aaron Maciag 12/17/2024 aaronjmaciag@gmail.com
#Create an algorithm that checks a two-dimensional array and determine if it is magic
#All elements of the array must be unique
#All columns, rows, and diagonal sums must equal the same number
def IsMagicSquare(matrix):
    sums = []
    #check that the matrix is a square and all the numbers are uniqu
    if (len(matrix) == len(matrix[0])) & (HasUniqueNums(matrix) == True):
        #sum colums
        sums +=[sum(col) for col in zip(*matrix)]
        #sum rows
        sums += [sum(row) for row in matrix]
        #sum reverse diagonal
        sums += [sum(matrix[i][len(matrix) - i - 1] for i in range(len(matrix)))]
        #sum diagonal
        sums += [sum(matrix[i][i] for i in range(len(matrix)))]
        #check that all of the sums are the same
        if sums.count(sums[0]) == len(sums):
            return True

    return False

#function to check that all the numbers in the matrix are unique
def HasUniqueNums(matrix):
    nums_seen = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] in nums_seen:
                return False
            else:
                nums_seen.append(matrix[i][j])
    return True


if __name__ == '__main__':
    #Non Magic Squares
    square = [[1, 2, 3],[4,5,6],[7,8,9]]
    notSquare = [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    #Magic Squares
    magic = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    magic2 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

    print('Is {} a magic square?? {}'.format(square,IsMagicSquare(square)))
    print('Is {} a magic square?? {}'.format(square,IsMagicSquare(magic)))
    print('Is {} a magic square?? {}'.format(square, IsMagicSquare(notSquare)))
    print('Is {} a magic square?? {}'.format(square, IsMagicSquare(magic2)))

