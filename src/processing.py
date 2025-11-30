from typing import List, Dict, Any


"""Функция filter_by_state , принимает список словарей и опционально
   значение ключа state (по умолчанию 'EXECUTED'. Возвращает новый список
   словарей, содержащий только те словари, у которых ключ state соответствует
   указаному значению"""


def filter_by_state(dict_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    filtered_list = []
    for item in dict_list:
        if item.get('state') == state:
            filtered_list.append(item)

    return filtered_list


"""Функция sort_by_date ,принимает список словарей и необязательный параметр, 
   задающий порядок сортировки (по умолчанию-убывание). Функция возвращает новый 
   список, отсортированный подате """


def sort_by_date(dict_list: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортируем список словарей  по ключю key присваивая значение date через
       функцию lambda, убывание организуем через reverse и аннотацию типов bool=True"""
    return sorted(dict_list, key=lambda x: x['date'], reverse=reverse)
