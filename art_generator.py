import colorama
import pyfiglet
from colorama import Fore

colorama.init(autoreset=True)

fonts = dict(enumerate(sorted(pyfiglet.FigletFont.getFonts())))
colors = dict(enumerate(sorted(Fore.__dict__.keys())))


def get_text(text, font, color_position, width):
    fig = pyfiglet.Figlet(font)
    fig.width = width
    formatted_text = fig.renderText(text)
    return Fore.__getattribute__(colors[color_position]) + formatted_text


def display_colors():
    for i in colors:
        print(str(i) + ". " + colors[i])


def display_fonts():
    for i in fonts:
        print(str(i) + ". " + fonts[i])


def write_file(file_path, text):
    with open(file_path, "w") as file:
        file.write(text)


while True:
    try:
        initial_text = str(input("Для відображення введіть текст, що містить символи ASCII: "))
        if not initial_text.isascii():
            print("Текст має містити лише символи ASCII")
            continue
        display_colors()
        color_position = int(input("Введіть позицію кольору, який ви бажаєте використовувати: "))
        display_fonts()
        font_position = int(input("Введіть позицію шрифту, який ви хочете використовувати: "))
        width = int(input("Введіть ширину тексту: "))
        modified_text = get_text(initial_text, fonts[font_position], color_position, width)
        print(modified_text)
        write_file("output.txt", modified_text)

        repeat = input("Створити інший арт? (так/ні): ")
        if repeat.lower() != "так":
            break

    except ValueError as e:
        print("Неможливо перевести в ціле значення")
    except KeyError:
        print("Ви ввели неправильне значення для ключа шрифтів або кольору")
    except pyfiglet.CharNotPrinted as e:
        print(str(e))
