from abc import ABC, abstractmethod
import colorama
from colorama import Fore

colorama.init(autoreset=True)
colors = dict(enumerate(sorted(Fore.__dict__.keys())))


class DataProcessor(ABC):

    def __init__(self, file_path):
        if file_path is None:
            raise ValueError("File path should have a value")
        self.__file_path = file_path

    @abstractmethod
    def _get_all_data(self) -> None:
        pass

    @abstractmethod
    def retrieve(self, text, color, width) -> str:
        pass

    def _read_file(self) -> str:
        with open(self.__file_path, "r") as file:
            return file.read()

    @staticmethod
    def display_colors() -> None:
        for i in colors:
            print(str(i) + ". " + colors[i])