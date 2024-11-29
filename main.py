import sys
from work_file import FileHandler,os
from config import main_file_path
from decor import except_catch

@except_catch
def rec_find_links(file_path : str,links : list[str],fileHandler : FileHandler) -> None:
    content: str | None = fileHandler.read_file(file_path)
    if content == None:
        print(file_path + ' wrong in name file')
        exit(1)
    old_links = set(links) # костыль для пересечения в цикл, чтб не попасть в рекурсию
    new_links = set(fileHandler.find_all_links(content))
    links|= new_links
    for i in new_links.difference(old_links):
        if i.endswith('.md'):
            rec_find_links(i,links,fileHandler)


@except_catch
def filter_file_list(file_list : list[str], black_list_file : list[str] | None) -> None:
    """Чистит входной лист файлов file_list от файлов в списке black_list_file"""
    pass




def main(*argv) -> None:
    # file_path : str = argv[1]

    fileHandler = FileHandler()

    links : set[str] = set()
    file_path : str = main_file_path + r'\тест.md'
    os.chdir(file_path[:file_path.rfind('\\')]) # меняю рабочую директорию на ту, где находится основной файл, с которым мы работаем
    rec_find_links(file_path,links,fileHandler) # Тут, наверное, плохо, что функция меняет список, который принимает
    # Возможно стоит сделать ее чистой, и представить данный список в виде возвращаемого значения
    print(links)
    dst = r'C:\Users\max\Desktop\Тех Защита Информации\1'
    fileHandler.copy_del_files(links,dst) 

if __name__ == '__main__':
    main(*sys.argv)