
# Obsidian Script Python

## Как использовать

### Требования
- Python 3.10+

### Базовый запуск
```powershell
python main.py <source_file>
```
- `<source_file>` — путь к исходной заметке Obsidian (`.md`), из которой будут найдены и собраны связанные файлы.
    - Данный способ стоит использовать, если source_file лежит в корне вашего obsidian репозитория
- По умолчанию файлы копируются в `output/` рядом с `main.py`.

### Дополнительные флаги
```powershell
python main.py <source_file> [--output <path>] [--delete] [--folder] [--verbose] [--main_path <path>]
```

- `--output`, `-o` — путь назначения для файлов.
- `--delete` — перемещать файлы (удалять из исходного места) вместо копирования.
- `--folder` — сохранять структуру папок относительно корня Obsidian.
- `--verbose` — подробные логи.
- `--main_path` — корневая папка Obsidian. Если не задана, берется папка относительно `source_file`.

### Возможные проблемы
- Не отлажена работа с якорями, если вы их много используете, могут не подтягиваться данные файлы

### Примеры
Скопировать все связанные файлы в папку `output` рядом с проектом:
```powershell
python main.py "D:\Vault\Notes\index.md"
```

Сохранить структуру папок в пользовательский каталог:
```powershell
python main.py "D:\Vault\Notes\index.md" --folder -o "D:\Export"
```

Переместить файлы (удалить из исходника):
```powershell
python main.py "D:\Vault\Notes\index.md" --delete -o "D:\Export"
```

Указать корень Obsidian явно:
```powershell
python main.py "D:\Vault\Notes\index.md" --main_path "D:\Vault"
```

## Архитектура проекта

### Поток выполнения
1. `main.py` принимает аргументы CLI и настраивает логирование.
2. `SearcherAllFiles` ищет ссылки в `source_file` и рекурсивно собирает связанные файлы.
3. `FileSetter` копирует или перемещает найденные файлы в целевую директорию.

### Основные модули
- `main.py` — CLI входная точка.
- `src/FileClasses/Searcher.py` — поиск ссылок (wikilink и markdown) и сбор зависимых файлов.
- `src/FileClasses/FileSetter.py` — копирование/перемещение файлов, сохранение структуры.
- `src/FileClasses/DirectoryWorker.py` — временная смена рабочей директории.
- `src/logger/logger.py` — логирование в консоль и файл.
- `src/lexicon/lexicon.py` — текстовые сообщения/подсказки CLI.

### Форматы ссылок
Поддерживаются:
- `[[link]]`
- `[[link|display]]`
- `[[link#section]]`
- `[[link#section|display]]`
- `[text](link)`
- `[text](link#section)`
- `[text](<link with spaces>)`
- `[text](file%20name.md)`
