"""[1.5] Second possibility.
Write a program that asks the user to enter a series of values of type float.
When the user enters a value that is not of the correct type, the program must give the user a second chance to enter the value,
and after two chances it must stop reading the input, terminating the program immediately.
Data entry continues until the user enters an empty string ('') as input.
Sum all correctly specified values and display their sum when the user has finished entering data.
Use exception handling to detect improper input."""

# Lab10.1.5

def main():
    chances = 2
    floats = []
    while chances != 0:
        try:
            input_ = input(f'Enter floats, (empty to end).\n\t{chances} {"chance" if chances == 1 else "chances"} remaining\n\t>>> ')
            float_ = float(input_)
        except ValueError:
            if not input_:
                break
            print(f'{"Please enter a valid float number" if chances > 1 else "GAME OVER"}')
            chances -= 1
        else:
            floats.append(float_)
    print(f'Sum of the correctly entered values is: {sum(floats)}')



if __name__ == '__main__':
    main()
