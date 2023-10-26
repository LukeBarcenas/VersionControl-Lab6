# Luke Barcenas

def encoder(password):
    encoded_pass = []
    for i in range(len(password)):
        temp_char = 0
        temp_char = int(password[i]) + 3
        if int(temp_char) >= 10:
            temp_char = int(temp_char) % 10
            encoded_pass.append(temp_char)
        else:
            encoded_pass.append(temp_char)
    encoded_pass = "".join([str(i) for i in encoded_pass])
    return encoded_pass


if __name__ == "__main__":
    user_input = 0

    while True:
        print("\nMenu\n-------------")
        print("1. Encode\n"
              "2. Decode\n"
              "3. Quit\n\n")
        user_input = input("Please enter an option: ")

        if user_input == "1":
            user_pass = input("Please enter your password to encode: ")
            encoded_password = encoder(user_pass)
            print("Your password has been encoded and stored!\n\n")

        elif user_input == "2":
            pass  # call to decoder function goes here

        elif user_input == "3":
            break
