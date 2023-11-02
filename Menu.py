class Menu:
    def __init__(self, items):
        self.items = items

    def display(self):
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")

    def choose_option(self):
        try:
            choice = int(input("Оберіть пункт меню: "))
            if 1 <= choice <= len(self.items):
                return choice
            else:
                print("Неправильний вибір. Будь ласка, введіть номер зі списку.")
        except ValueError:
            print("Неправильний ввід. Введіть номер зі списку.")