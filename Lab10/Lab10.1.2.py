"""[1.2] From the bottom.
Write a program that reads all the lines in a text file input.txt, reverses their order, and writes them to another
 file output.txt."""

# Lab10.1.1

FILE = './input_2.txt'


def main():
    try:
        input_file = reader(FILE)
    except FileNotFoundError as err:
        print(err)
        exit(1)
    lines = input_file.split('\n')
    for index, element in enumerate(reversed(lines[:-1])):
        writer('./output_2.txt', element)


def reader(file):
    with open(file, 'r') as f:
        return f.read()


def writer(file, line):
    with open(file, 'a') as f:
        f.write(f'{line}\n')


if __name__ == '__main__':
    main()
