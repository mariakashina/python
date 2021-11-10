from itertools import zip_longest
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
distribution = (list(zip_longest(tutors, klasses))[i] for i in range(0, len(tutors) + 1))
print(next(distribution))
print(next(distribution))
