'''
Create a list of all odd numbers between 1 and a max number. 
Max number is something you need to take from a user using input() 
function
'''

def odd_list():
    '''
    Input: User will input a number (max number)

    return: a odd list from range of 1 to max 
            number give by the user. 
    '''
    max_num = int(input('Enter a number: '))
    odd_lst = []
    for i in range(1, max_num +1):
        if i % 2 != 0:
            odd_lst.append(i)
    return odd_lst
    

a = odd_list()
print(a)