
def main():

    numbers = get_numbers()
    print(f"weird sum is = {weird_sum(numbers)}")


def get_numbers():
    user_input = input("Please enter int:\n\t>>> ")
    list_ints = []
    while user_input:
        if not validator(user_input):
            user_input = input("Please enter valid int:\n\t>>> ")
        else:
            list_ints.append(int(user_input))
            user_input = input("Please enter another int:\n\t>>> ")
    return list_ints


def validator(x):
    return x.isdigit()


def weird_sum(raw_list):
    modified_list = []
    for i, e in enumerate(raw_list):
        if i % 2 != 0:
            modified_list.append(e * -1)
        else:
            modified_list.append(e)
    total = sum(modified_list)
    return total


if __name__ == '__main__':
    main()
