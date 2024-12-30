from src.FileClasses.Searcher import SearcherAllFiles, os
from src.FileClasses.FileSetter import FileSetter


class MainActivity:
    help = """
    Можно скопировать или перенести файл и все его подфайлы в другое место.
    flags:
    -s/--src <path> - Главный файл
    --dst <path> - Целевая папка
    Если вы не включаете интерактивный режим, то вышеуказанные флаги обязательны

    --del - Указывает, что нужно именно перенести файл
    --folder - Указывает, что нужно создавать папки и делать как в источнике

    --interactive - Включить интерактивный режим
        - Данный флаг пока не работает..:)
    """

    def __init__(self, args):
        if len(args) < 3:
            print(self.help)
            print(args)
        else:
            for i in range(len(args)):
                if args[i] == '-s' or args[i] == '--src':
                    self.src = args[i + 1]
                if args[i] == '--dst':
                    self.dst = args[i + 1]
                if args[i] == '--del':
                    self.del_flag = True
                if args[i] == '--folder':
                    self.folder_flag = True
            if getattr(self, 'src', None) is None or getattr(self, 'dst', None) is None:
                print(self.help)
                print(args)
            else:
                self.main()

    def main(self):
        searcher = SearcherAllFiles()
        file_path: str = self.src
        links = searcher.searchIn(file_path)
        print(links)
        FileSetter.file_transfer(links,
                                 self.dst,
                                 del_flag=getattr(self, 'del_flag', False),
                                 folder_flag=getattr(self, 'folder_flag', False))