## Примеры тестирования кода
### В качестве условия принято реальное ТЗ на https://freelance.habr.com

ТЗ для тестирования находится в файле <TZ_test_code.txt>

в рамках проекта рассмотрено 2 варианта:
- 1 вариант: модуль <unittest> запуск - test_unit.py
- 2 вариант: рукописный тест - tests_manual.py

* при тестировании курсор должен быть в консоли. Используется модуль <keyboard> для ввода ожидаемых данных.

### локально проект доступен по ссылке:
- git@github.com:SergSukh/code_testing_examples.git
### установка окружения и зависимостей последовательный ввод команд:
$python -m venv venv
$source venv/scripts/activate
$pip install -r req.txt

### Запуск тестирования в активированном виртуальном окружении:
$ python tests_manual.py # полностью рукописный тест
$ python tests_unit.py # тест на основе unittest