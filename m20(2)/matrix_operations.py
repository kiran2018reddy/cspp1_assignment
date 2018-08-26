def mult_matrix(m1_, m2_):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    result = []
    if len(m1_[0]) == len(m2_):
        for i1_ in range(len(m1_)):
            resTemp = []
            for j1_ in range(len(m2_[0])):
                res = 0
                for k1_ in range(len(m2_)):
                    res += m1_[i1_][k1_]*m2_[k1_][j1_]
                resTemp.append(res)
            result.append(resTemp)
        return result
    else:
        print("Error: Matrix shapes invalid for mult")
        return None

def add_matrix(m1_, m2_):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    # for i in m1:
    #     for j in m2:
    #         len(i)!=len(j)
    #         return "Error: Matrix shapes invalid for addition"
    #     else:
    #         print(similar)
    #     for i in range(len(m1)):#iterate through rows
    #         for j in range(len(m2[0])):#iterate through coloums
    #             result[i][j] = m1[i][j] + m2[i][j]
    # for r in result:
    #     print(r)
    if len(m1_) != len(m2_):
        print("Error: Matrix shapes invalid for addition")
        return None
    for i1_ in range(len(m1_)):
        if len(m1_[i1_]) != len(m2_[i1_]):
            print("Error: Matrix shapes invalid for addition")
            return None
    result = []
    for i1_ in range(len(m1_)):
        row = []
        for j1_ in range(len(m1_[0])):
            add = m1_[i1_][j1_] + m2_[i1_][j1_]
            row.append(add)
        result.append(row)
    return result       
                
                

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    rows, columns = [int(i1_) for i1_ in input().split(",")]
    matrix = []
    for i1_ in range(rows):
        lst = [int(i1_) for i1_ in input().split(" ")]
        if len(lst) != columns:
            print("Error: Invalid input for the matrix")
            return None
        matrix.append(lst)
    return matrix
   
    

def main():
    # read matrix 1
    m1_ = read_matrix()

    # read matrix 2
    m2_ = read_matrix()
    if (m1_ != None and m2_ != None):
        print(add_matrix(m1_, m2_))
        print(mult_matrix(m1_, m2_))
        

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2

if __name__ == '__main__':
    main()
