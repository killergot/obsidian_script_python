import os
import logging

log = logging.getLogger(__name__)

class DirectoryWorker:
    directory_stack = []

    @classmethod
    def pushd(cls,path):
        # Сохраняем текущую директорию в стек
        cls.directory_stack.append(os.getcwd())
        # Переходим в новую директорию
        os.chdir(path)
        log.debug(f"Перешли в директорию: {os.getcwd()}")

    @classmethod
    def popd(cls):
        if cls.directory_stack:
            # Возвращаемся в последнюю директорию из стека
            prev_dir = cls.directory_stack.pop()
            os.chdir(prev_dir)
            log.debug(f"Вернулись в директорию: {os.getcwd()}")
        else:
            log.debug("Стек директорий пуст!")