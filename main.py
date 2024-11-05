import sys
from work_file import *

def rec_find_links(file_path,links):
    content: str | None = read_file(file_path)
    if content == None:
        print(file_path + ' wrong in name file')
        exit(1)

    new_links = find_all_links(content)
    links.extend(new_links)
    for i in new_links:
        if i.endswith('.md'):
            print(i)
            rec_find_links(i,links)
    # Тут нужно жеско починить,
    # поменять list(links) на set(links)

def main(*argv) -> None:
    # file_path : str = argv[1]
    links : list[str] = []
    file_path : str = r'B:\obsidian_files\merge\myFolder\тест.md'
    os.chdir(file_path[:file_path.rfind('\\')])
    rec_find_links(file_path,links)
    print(links)

if __name__ == '__main__':
    main(*sys.argv)