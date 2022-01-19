

rating1 = input("From a scale of 1-5 how cute is this picture: ")
# testing to make sure that the inputs are integers
try:
    x = int(rating1)
except ValueError:
    error_Message = " {} is not an integer please only input integers "
    print(error_Message.format(rating1))
    rating1 = input("From a scale of 1-5 how cute is this picture?: ")
while x > 5 or x < 1:
    rating1 = input("please follow directions...From a scale of 1-5 how cute is this picture?: ")
    x = int(rating1)


rating2 = input("ok how cute is this one: ")
# testing to make sure that the inputs are integers
try:
    y = int(rating2)
except ValueError:
    error_Message = " {} is not an integer please only input integers "
    print(error_Message.format(rating2))
    rating2 = input("ok how cute is this one: ")
    y = int(rating1)
while y > 5 or y < 1:
    rating2 = input("please follow directions...From a scale of 1-5 how cute is this one?: ")
    y = int(rating1)




rating3 = input("Now what about this picture: ")
# testing to make sure that the inputs are integers
try:
    z = int(rating3)
except ValueError:
    error_Message = " {} is not an integer please only input integers "
    print(error_Message.format(rating3))
    rating3 = input("Now what about this picture?: ")
while z > 5 or z < 1:
    rating3 = input("please follow directions...From a scale of 1-5 what about this picture?: ")
    z = int(rating1)


# this is the algorithm grading the users rating of the pictures
def grading():

    if x + y + z >= 13:
        print("Wow! You thought these pics were A+ , glad you liked them so much!")
        return

    if x + y + z >= 12:
        print("Glad you liked them! You gave these pics a B")
        return

    if x + y + z >= 10:
        print("huh guess these pictures were just ok, you gave them a C")
        return

    if x + y + z >= 9:
        print("oh geez not a fan i guess... you gave these pictures an D")
        return

    else:
        print("you didn't really like these did you... these pictures didn't pass ")


grading()
