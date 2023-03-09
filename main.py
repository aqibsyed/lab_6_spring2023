def encode(my_pass):
    new_pass = ''
    for x in str(my_pass):
        x = int(x) + 3
        if x > 9:
            x -= 10
        new_pass = new_pass + str(x)

    return new_pass


def decode(my_pass):
    pass


if __name__ == "__main__":
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")

        option = input("Please enter an option: ")
        if option == '1':
            my_pass = input("Please enter your password to encode: ")
            encode(my_pass)
            print("Your password has been encoded and stored!\n")

        elif option == '2':
            print(
                f"The encoded password is {encode(my_pass)}, and the original password is {decode(encode(my_pass))}.\n")
# comment
        elif option == '3':
            break
        else:
            print("bruh\n")
