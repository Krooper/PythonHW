tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Андрей',
    'Юлия', 'Сергей', 'Полина', 'Анна'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def tut_klass(tutors_list, klasses_list):
    current = 0
    while current < len(tutors):
        if current >= len(klasses_list):
            std_tupl = (tutors_list[current], None)
        else:
            std_tupl = (tutors_list[current], klasses_list[current])
        yield std_tupl
        current += 1


students = tut_klass(tutors, klasses)

for i in range(16):
    print(next(students))
