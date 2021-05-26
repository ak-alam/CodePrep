'''
Write a program to find the missing number in an unordered integer array of size 99
and containing number from 1 to 100
e.g if input = [1,2,4,6]
missing output will be 5
'''

def sorted_missing_number(lst):
    initial_val = 1
    missing = 0
    if initial_val == lst[initial_val + 1]:
        missing += initial_val
        initial_val += 1
    return missing



def unsorted_missing_number(lst):
    n = len(lst)
    total = (n+1) * (n+2) / 2
    sum_arr = sum(lst)
    return total - sum_arr


#print(unsorted_missing_number([2,5,7,8,3]))

print(sorted_missing_number([1,2,3,4,6]))