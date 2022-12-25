"""2.2 Genes."""
# Lab11.2.2

FILE = './genetic_code.csv'  # Make sure to put this file in the same directory as the code file before testing


def main():
    genetic_code = get_genetic_code()

    gene_sequence = get_input()

    sliced_sequence = slicer(gene_sequence)

    translated_seq = ""

    for genes in sliced_sequence:
        translated_seq += genetic_code[genes]
    print(translated_seq)


def get_genetic_code() -> dict:
    """Reads the file and returns a dictionary of the genetic codes"""
    temp_dict = dict()
    temp_list = list()

    try:
        with open(FILE) as in_file:
            for line in in_file:
                temp_list.append(line.split(',', maxsplit=1))
    except OSError as err:
        print(err)
        exit(1)

    for element in temp_list:
        element[1] = element[1].strip('"\n')  # Removes the unwanted characters from the read file

    for pairs in temp_list[:-2]:
        codon_list = [_.strip() for _ in pairs[1].split(',')]
        for codons in codon_list:
            temp_dict[codons] = pairs[0]

    return temp_dict


def get_input() -> str:
    """mRNA inserted as an input from the user"""
    flag_1 = False
    allowed_characters = 'GAUC'
    while not flag_1:
        usr_inp = input(f'Please enter the mRNA sequence\n(Sample: GUAUGCACGUGACUUUCCUCAUGAGCUGAU)\n\t>>> ')
        if not usr_inp:
            print('Empty? seems like and end to me.')
            exit(1)
        for char in usr_inp:
            if char.upper() not in allowed_characters:
                print('Invalid CODON, try again.')
                break
        else:
            flag_1 = True
    return usr_inp.upper()


def slicer(seq: str) -> list:
    """Gets the gene sequence and slices it into a list, and also checks the validity of the sequence"""
    start = ['AUG', 'GUG']
    end = ['UAG', 'UGA', 'UAA']
    for x in range(len(seq) - 2):
        if seq[x: x + 3] in start:
            start_i = x
            break
    else:
        print('No starting gene found')
    list_ = [seq[i: i + 3] for i in range(start_i, len(seq) - 2, 3)]
    for i, e in enumerate(list_):
        if e in end:
            end_i = i
            break
    else:
        print('No ending gene found')
        exit(1)

    return list_[:end_i]


if __name__ == '__main__':
    main()
