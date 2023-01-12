from const import STATUS, SYM


def input_patient(patients:list, num=None):
    if not num:
        num = input('Введите ID пациента: ')
    for s in str(num):
        if s not in SYM:
            return 'Ошибка. ID пациента должно быть числом (целым, положительным)'
    if int(num) < 1:
        return 'Ошибка. ID пациента должно быть числом (целым, положительным)'
    if int(num) > 200 or patients[int(num)] not in STATUS:
        return 'Ошибка. В больнице нет пациента с таким ID'
    return int(num)


def calculate_statistics(patients):
    sum_patients = len(patients) - patients.count('')
    res = (f'В больнице на данный момент находится {sum_patients} чел., из них:\n')
    for status in (0, 1, 2, 3):
        if status in patients:
            res += (f'- в статусе "{STATUS[status]}": {patients.count(status)} чел.\n')
    return res


def discharge(patients, num=None):
    num = input_patient(patients, num)
    if type(num) == str:
        return num
    patients[num] = ''
    return 'Пациент выписан из больницы'
    

def get_status(patients, num=None):
    num = input_patient(patients, num)
    if type(num) == str:
        return num
    return f'Статус пациента: "{STATUS[patients[num]]}"'


def status_down(patients, num=None):
    num = input_patient(patients, num)
    if type(num) == str:
        return num
    if patients[num] == 0:
        return 'Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)'
    patients[num] -= 1
    return f'Новый статус пациента: "{STATUS[patients[num]]}"'


def status_up(patients, num=None):
    num = input_patient(patients, num)
    if type(num) == str:
        return num
    if patients[num] == 3:
        return 'Желаете этого клиента выписать? (да/нет): ', num
    patients[num] += 1
    return f'Новый статус пациента: "{STATUS[patients[num]]}"'


def check_patient(patients, num):
    answer = input('Желаете этого клиента выписать? (да/нет): ').lower()
    if answer == 'да':
        return discharge(patients, num)
    return 'Пациент остался в статусе "Готов к выписке"'


def stop(patients):
    return 'Сеанс завершён.'


def err_except(patients):
    return 'Неизвестная команда! Попробуйте ещё раз'
