import os
import re

from FileClasses.decor import except_catch
from FileClasses.DirectoryWorker import DirectoryWorker

class SearcherAllFiles:
    """Класс для поиска всех подфайлов"""
    file_extensions: tuple[str, ...] = (
        '.txt',  # Текстовые файлы
        '.md',  # md-файлы
        '.pdf',  # PDF-файлы
        '.doc',  # Microsoft Word документы
        '.docx',  # Microsoft Word документы (новый формат)
        '.xls',  # Microsoft Excel файлы
        '.xlsx',  # Microsoft Excel файлы (новый формат)
        '.ppt',  # Microsoft PowerPoint файлы
        '.pptx',  # Microsoft PowerPoint файлы (новый формат)
        '.csv',  # CSV (Comma Separated Values) файлы
        '.jpg',  # JPEG изображения
        '.jpeg',  # JPEG изображения
        '.png',  # PNG изображения
        '.gif',  # GIF изображения
        '.bmp',  # BMP изображения
        '.zip',  # ZIP архивы
        '.rar',  # RAR архивы
        '.exe',  # Исполняемые файлы
        '.bat',  # Пакетные файлы
        '.html',  # HTML файлы
        '.css',  # CSS файлы
        '.js',  # JavaScript файлы
        '.json',  # JSON файлы
        '.xml',  # XML файлы
        '.mp3',  # MP3 аудиофайлы
        '.wav',  # WAV аудиофайлы
        '.mp4',  # MP4 видеофайлы
        '.avi',  # AVI видеофайлы
        '.mkv',  # MKV видеофайлы
        '.dll',  # Библиотеки динамической компоновки
    )

    def searchIn(self,file_path) -> set[str]:
        res = set()
        self.main_file_path = file_path[:file_path.rfind('\\')]
        DirectoryWorker.pushd(self.main_file_path,log=True)
        self.rec_find_links(file_path, res)
        res.add(file_path[file_path.rfind('\\')+1:])
        return res

    def read_file(self, path : str) -> str | None:
        """Функция для чтение информации из файла"""
        with open(path,'r',encoding="utf-8") as file:
            content : str = file.read()
            return content

    def refactor_path_files(self, links : list[str]) -> list[str] :
        """
        Меняет все названия файлов на полные с расширением
        Также удаляет из списка несуществующие файлы
        :param links: Список файлов с неполными путями
        :return: Список файлов с полными путями
        """
        return list(filter(lambda x:x,[self.set_exist_file(i) for i in links]))

    def set_exist_file(self, test : str) -> str | None:
        """Проверка того, существует ли файл"""
        if not test.endswith(self.file_extensions):
            test += '.md'
        if os.path.exists(test):
            return test
        for root, dirs, files in os.walk(self.main_file_path):
            if root.rfind('.git') == -1 and root.rfind('.obsidian') == -1:  # убираем проверку технических папок
                if (os.path.exists(os.path.join(root,test))):
                    return os.path.join(root[len(self.main_file_path)+1:],test)
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
    def rec_find_links(self,file_path: str, links: set[str]) -> None:
        content: str | None = self.read_file(file_path)
        if content == None:
            print(file_path + ' wrong in name file')
            exit(1)
        old_links = set(links)  # костыль для пересечения в цикл, чтб не попасть в рекурсию
        new_links = set(self.find_all_links(content))
        links |= new_links
        for i in new_links.difference(old_links):
            if i.endswith('.md'):
                self.rec_find_links(i, links)
