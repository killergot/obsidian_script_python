import os
import shutil
import re

from config import file_extensions,folder_path


def read_file(path : str) -> str | None:
    """Функция для чтение информации из файла"""
    with open(path,'r',encoding="utf-8") as file:
        content : str = file.read()
        return content

def refactor_path_files(links : list[str]) -> list[str] :
    return list(filter(lambda x:x,[set_exist_file(i) for i in links]))

def set_exist_file(test : str) -> str | None:
    """Проверка того, существует ли файл"""
    if not test.endswith(file_extensions):
        test += '.md'
    for directory in folder_path:
        if os.path.exists(test):
            return test
        elif os.path.exists(os.path.join(directory, test)):
            return os.path.join(directory, test)
    return None


def find_all_links(file : str) -> list[str]:
    """Функция для нахождения всех ссылок в файле
        Рассматриваются 3 вида ссылок в obsidian:
        1 - [[link]]
        2 - [text](link)
        3 - [text](<link is separated by a space>)
    """
    pattern : str= r"\[\[([^\n\]]+?)\]\]|\[.*?\]\((<([^>\n]+)>|([^()\n<>]+))\)"
    matches : list[str] = re.findall(pattern, file)
    results : list[str]= []
    for match in matches:
        # Извлекаем только непустые группы (т.е. либо из [[]], либо из ())
        results.append(match[0] or match[2] or match[3])
    return refactor_path_files(results)
