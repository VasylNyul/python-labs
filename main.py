import math

history = []
memory = []


def main():
    while True:
        try:
            num1 = float(input('Введіть перше число: '))
            operator = input('Введіть оператор (+, -, *, /, ^, √, %): ')
            num2 = None
            if operator != '√':
                num2 = float(input("Введіть друге число: "))

            decimal_places = int(input('Кількість десяткових розрядів для результату: '))
            if decimal_places < 0:
                raise ValueError('Непідтримувана кількість десяткових розрядів. Спробуйте ще раз.')

            result = calculate(num1, num2, operator, decimal_places)

            print(f'Результат: {result}')

            memory_change(result)
            show_history()

            repeat = input('Виконати ще одне обчислення? (так/ні): ')
            if repeat.lower() != 'так':
                break

        except ValueError as e:
            print(f'Помилка: {e}')
        except ZeroDivisionError:
            print('Помилка: Ділення на нуль')


def memory_change(result):
    global memory
    memory_option = input("Зберегти результат? (так/ні): ")
    if memory_option.lower() == 'так':
        memory.append(result)

    if memory:
        memory_option = input("Отримати результат з пам'яті? (так/ні): ")
        if memory_option.lower() == 'так':
            selected_position = int(
                input(f'Оберіть порядковий номер результату, який бажаєте отримати(макс: {len(memory)}): '))
            if 1 <= selected_position <= len(memory):
                value = memory[selected_position-1]
                print(f"Значення з пам'яті: {value}")
            else:
                raise ValueError('Порядковий номер не дійсний.')


def show_history():
    show = input('Показати історію обчислень? (так/ні): ')
    if show.lower() == 'так':
        print('\nІсторія обчислень:')
        for entry in history:
            num1, operator, num2, result = entry
            if num2 is not None:
                print(f'{num1} {operator} {num2} = {result}')
            else:
                print(f'{operator}{num1} = {result}')


def calculate(num1, num2, operator, decimal_places):
    operator_functions = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else None,
        '^': lambda x, y: x ** y,
        '√': lambda x, _: math.sqrt(x),
        '%': lambda x, y: x % y
    }

    if operator in operator_functions:
        result = operator_functions[operator](num1, num2)
        if result is None:
            raise ZeroDivisionError
    else:
        raise ValueError('Непідтримуваний оператор. Введіть оператор, який підтримується (+, -, *, /, ^, √, %)')

    if decimal_places == 0:
        result = int(result)
    else:
        result = round(result, decimal_places)
    push_to_history(num1, num2, operator, result)

    return result


def push_to_history(num1, num2, operator, result):
    if operator == '√':
        history.append((operator, num1, result))
    else:
        history.append((num1, operator, num2, result))


if __name__ == '__main__':
    main()
