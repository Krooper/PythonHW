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
    dir_name = 'authapp'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    # Создали нужные файлы в директории settings
    open('settings/__init__.py', 'w')
    open('settings/dev.py', 'w')
    open('settings/prod.py', 'w')

    # Создали нужные файлы в директории mainapp
    open('mainapp/__init__.py', 'w')
    open('mainapp/models.py', 'w')
    open('mainapp/views.py', 'w')
    # Зашли туда, создали там доп. директории, вышли
    os.chdir('mainapp')
    dir_path = os.path.join('templates', 'mainapp')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    os.chdir('..')
    # Создали нужные файлы в этих директориях
    open('mainapp/templates/mainapp/base.html', 'w')
    open('mainapp/templates/mainapp/index.html', 'w')


    # Создали нужные файлы в директории authapp
    open('authapp/__init__.py', 'w')
    open('authapp/models.py', 'w')
    open('authapp/views.py', 'w')
    # Зашли туда, создали там доп. директории, вышли
    os.chdir('authapp')
    dir_path = os.path.join('templates', 'authapp')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    os.chdir('..')
    # Создали нужные файлы в этих директориях
    open('authapp/templates/authapp/base.html', 'w')
    open('authapp/templates/authapp/index.html', 'w')

    # Вышли из директории my_project
    os.chdir('..')

    return 0


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
