from collections import deque


def main():
    # Добавляем с одного конца, забираем с другого. Это порядок прихода.
    items = deque()
    print("""1 — Добавить в конец
2 — Извлечь первый элемент
3 — Посмотреть первый элемент
4 — Проверить, пуста ли очередь
5 — Узнать размер
6 — Найти элемент
7 — Очистить очередь
8 — Показать все элементы
0 — Выйти""")

    while True:
        command = input("Команда: ").strip()
        if command == "0":
            break
        elif command == "1":
            item = input("Элемент: ")
            items.append(item)
            print("Элемент добавлен.")
        elif command == "2":
            if items:
                print("Извлечён:", items.popleft())
            else:
                print("Очередь пуста.")
        elif command == "3":
            if items:
                print("Первый элемент:", items[0])
            else:
                print("Очередь пуста.")
        elif command == "4":
            print("Очередь пуста." if not items else "Очередь не пуста.")
        elif command == "5":
            print("Размер очереди:", len(items))
        elif command == "6":
            item = input("Что найти: ")
            print("Элемент найден." if item in items else "Элемент не найден.")
        elif command == "7":
            items.clear()
            print("Очередь очищена.")
        elif command == "8":
            if items:
                print("Очередь от начала к концу:")
                for position, item in enumerate(items, start=1):
                    print(f"{position}. {item}")
            else:
                print("Очередь пуста.")
        else:
            print("Выберите команду от 0 до 8.")


if __name__ == "__main__":
    main()
