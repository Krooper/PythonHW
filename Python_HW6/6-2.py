def row_reader(file):
    counter = 0
    row_list = []
    for row in file:
        if counter % 2 == 0:
            row = row.replace('\n', '')
            row_list.append(row)
        counter += 1
    return row_list


def main(argv):
    program, *args = argv
    with open('bakery.csv', 'r', encoding='utf-8') as bakery_file:
        if len(args) == 0:
            row_list = row_reader(bakery_file)
            for el in row_list:
                print(el)

        elif len(args) == 1:
            row_list = row_reader(bakery_file)
            i = int(args[0])-1
            while i < len(row_list):
                print(row_list[i])
                i += 1

        elif len(args) == 2:
            row_list = row_reader(bakery_file)
            start = int(args[0])-1
            finish = int(args[1])
            i = start
            while i < finish:
                print(row_list[i])
                i += 1
    return 0


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
