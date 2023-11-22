import json
from operator import itemgetter


def read_from_json():
    """
    Считывает данные из JSON и возвращает список
    """
    with open("operations.json", encoding="utf8") as file:
        data = json.load(file)
    return data


def sort_by_state():
    """
    Возвращает новый список только с выполненными (EXECUTED) операциями
    (1 сортировка)
    """
    sorted_by_state_list = []
    unsorted_list = read_from_json()
    for operation in unsorted_list:
        for key, value in operation.items():
            if value == "EXECUTED":
                sorted_by_state_list.append(operation)
    return sorted_by_state_list


def sort_by_date():
    """
    Возвращает отсортированный по дате (по убыванию) новый список
    (2 сортировка)
    """
    unsorted_list = sort_by_state()
    sorted_by_date_list = sorted(unsorted_list, key=itemgetter("date"), reverse=True)
    return sorted_by_date_list


def date_format():
    """
    Возвращает дату операции в формате ДД.ММ.ГГГГ
    """
    pass


def encoding_card_number():
    """
    Возвращает замаскированный номер карты
    (видны первые 6 цифр и последние 4,
    разбито по блокам по 4 цифры, разделенных пробелом)
    """
    pass


def encode_account_number():
    """
    Возвращает замаскированный номер счета
    (видны только последние 4 цифры и 2 символа "*" перед ними)
    """
    pass


def print_operations():
    """
    Выводит на экран данные по последним 5 выполненным операциям
    """
    pass
