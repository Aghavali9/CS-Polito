"""[1.5] Lists union.
Write a function merge(a, b) that merges the two lists a and b, alternating one element of the first and one element of the second.
If one list is shorter than the other, the items are alternated as long as possible, then the items left in the longer list are added, in-order.
Starting lists should not be changed.
If, for example, the content of a is 1 4 9 16 and the content of b is 9 7 4 9 11,
the invocation of merge(a, b) returns a new list composed of the following values: 1 9 4 7 9 4 16 9 11."""


# Lab08.1.5

def main():
    a = [1, 4, 9, 16]
    b = [9, 7, 4, 9, 11]
    print(merger(a, b))


def merger(a, b):
    temp_list = []
    difference = abs(len(a) - len(b))
    for i in zip(a, b):
        for e in i:
            temp_list.append(e)
    if len(a) > len(b):
        temp_list.extend(a[-difference:])
    else:
        temp_list.extend(b[-difference:])
    return temp_list


if __name__ == '__main__':
    main()
