import json
import re
import textwrap
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


def date_format(date):
    """
    Возвращает дату операции в формате ДД.ММ.ГГГГ
    """
    date_only = date[:10]
    date_in_list = date_only.split("-")
    date_form = '.'.join(date_in_list[::-1])
    return date_form


def encoding_number(number):
    """
    Возвращает замаскированный номер карты
    (видны первые 6 цифр и последние 4,
    разбито по блокам по 4 цифры, разделенных пробелом)
    или
    возвращает замаскированный номер счета
    (видны только последние 4 цифры)
    """
    nums = re.findall(r'\d+', number)
    nums_only = str([int(i) for i in nums][0])
    if len(nums_only) == 16:
        num_in_list = textwrap.wrap(nums_only, 4)
        num_in_list[1] = num_in_list[1][:2] + '**'
        num_in_list[2] = '****'
        encoding_num = ' '.join(num_in_list)
    else:
        encoding_num = "**" + nums_only[-4:]
    return encoding_num


def print_operations():
    """
    Выводит на экран данные по последним 5 выполненным операциям
    """
    pass
