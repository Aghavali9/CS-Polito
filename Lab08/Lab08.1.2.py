"""[1.2] Buffer
Write the pseudocode for an algorithm that, given a list of defined length, moves the elements "forward" one position
(thus increasing their index by one unit), and moves the element at the last position to the first position.
For example, the list 1 7 9 3 0 4, after this operation, becomes the list: 4 1 7 9 3 0.
Write a program implementing the above described algorithm."""


# Lab08.1.2

def main():
    int_list = [1, 7, 9, 3, 0, 4]
    buffer = []
    print(f'{"-" * 45}\nOriginal List :\t{int_list}')
    buffer.insert(0, int_list[-1])
    for i in int_list[:-1]:
        buffer.append(i)
    print(f'{"-" * 45}\nModified List :\t{buffer}\n{"-" * 45}')


if __name__ == '__main__':
    main()
