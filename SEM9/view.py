# Модуль для ввода/вывода информации


def choose() -> str:
    """"Выбор режима работы приложения"""
    return input('Выберете режим работы: ')


def get_expr() -> str:
    """"Запрашивает у пользователя задачу"""
    return input('Введите пример: ')


def show_res(res: str):
    """Выводит результат"""
    print(res)


def erorr_mode():
    """Выводит сообщение об ошибке выбора режима"""
    pass
    print('Такого режима нет')


def show_history(history: str):
    """Выводит истроию оперций"""
    print(history.split('/n'))
    for i in history.split('/n'):
        print(i.replace(';','-> результат '))
