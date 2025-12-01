from typing import Any, Dict, List

"""Функция filter_by_state , принимает список словарей и опционально
   значение ключа state (по умолчанию 'EXECUTED'. Возвращает новый список
   словарей, содержащий только те словари, у которых ключ state соответствует
   указаному значению"""


def filter_by_state(data_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    filtered_list = []
    for item in data_list:
        if item.get("state") == state:
            filtered_list.append(item)

    return filtered_list


"""Функция sort_by_date ,принимает список словарей и необязательный параметр, 
   задающий порядок сортировки (по умолчанию-убывание). Функция возвращает новый 
   список, отсортированный подате """


def sort_by_date(data_list: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортируем список словарей  по ключю key присваивая значение date через
    функцию lambda, убывание организуем через reverse и аннотацию типов bool=True"""
    return sorted(data_list, key=lambda item: item["date"], reverse=reverse)


# if __name__ == "__main__":
#     test_data = [
#         {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
#     ]
#
# result = filter_by_state(test_data)
# print(result)
#
#
# result = sort_by_date(test_data)
# print(result)
