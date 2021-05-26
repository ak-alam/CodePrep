def diagonal_difference(arr):

    
    lef_diag = []
    right_diag = []
    arr_len = len(arr)

    for i in range(arr_len):
        for j in range(arr_len):
            if (i == j):
                lef_diag.append(arr[i][j])
            if (i + j) == (len(arr) - 1):
                right_diag.append(arr[i][j])

    arr_diff = sum(lef_diag) - sum(right_diag)
    return abs(arr_diff)

arr = [[1, 2, 3], 
      [4, 5, 6],
      [9, 8, 9 ]]        

    

val = diagonal_difference(arr)
print(val)