# Для хобби используем список как изменяемый класс
# (на случай, если пользователь захочет его изменить в последствии)
# Для ФИО - сначала список (чтобы была возможность тоже его менять), а потом преобразуем в строку
# (чтобы была возможность добавлять в качестве ключа словаря)
# Для ФИО + хобби - словарь (чтобы у пользователя была возможность добавлять/менять хобби
# и при этом не появлялся новый ключ)

users_list = []
hobby_list = []
user_hobby_dict = {}

# Читаем первый файл, убираем \n (для этого делаем список) и объединяем обратно в строку
# (чтобы была возможность добавлять в качестве ключа словаря),
# потом заполняем список строками
with open('users.csv', 'r', encoding='utf-8') as users:
    for line in users:
        line = line.split(',')
        line[-1] = line[-1].replace('\n', '')
        user = ','.join(line)
        users_list.append(user)

# Читаем второй файл, убирать \n (для этого делаем список)
# потом заполняем список списками
with open('hobby.csv', 'r', encoding='utf-8') as hobbies:
    for line in hobbies:
        line = line.split(',')
        line[-1] = line[-1].replace('\n', '')
        hobby_list.append(line)


# Заполняем словарь
for number in range(len(users_list)):
    if number < len(hobby_list):
        user_hobby_dict[users_list[number]] = hobby_list[number]
    else:
        user_hobby_dict[users_list[number]] = None
print(user_hobby_dict)

# Записываем словарь в файл
# Режим w+ используется, чтобы файл создавать
with open('users_hobby.txt', 'w+', encoding='utf-8') as users_hobby:
    for key, value in user_hobby_dict.items():
        users_hobby.write(f'{key}, {value}\n')
