from digitalSign import generate_key, hash_message, sign_message, verify

if __name__ == "__main__":
    generate_key()
    
    while True:
        default_msg = "This is a confidential document!"
        
        choice = input("\n1. Press 1 to sign the default message\n2. Press 2 to sign your own message\n3. Press 3 to verify messages\n4. Exit\nEnter your choice: ")
        
        if choice == "1":
            message = default_msg
            hashed_message = hash_message(message)
            signature = sign_message(message, hashed_message)
            print("The message has been successfully signed and stored")
        elif choice == "2":
            message = input("Enter the message you want to sign: ")
            hashed_message = hash_message(message)
            signature = sign_message(message, hashed_message)
            print("The message has been successfully signed and stored")
        elif choice == "3":
            verify()
        elif choice == "4":
            print("Exiting...")
            break #keluar from loop
        else:
            print("Invalid choice. Please try again.")

    print("Thanks for using our program... \n Credit to : Rusdi and Syazwan")