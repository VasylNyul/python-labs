import json


def write_into_file(file_path: str, text: str) -> None:
    """
    Write text into a file. May raise PermissionError or OSError.
@@ -24,3 +27,36 @@ def read_from_file(file_path: str) -> str:
    """
    with open(file_path, "r") as file:
        return file.read()


def read_from_json(file_path: str) -> dict:
    """
    Read a JSON file. May raise FileNotFoundError, PermissionError, or OSError.
    :param file_path: The path to the file to read from.
    :return: The content of the file as a dictionary.
    :raises FileNotFoundError: If the file does not exist.
    :raises PermissionError: If the user does not have permission to read the file.
    :raises OSError: If the file is not a file.
    :raises JSONDecodeError: If the file is not a valid JSON file.
    """
    with open(file_path, "r") as file:
        return json.load(file)


def write_into_json(file_path: str, jsons: list) -> None:
    """
    Write a JSON text into a file.
    :param jsons:
    :param file_path: The path to the file to read from.
    :raises FileNotFoundError: If the file does not exist.
    :raises PermissionError: If the user does not have permission to read the file.
    :raises OSError: If the file is not a file.
    :raises JSONDecodeError: If the file is not a valid JSON file.
    """
    jsons_text_representation = json.dumps(jsons, indent=4)
    json.loads(jsons_text_representation)

    with open(file_path, "w") as file:
        file.write(jsons_text_representation)