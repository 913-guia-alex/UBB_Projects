# Main.py

from FA import FA


def main():
    fa = FA("C:\\Users\\Alex\\PycharmProjects\\Lab2LFTC\\fa.in")
    print("1. Print states")
    print("2. Print alphabet")
    print("3. Print output states")
    print("4. Print initial state")
    print("5. Print transitions")
    print("6. Check word")
    print("7. Get matching substring")
    print("0. Exit")

    while True:
        option = int(input("> "))
        if option == 1:
            fa.print_states()
        elif option == 2:
            fa.print_alphabet()
        elif option == 3:
            fa.print_output_states()
        elif option == 4:
            fa.print_initial_state()
        elif option == 5:
            fa.print_transitions()
        elif option == 6:
            word = input("Enter word: ")
            print(f"Accepted: {fa.check_accepted(word)}")
        elif option == 7:
            word = input("Enter word: ")
            accepted = fa.get_next_accepted(word)
            if accepted is None:
                print("No matching substring")
            else:
                print(f"Matching substring: {accepted}")
        elif option == 0:
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
