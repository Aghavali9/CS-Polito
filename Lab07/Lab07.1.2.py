from random import randint


def main():
    number_list = [randint(1, 100) for _ in range(10)]
    print('-' * 60)
    print(f'Random int list: {number_list}')
    print('-'*60)
    even_index = []
    even_value = []
    for i, e in enumerate(number_list):
        if i % 2 == 0:
            even_index.append(e)

        if e % 2 == 0:
            even_value.append(e)
    print(f"All elements of even index: {even_index}")
    print('-'*60)
    print(f"All elements of even value: {even_value}")
    print('-'*60)
    print(f"All elements in reverse order:\n{number_list[::-1]}")
    print('-'*60)
    print(f"First Element: {number_list[0]} Last Element: {number_list[-1]}")
    print('-'*60)


if __name__ == '__main__':
    main()
