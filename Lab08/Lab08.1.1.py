"""[1.1] Out-of-range. Write a program that contains an out-of-range error. What happens if you run the program?"""


# Lab08.1.1

def main():
    int_list = [1, 2, 3, 4, 5, 6]
    print(int_list[6])  # IndexError: list index out of range


if __name__ == '__main__':
    main()
