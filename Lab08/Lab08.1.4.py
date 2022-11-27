"""[1.4] Table.
Write the instructions for the execution of the following operation for a table in Python of 𝑚 rows and 𝑛 columns
(dimensions are inserted by the user):

Initialize the table with values equal to zero (0)
Fill all the cells with values equal to one (1)
Fill the cells alternating 0 and 1 in a chess scheme
Fill with 0 only the cells of the upper row and of the lower one, leaving the rest of the table unchanged;
Fill with 1 only the cells of the right column and of the left column, leaving the rest of the table unchanged;
Calculate and display the sum of all the elements
After each operation, display the table!"""


# Lab08.1.4

def main():
    m, n = get_numbers()
    table = [[0] * n for _ in range(m)]
    print(f'\nStep 1:\n')
    print_table(table)
    print(f'\nStep 2:\n')
    table = [[1] * n for _ in range(m)]
    print_table(table)
    print(f'\nStep 3:\n')
    table = [[0] * n for _ in range(m)]
    for i in range(m):
        if i % 2 == 0:
            for j in range(n):
                if j % 2 == 0:
                    table[i][j] = 1
        else:
            for j in range(n):
                if j % 2 != 0:
                    table[i][j] = 1
    print_table(table)
    print(f'\nStep 4:\n')
    for i in range(n):
        table[0][i] = 0
        table[-1][i] = 0
    print_table(table)
    print(f'\nStep 5:\n')
    for i in range(m):
        table[i][0] = 1
        table[i][-1] = 1
    print_table(table)
    print(f'\nStep 6:\n')
    print(f'Sum of all elements is {sum_table(table)}')


def get_numbers():
    m = input("Number of rows:\n\t>>> ")
    n = input("Number of columns:\n\t>>> ")
    flag_1 = True
    while flag_1:
        if not validator(m) or not validator(n):
            m = input("Please enter valid number of rows:\n\t>>> ")
            n = input("Please enter valid number of columns:\n\t>>> ")
        else:
            flag_1 = False
    return int(m), int(n)


def validator(x):
    return x.isdigit()


def print_table(table):
    for row in table:
        for element in row:
            print(f"{element:4d}", end='')
        print()


def sum_table(table):
    x = []
    for row in table:
        x.append(sum(row))
    return sum(x)


if __name__ == '__main__':
    main()
