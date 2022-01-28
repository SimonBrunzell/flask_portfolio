
def evenOdd():

    X = input("what number do you wanna test?: ")
    x = int(X)

    y = int(x / 2)

    try:
        X = int(x)
    except ValueError:
        error_Message = " {} is not an integer please only test integers "
        print(error_Message.format(x))

    if x / y == 2:
        even_Msg = " {} is an even number "
        print(even_Msg.format(x))

    else:
        odd_Msg = " {} is an odd number "
        print(odd_Msg.format(x))

evenOdd()

def playAgain():
    while 2 == 2:
        response = input("do you wanna try again?: ")
        if response == "yes" or "y" or "yes please" or "si" or "yeah" or "si por favor":
            print("ok")
            evenOdd()

playAgain()


