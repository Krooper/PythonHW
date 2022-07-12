import shutil
import os


def main(argv):
    # Зашли директорию my_project
    os.chdir('my_project')

    # Переместили шаблоны из одной директории в директорию my_project
    shutil.copytree('mainapp/templates/mainapp', 'templates/mainapp', dirs_exist_ok=True)
    # Удалили то, что было
    shutil.rmtree('mainapp/templates')

    # Переместили шаблоны из одной директории в директорию my_project
    shutil.copytree('authapp/templates/authapp', 'templates/authapp', dirs_exist_ok=True)
    # Удалили то, что было
    shutil.rmtree('authapp/templates')

    # Вышли из директории my_project
    os.chdir('..')
    return 0


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))