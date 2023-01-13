from commands import CMD

patients = [0] * 200


def input_cmd(cmd):
    """Проверка полученной команды"""
    if cmd.lower() in CMD:
        return CMD[cmd.lower()]
    return CMD['error']


def main():
    """Основной блок вывода информации"""
    while True:
        cmd = str(input('Введите команду'))
        text = input_cmd(cmd)(patients)
        print(text if type(text) == str else CMD[text[0]](patients, text[1]))
        if text == 'Сеанс завершён.':
            break


if __name__ == '__main__':
    main()