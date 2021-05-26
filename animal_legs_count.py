''' 
In this challenge, a farmer is asking you to tell him
how many legs can be counted among all his animals.
The farmer breeds three species:
chicken = 2 legs
cows = 4 legs
pigs = 4 legs

The farmer has counted his animals and he gives you the
a subtotal for each species, you have to implement a function
that returns the total numbers of legs of all the animals. 


'''

def animanl_legs_count(chicken_c, cows_c, pigs_c):
    
    chicken_c *= 2
    cows_c *= 4
    pigs_c *= 4

    return chicken_c + cows_c + pigs_c


print(animanl_legs_count(1, 1, 1))