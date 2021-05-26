""" 
write a program to print the following output
*****
****
***
****
*****
"""
def star_patterns(num):
    for rows in range(num + 1, 0, -1):
        for _ in range(0, rows - 1):
            print('*', end='')
        print(' ')
    for rows in range(1, num+1):
        for _ in range(1, rows+1):
            print('*', end= '')
        print('')
 
star_patterns(5)
