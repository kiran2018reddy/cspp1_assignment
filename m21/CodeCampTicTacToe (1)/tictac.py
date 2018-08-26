def main():
    matrix = []
    i = 0
    while i < 3:
        lst = input().split(" ")
        matrix.append(lst)
        i = i+1
    if checkInput(matrix):
        if checkGame(matrix):
            checkWinner(matrix)
        else:
            print("invalid game")
    else:
        print("invalid input")
def checkGame(matrix):
    count_o = 0
    count_x = 0
    for row in matrix:
        for i in row:
            if i == "o":
                count_o += 1
            elif i == "x":
                count_x += 1
    if abs(count_x - count_o) == 1 or abs(count_x - count_o) == 0:
        return True
    return False
def checkInput(matrix):
    for i in matrix:
        for j in i:
            if j not in "o x .":
                return False
    return True
def rows(matrix):
    Winner_x = False
    Winner_o = False
    for row in matrix:
        if row.count("x") == 3:
            Winner_x = True
        if row.count("o") == 3:
            Winner_o = True
    if Winner_o and Winner_x:
        print("invalid game")
        exit()
    if Winner_x:
        return(True,"x")
    if Winner_o:
        return(True,"o")
    return (False,0)
def column(matrix):
    transpose = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(matrix[j][i])
        transpose.append(row)
    return rows(transpose)
def diagonal(matrix):
    d1 = []
    for i in range(len(matrix)):
        d1.append(matrix[i][i])
    if d1.count("o") == 3:
        return (True, "o")
    if d1.count("x") == 3:
        return (True, "x")
    d2 = []
    j = len(matrix[0]) - 1
    for i in range(len(matrix)):
        d2.append(matrix[i][j])
        j = j - 1
    if d1.count("o") == 3:
        return (True, "o")
    if d2.count("x") == 3:
        return (True, "x")
    return (False,0)


def checkWinner(matrix):
    if rows(matrix)[0]:
        print(rows(matrix)[1])
    elif column(matrix)[0]:
        print(column(matrix)[1])
    elif diagonal(matrix)[0]:
        print(diagonal(matrix)[1])
    else:
        print("draw")
if __name__ == '__main__':
    main()
