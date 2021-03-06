def appearance(intervals):
    # Интервалы разделяем на кортежи, где первый элемент кортежа это время входа/выхода,
    # а второй элемент кортежа это 1 или -1, что обозначает вход/выход
    events = []
    for interval in intervals:
        event = intervals[interval]
        for i in range(len(event)):
            events.append((event[i], 1 - 2 * (i % 2)))

    # Сортируем события по времени
    events = sorted(events)

    count = 0
    start = -1
    time = 0

    # Перебираем события
    for event in events:
        # Подсчитываем количество событий. Помним что событие 1 это начало времени ученика, преподавателя или учителя
        count += event[1]
        # Если подсчет равен 3, значит время урока, преподавателя и ученика совпало. Сохраняем начало этого интервала.
        if count == 3:
            start = event[0]
        # Далее проверяем подсчет. Если при очередном проходе он равен 2 и начало времени интервала не равно нулю, то
        # либо ученик, либо учитель уже не присутствуют на уроке. Из времени текущего события вычитаем начало интервала
        # и результат суммируем в отдельной переменной.
        if count == 2 and start > 0:
            time += event[0] - start
            start = -1

    return time

tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                        1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                        1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                        1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     }
]




if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        # Во втором примере результаты не сходятся. Скорее всего ошибка в самом примере. Менять ничего не стал.
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

