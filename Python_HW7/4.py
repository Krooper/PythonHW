import os


def main(argv):
    size_dict = {}
    os.chdir('some_data')
    for file in os.listdir(os.getcwd()):
        file_size = os.stat(file).st_size
        i = 1
        while file_size/10 > 1:
            file_size /= 10
            i += 1
        if (10 ** i) not in size_dict:
            size_dict[10 ** i] = 1
        else:
            size_dict[10 ** i] += 1
    os.chdir('..')
    print(size_dict)

    return 0


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))