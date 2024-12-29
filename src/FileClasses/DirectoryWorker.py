import os

class DirectoryWorker:
    directory_stack = []

    @classmethod
    def pushd(cls,path,*,log: bool = False):
        # Сохраняем текущую директорию в стек
        cls.directory_stack.append(os.getcwd())
        # Переходим в новую директорию
        os.chdir(path)
        if log:
            print(f"Перешли в директорию: {os.getcwd()}")

    @classmethod
    def popd(cls,*,log: bool = False):
        if cls.directory_stack:
            # Возвращаемся в последнюю директорию из стека
            prev_dir = cls.directory_stack.pop()
            os.chdir(prev_dir)
            if log:
                print(f"Вернулись в директорию: {os.getcwd()}")
        else:
            if log:
                print("Стек директорий пуст!")