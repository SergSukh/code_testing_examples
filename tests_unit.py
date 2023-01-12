import unittest

import keyboard

from base import input_cmd
from commands import CMD
from fixtures.fixtures_cmd import (cmd_list_1, cmd_list_2, cmd_list_3,
                                   cmd_list_4, cmd_list_5, cmd_list_6)
from fixtures.fixtures_res import (res_list_1, res_list_2, res_list_3,
                                   res_list_4, res_list_5, res_list_6)


class TestHospitalCMD(unittest.TestCase):
    """Тестируем функции"""

    def test_hospital_cmd(self):
        """=== Приёмочный тест № 1 (базовый сценарий) ==="""
        patients = [1] * 200
        for _ in range(len(cmd_list_1)):
            if type(cmd_list_1[_]) == list:
                self.assertEqual(
                    CMD[cmd_list_1[_][0]](patients, (cmd_list_1[_][1])-1),
                    res_list_1[_],
                    f'Команда <{cmd_list_1[_][0]}> для пациента <{cmd_list_1[_][1]}> работает некорректно.' )
            else:
                self.assertEqual(
                    CMD[cmd_list_1[_]](patients),
                    res_list_1[_],
                    f'Команда <{cmd_list_1[_]}> работает некорректно.' )

    def test_unnow_cmd(self):
        """=== Приёмочный тест № 2 (неизвестная команда) ==="""
        patients = [1] * 200
        for _ in range(len(cmd_list_2)):
            self.assertEqual(
                input_cmd(cmd_list_2[_])(patients),
                res_list_2[_],
                f'Команда <{cmd_list_2[_]}> работает некорректно.'
            )
    
    def test_error_data(self):
        """=== Приёмочный тест № 3 (случаи ввода пользователем некорректных данных) ==="""
        patients = [1] * 200
        for _ in range(len(cmd_list_3)):
            if type(cmd_list_3[_]) == list:
                self.assertEqual(
                    CMD[cmd_list_3[_][0]](patients, (cmd_list_3[_][1])),
                    res_list_3[_],
                    f'Команда <{cmd_list_3[_][0]}> для пациента <{cmd_list_3[_][1]}> работает некорректно.' )
            else:
                self.assertEqual(
                    CMD[cmd_list_3[_]](patients),
                    res_list_3[_],
                    f'Команда <{cmd_list_3[_]}> работает некорректно.' )

    def test_disharge_true(self):
        """=== Приёмочный тест № 4 (попытка повысить самый высокий статус, которая приводит к выписке пациента) ==="""
        patients = [1] * 200
        keyboard.write('да\n')  # Ответ на вопрос в коде
        for _ in range(len(cmd_list_4)):
            if type(cmd_list_4[_]) == list:
                self.assertEqual(
                    CMD[cmd_list_4[_][0]](patients, (cmd_list_4[_][1])),
                    res_list_4[_],
                    f'Команда <{cmd_list_4[_][0]}> для пациента <{cmd_list_4[_][1]}> работает некорректно.'
                )
            else:
                self.assertEqual(
                    CMD[cmd_list_4[_]](patients),
                    res_list_4[_],
                    f'Команда <{cmd_list_4[_]}> работает некорректно.'
                )

    def test_disharge_false(self):
        """=== Приёмочный тест № 5 (попытка повысить самый высокий статус, которая ни к чему не приводит) ==="""
        patients = [1] * 200
        keyboard.write('нет\n') # Ответ на вопрос в коде
        for _ in range(len(cmd_list_5)):
            if type(cmd_list_5[_]) == list:
                self.assertEqual(
                    CMD[cmd_list_5[_][0]](patients, (cmd_list_5[_][1])),
                    res_list_5[_],
                    f'Команда <{cmd_list_5[_][0]}> для пациента <{cmd_list_5[_][1]}> работает некорректно.'
                )
            else:
                self.assertEqual(
                    CMD[cmd_list_5[_]](patients),
                    res_list_5[_],
                    f'Команда <{cmd_list_5[_]}> работает некорректно.'
                )

    def test_status_down_false(self):
        """=== Приёмочный тест № 6 неудачная попытка понизить самый низкий статус) ==="""
        patients = [1] * 200
        for _ in range(len(cmd_list_6)):
            if type(cmd_list_6[_]) == list:
                self.assertEqual(
                    CMD[cmd_list_6[_][0]](patients, (cmd_list_6[_][1])),
                    res_list_6[_],
                    f'Команда <{cmd_list_6[_][0]}> для пациента <{cmd_list_6[_][1]}> работает некорректно.'
                )
            else:
                self.assertEqual(
                    CMD[cmd_list_6[_]](patients),
                    res_list_6[_],
                    f'Команда <{cmd_list_6[_]}> работает некорректно.'
                )


if __name__ == '__main__':
    unittest.main()