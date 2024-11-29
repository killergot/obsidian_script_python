import os
import shutil
import re

from config import file_extensions,main_file_path
from decor import except_catch

class FileHandler:
    """Класс для работы с файлами"""
    def __init__(self):
        self.file_extensions : list[str] = file_extensions

    def read_file(self, path : str) -> str | None:
        """Функция для чтение информации из файла"""
        with open(path,'r',encoding="utf-8") as file:
            content : str = file.read()
            return content

    def refactor_path_files(self, links : list[str]) -> list[str] :
        return list(filter(lambda x:x,[self.set_exist_file(i) for i in links]))

    def set_exist_file(self, test : str) -> str | None:
        """Проверка того, существует ли файл"""
        if not test.endswith(self.file_extensions):
            test += '.md'
        if os.path.exists(test):
            return test
        for root, dirs, files in os.walk(main_file_path): 
            if root.rfind('.git') == -1 and root.rfind('.obsidian') == -1:  # убираем проверку технических папок
                if (os.path.exists(os.path.join(root,test))):
                    return os.path.join(root[len(main_file_path)+1:],test)
        return None


    def find_all_links(self, file : str) -> list[str]:
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
        return self.refactor_path_files(results)


    
    @except_catch
    def copy_del_files(self,file_list : list[str], dst_path : str) -> None:  
        """Копирует все файлы в списке в dst_path по таким-же путям как и в исходном
        Если установлен флаг удаления, то так-же удаляет все файлы из сходного репозитория"""
        # Проверка того, существует ли папка dst_path
        if not os.path.exists(dst_path) and not os.path.isfile(dst_path):
            print('Данной папки не существует')
            return 

        print('sdfa')


        # Цикл, в котором будем проходиться по всем файлам
        for i in file_list:
            pass