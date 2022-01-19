X = input("what number do you wanna test?: ")
x = 6
y = x / 2

try:
    test_Number = int(x)
except ValueError:
    error_Message = " {} is not an integer please only test integers "
    print(error_Message.format(x))

if x / y == 2:
    even_Msg = " {} is an even number "
    print(even_Msg.format(x))

else:
    odd_Msg = " {} is an odd number "
    print(odd_Msg.format(x))


