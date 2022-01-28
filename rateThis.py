

# for first input
# ok making the ratings global fixing everything camp!
global rating1
rating1 = input("From a scale of 1-5 how cute is this picture: ")
# testing to make sure that the inputs are integers
try:
    x = int(rating1)
except ValueError:
    error_Message = " {} is not an integer please only input integers "
    print(error_Message.format(rating1))
    rating1 = input("From a scale of 1-5 how cute is this picture: ")

    if rating1 == "1":
        x = int(rating1)

    elif rating1 == "2":
        x = int(rating1)

    elif rating1 == "3":
        x = int(rating1)

    elif rating1 == "4":
        x = int(rating1)

    elif rating1 == "5":
        x = int(rating1)

    else:
        error_Message = " {} is not an integer since you can't follow directions you don't get to play "
        print(error_Message.format(rating1))
        x = int(3000)

while 2999 > x > 5 or x < 1:
    rating1 = input("please follow directions...From a scale of 1-5 how cute is this picture?: ")
    x = int(rating1)


#
# for second input
rating2 = input("ok how cute is this one: ")
# testing to make sure that the inputs are integers
try:
    y = int(rating2)
except ValueError:
    error_Message = " {} is not an integer please only input integers "
    print(error_Message.format(rating2))
    rating2 = input("ok how cute is this one: ")
    y = int(rating2)

    if rating2 == "1":
        y = int(rating2)
    elif rating2 == "2":
        y = int(rating2)
    elif rating2 == "3":
        y = int(rating2)
    elif rating2 == "4":
        y = int(rating2)
    elif rating2 == "5":
        y = int(rating2)
    else:
        error_Message = " {} is not an integer since you can't follow directions you don't get to play "
        print(error_Message.format(rating2))
        y = int(3000)

while y > 5 or y < 1:
    rating2 = input("please follow directions...From a scale of 1-5 how cute is this one?: ")
    y = int(rating2)


#
# for third input
rating3 = input("Now what about this picture: ")
# testing to make sure that the inputs are integers

try:
    z = int(rating3)
except ValueError:
    error_Message = " {} is not an integer please only input integers "
    print(error_Message.format(rating3))
    rating3 = input("Now what about this picture?: ")

    if rating3 == "1":
        z = int(rating3)
    elif rating3 == "2":
        z = int(rating3)
    elif rating3 == "3":
        z = int(rating3)
    elif rating3 == "4":
        z = int(rating3)
    elif rating3 == "5":
        z = int(rating3)
    else:
        error_Message = " {} is not an integer since you can't follow directions you don't get to play "
        print(error_Message.format(rating3))
        z = int(3000)

while z > 5 or z < 1:
    rating3 = input("please follow directions...From a scale of 1-5 what about this picture?: ")
    z = int(rating3)


#
# this is the algorithm grading the users rating of the pictures
def grading():

    if x + y + z >= 3000:
        print("thought you beat the system huh.... Nope I just wasted your time you don't get a grade")

    if 2999 > x + y + z >= 13:
        print("Wow! You thought these pics were A+ , glad you liked them so much!")
        return

    if 2999 > x + y + z >= 12:
        print("Glad you liked them! You gave these pics a B")
        return

    if 2999 > x + y + z >= 10:
        print("huh guess these pictures were just ok, you gave them a C")
        return

    if 2999 > x + y + z >= 9:
        print("oh geez not a fan i guess... you gave these pictures an D")
        return

    if x + y + z < 9:
        print("you didn't really like these did you... these pictures didn't pass ")


grading()
