age1 = 21
age2 = 16

def sort_age(age1, age2):
    if (age1 > age2):
        temp = age2
        age2 = age1
        age1 = temp
        print("your sorting function sorted ages to: ", age1, age2)
    else:
        print("your sorting function sorted ages to: ", age1, age2)

sort_age(age1, age2)

matrix = [ [1,2,3],[4,5,6],[7,8,9] ]
def print_square(matrix):
    for x in matrix:
        print("printing the matrix printed: ", *x)


print_square(matrix)
