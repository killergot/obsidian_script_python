import curses


def main(stdscr):
    # Очищаем экран
    curses.curs_set(0)  # Скрываем курсор
    stdscr.clear()

    # Массив с элементами
    items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

    # Переменная для отслеживания текущего элемента
    current_item = 0

    while True:
        # Очистка экрана и вывод списка
        stdscr.clear()

        # Выводим все элементы массива, выделяя текущий
        for i, item in enumerate(items):
            if i == current_item:
                stdscr.addstr(i, 0, f"> {item}", curses.A_REVERSE)  # Выделяем текущий элемент
            else:
                stdscr.addstr(i, 0, item)

        # Отображаем изменения
        stdscr.refresh()

        # Ожидаем нажатие клавиши
        key = stdscr.getch()

        # Навигация по списку с помощью стрелок
        if key == curses.KEY_UP:  # Стрелка вверх
            current_item = (current_item - 1) % len(items)
        elif key == curses.KEY_DOWN:  # Стрелка вниз
            current_item = (current_item + 1) % len(items)
        elif key == 27:  # ESC для выхода
            break


# Запуск программы
curses.wrapper(main)