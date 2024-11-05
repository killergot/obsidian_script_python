import sys
from work_file import FileHandler,os

from config import main_file_path

def rec_find_links(file_path,links,fileHandler : FileHandler):
    content: str | None = fileHandler.read_file(file_path)
    if content == None:
        print(file_path + ' wrong in name file')
        exit(1)

    new_links = fileHandler.find_all_links(content)
    links.extend(new_links)
    # for i in new_links:
    #     if i.endswith('.md'):
    #         print(i)
    #         rec_find_links(i,links)
    # Тут нужно жеско починить,
    # поменять list(links) на set(links)

def main(*argv) -> None:
    # file_path : str = argv[1]

    fileHandler = FileHandler()

    links : list[str] = []
    file_path : str = main_file_path
    os.chdir(file_path[:file_path.rfind('\\')]) # меняю рабочую директорию на ту, где находится основной файл, с которым мы работаем
    rec_find_links(file_path,links,fileHandler) # Тут, наверное, плохо, что функция меняет список, который принимает
    # Возможно стоит сделать ее чистой, и представить данный список в виде возвращаемого значения
    print(links)

if __name__ == '__main__':
    main(*sys.argv)