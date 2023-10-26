# Luke Barcenas

# encoder function, adds 3 to each number in the password
def encoder(password):
    encoded_pass = []
    # goes through each number in the string, adds 3, and
    # puts them in a new list
    for i in range(len(password)):
        temp_char = 0
        temp_char = int(password[i]) + 3
        if int(temp_char) >= 10:
            temp_char = int(temp_char) % 10
            encoded_pass.append(temp_char)
        else:
            encoded_pass.append(temp_char)
    # the list is made into a string
    encoded_pass = "".join([str(i) for i in encoded_pass])
    return encoded_pass


if __name__ == "__main__":
    user_input = 0

    # menu loop
    while True:
        print("\nMenu\n-------------")
        print("1. Encode\n"
              "2. Decode\n"
              "3. Quit\n\n")
        user_input = input("Please enter an option: ")

        # if the user types '1', run the encoder
        if user_input == "1":
            user_pass = input("Please enter your password to encode: ")
            encoded_password = encoder(user_pass)
            print("Your password has been encoded and stored!\n\n")

        # if the user types '2', run the decoder
        elif user_input == "2":
            pass  # call to decoder function goes here

        # if the user types '3', end the program
        elif user_input == "3":
            break
