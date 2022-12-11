"""[1.4] Hotel.
The administrative manager of a hotel records sales in a text file. Each line contains the following 4 information,
separated by semicolon characters (';'):
I. the client's name; II. the service sold; III. the amount paid; IV. the date of the event.
The services sold may be, for example, a dinner, a conference, or lodging.
The proper format for this file is for it to contain 4 fields per line, and for the amount paid to contain values of type float.
Write a program that reads this text file, and displays the total amount for each type of service,
reporting an error if the file does not exist or if its format is incorrect."""

# Lab10.1.4
FILE = 'Hotel.txt'


def main():
    try:
        contents = reader(FILE)
    except FileNotFoundError as err:
        print(err)
        exit(1)
    data = organizer(contents)
    for elements in data:
        if len(elements) != 4 and isinstance(elements[2], float):
            print('Format is incorrect')
            exit(1)
    dinner, lodging, conference = aggregator(data)
    print(f'Dinner: {dinner:.2f}\nLodging: {lodging:.2f}\nConference: {conference:.2f}')


def reader(file) -> list:
    """Reads all the lines of a text file into a list"""
    with open(file) as f:
        list_ = [e.rstrip('\n') for e in f.readlines()]
    return  list_

def organizer(raw_list: list) -> tuple:
    """Divides the lines by ; and stores them and returns a tuple"""
    tmp_list = []
    for elm in raw_list:
        items = tuple([e.strip() for e in elm.split(';')])
        tmp_list.append(items)
    return tuple(tmp_list)


def aggregator(raw_list: tuple) -> float:
    """Sums every service's value and returns it"""
    dinner = 0
    conference = 0
    lodging = 0
    for element in raw_list:
        if 'dinner' in element:
            dinner += float(element[2])
        elif 'lodging' in element:
            lodging += float(element[2])
        else:
            conference += float(element[2])
    return dinner, conference, lodging


if __name__ == '__main__':
    main()
