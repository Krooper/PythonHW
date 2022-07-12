from csv import writer


def main(argv):
    program, *args = argv
    with open('bakery.csv', 'a', encoding='utf-8') as bakery_file:
        bakery_writer = writer(bakery_file)
        bakery_writer.writerow(args)
    return 0


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
