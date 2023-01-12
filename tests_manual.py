import time

import keyboard

from base import CMD, input_cmd
from fixtures.fixtures_cmd import (cmd_list_1, cmd_list_2, cmd_list_3,
                                   cmd_list_4_m, cmd_list_5_m, cmd_list_6)
from fixtures.fixtures_res import (res_list_1, res_list_2, res_list_3,
                                   res_list_4, res_list_5, res_list_6)
from fixtures.tests_name import test_name


def test_case(test_cmd, res):
    patients = [1] * 201
    i = 0
    while True:
        key = ''
        if type(test_cmd[i]) == list:
            for _ in test_cmd[i]:
                key += str(_) + '\n'
        else:
            key = test_cmd[i]+'\n'
        keyboard.write(key)
        print('\nIN:')
        cmd = str(input('Введите команду: '))
        text = input_cmd(cmd)(patients)
        result = (text if type(text) == str else CMD[text[0]](patients, text[1]))
        print('\nOUT:\n', result)
        assert (result == res[i], f'Команда {test_cmd[i]} выполнена некорректно')
        i += 1
        if text == 'Сеанс завершён.':
            break


def test():
    now = time.time()
    for test_num in range(len(test_cmd)):
        st_time = time.time()
        print(test_name[test_num])
        test_case(test_cmd[test_num], res[test_num])
        print(f'>>>  Тест успешно пройден за {time.time()-st_time} сек.')
    print(f'>>>  Тестирование успешно завершеноузнать статус пациента {time.time()-st_time} сек.')

if __name__ == '__main__':
    test_cmd = [cmd_list_1, cmd_list_2, cmd_list_3, cmd_list_4_m, cmd_list_5_m, cmd_list_6]
    res = [res_list_1, res_list_2, res_list_3, res_list_4, res_list_5, res_list_6]
    test()