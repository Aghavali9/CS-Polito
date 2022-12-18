"""1.1 Counting words.
Write a program counting all occurrences of a word in a text file whose name is obtained as an input.
Assume the file contains only alphabetical characters or white spaces. The program shall output all the words in the file,
with the number of occurrences near each word."""

# Lab11.1.1

def main():
    occurrences = dict()
    file_name = input(f'Please enter the file name.\n\t>>> ')
    contents = reader(file_name)
    key_container = [_ for _ in set(contents)]
    for item in key_container:
        occurrences[item] = lookup(contents, item)
    for elements in occurrences:
        print(f'{elements}: {occurrences[elements]}')


def reader(file) -> list:
    """Reads all the lines of a text file into a list of words"""
    try:
        with open(file) as f:
            list_ = [_.strip('(),.?!').lower() for _ in  f.read().split()]
    except OSError as err:
        print(err)
        exit(1)
    return  list_

def lookup(raw_list: list, word: str) -> int:
    """Searches for a word inside a list and returns the number of occurrences of that word"""
    counter = 0
    for words in raw_list:
        token = words.strip('(),.?!').lower()
        if word.lower() == token:
            counter += 1

    return counter



if __name__ == '__main__':
    main()
