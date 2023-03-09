# elliot jordan

def encode(to_encode):
    pass


def decode(to_decode):
    pass


def main():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")
    user_choice = input("Please enter an option: ")
    if user_choice == 1:
        to_encode = input()
        encode(to_encode)
    elif user_choice == 2:
        pass
    elif user_choice == 3:
        quit()

if __name__ == "__main__":
    main()
