from digitalSign import hash_message, sign_message, verify

if __name__ == "__main__":
    # generate_key()
    # print("The keys have been generated")

    default_msg = "This is a confidential document!"

    print("Enter your Choice : ")
    choice = input("Press 1 to sign the default message,press 2 to sign your own message, 3 to verify the message's integrity: ")
    if int(choice) == 1:
        message = default_msg
        hashed_message = hash_message(message)
        signature = sign_message(message,hashed_message)
        print("The message has been successfully signed and stored")
    elif int(choice) == 2:
        message = input("Enter the message you wanted to sign : ")
        hashed_message = hash_message(message)
        signature = sign_message(message,hashed_message)
        print("The message has been successfully signed and stored")
    elif int (choice) == 3:
        verify()



