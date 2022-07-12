import os


def main(argv):
    # Создали директорию my_project (если она не существует)
    dir_name = 'my_project'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    # Зашли директорию my_project
    os.chdir('my_project')
    # Создали все остальные директории в my_project (если они не существуют)
    dir_name = 'settings'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    dir_name = 'mainapp'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    dir_name = 'adminapp'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    dir_name = 'authapp'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    # Вернулись в корень
    os.chdir('..')
    # Проверили, что вернулись и что всё создано
    print(os.listdir(path="."))
    print(os.listdir(path="my_project"))

    return 0


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
