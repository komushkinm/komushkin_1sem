

if __name__ == "__main__":
    pass # Ваш код здесь

students = ["Комушкин", "Сулимов", "Шкарупин", "Шакиров", "Фомин",
           "Руденко", "Бакшаев", "Кравченко", "Демченко", "Ким"]


grades = [
    [4, 5, 3, 4, 5],
    [3, 4, 3, 3, 4],
    [5, 5, 5, 5, 5],
    [4, 3, 4, 4, 3],
    [3, 3, 2, 3, 3],
    [5, 4, 5, 4, 5],
    [4, 4, 4, 4, 4],
    [3, 2, 3, 3, 2],
    [5, 5, 4, 5, 4],
    [4, 4, 3, 4, 4]
]

subjects = ["Алгебра", "Геометрия", "Русский язык", "Литература", "Информатика"]

avg_grades = []

for i in range(len(students)):
    avg_in_time = sum(grades[i]) / len(grades[i])
    avg_grades.append(avg_in_time)
    print(f'{students[i]}, средний балл: , {str(round(avg_in_time, 2))}')
print('')
for j in range(len(subjects)):
    grades_of_subject = [grades[i][j] for i in range(len(students))]

    maxx_gr = max(grades_of_subject)
    minn_gr = min(grades_of_subject)
    avg_gr_of_subject = sum(grades_of_subject) / len(grades_of_subject)


    print(f'\n{subjects[j]}')
    print(f'макс. оценка: {maxx_gr}')
    print(f'мин. оценка: {minn_gr}')
    print(f'средняя оценка: {avg_gr_of_subject}')

best_st_index = avg_grades.index(max(avg_grades))
nebest_st_index = avg_grades.index(min(avg_grades))


print(f'\nс лучшими баллами: {students[best_st_index]}')
print(f'с худшими баллами: {students[nebest_st_index]}')
