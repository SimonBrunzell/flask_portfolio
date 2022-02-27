def palindrome():
    inputted_word = input("provide a word to check if it's a palindrome :D: ")

    length = int(len(inputted_word) / 2)

    index_front = 0
    index_back = len(inputted_word) - 1

    check = 0

    for index in range(0, length):
        first = inputted_word[index_front]
        last = inputted_word[index_back]
        if first.lower() == last.lower():
            index_front = index_front + 1;
            index_back = index_back - 1;
            check = check + 1;
        else:
            index = length
            
    if check == length:
        print("congrats! the word", inputted_word, "is a palindrome")
    else:
        print("your word", inputted_word, "is not a palindrome")

palindrome()

