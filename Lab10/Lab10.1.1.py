"""[1.1] Enola Gay.
Write a program that reads the text file input.txt, and writes each line read in the file output.txt preceded by its line number
 inserted as a comment between characters '/*' and ' */'."""

# Lab10.1.1

FILE = './input_1.txt'


def main():
    try:
        input_file = reader(FILE)
    except FileNotFoundError as err:
        print(err)
        exit(1)
    lines = input_file.split('\n')
    for index, element in enumerate(lines[:-1], start= 1):
        writer('./output_1.txt', index, element)


def reader(file):
    with open(file, 'r') as f:
        return f.read()


def writer(file, line_no, line):
    with open(file, 'a') as f:
        f.write(f'/*{line_no}*/')
        f.write(f'{line}\n')


if __name__ == '__main__':
    main()
