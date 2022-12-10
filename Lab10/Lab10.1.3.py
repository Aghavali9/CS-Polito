"""[1.3] Ring search.
Write a program that searches for a given word in the contents of a group of files. The program must ask the user for input:
I. A list of file names on a single line, separated by commas;
II. A word to search. File names must be stored in a list, while the word to be searched must be stored in a variable.
The program must display all lines that contain the word, even as a substring of other words,
without distinguishing between uppercase and lowercase letters.
Each displayed line must be preceded by the name of the file in which it is located."""

# Lab10.1.3
# '10000_days.txt, back_in_black.txt, The_Ensemble_of_Silence.txt'

def main():

    final_query = []
    file_list = get_file_names()
    keyword = get_keyword()
    for files in file_list:
        try:
            contents = reader(files).split('\n')
            matches = lookup(contents, keyword)
        except FileNotFoundError as err:
            print(err)
            exit(1)
        for items in matches:
            final_query.append(f'{files}: {items}')
    if not final_query:
        print(f'Sorry, "{keyword}" was not found in the files.')
    else:
        for elements in final_query:
            print(f'{elements}')

def reader(file) -> str:
    with open(file, 'r') as f:
        return f.read()


def lookup(doc_list: list, keyword: str) -> list:
    """Searches for a keyword in a list and returns a list of lines containing the keyword"""
    lines = []
    for i, docs in enumerate(doc_list):
        tokens = docs.split()
        normalized = [token.rstrip('.,').lower() for token in tokens]
        if keyword.lower() in normalized:  # searching for the exact match
            lines.append(docs)
        elif ' '.join(normalized).find(keyword.lower()) >= 0:  # searching in the substrings, this can be deleted to return exact matches only.
            lines.append(docs)
    return lines

def get_file_names() -> list:
    """Gets the file name from user"""
    input_ = input('Enter file names with , between names.\n\t>>> ')
    temp_list = input_.split(',')
    normalized = [e.strip() for e in temp_list]
    return normalized

def get_keyword() -> str:
    """Gets the keyword we want to look up in the files"""
    input_ = input('What do you wanna look for?\n\t>>> ')
    return input_

if __name__ == '__main__':
    main()
