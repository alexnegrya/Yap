import random
import string
import time
import os
from os.path import getsize


class Color:
    """
    Класс с цветами
    """
    purple = '\033[95m'
    cyan = '\033[96m'
    dark_cyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'


class Date:
    def __init__(self):
        self.seconds = time.time()
        self.date = time.localtime(self.seconds)

    def get_date(self):
        # Преоброзуем в стандартный вариант
        now = time.strftime("%d/%m/%Y %H:%M", self.date)
        return now

    def get_seconds(self):
        return int(self.seconds)

    def get_date_by_code(self, date_code):
        # Преоброзуем в вариант который запросили
        now = time.strftime(date_code, self.date)
        return now


def generate_string(length):
    """
    Функция генерирует строку с цифрами
    """
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string


def write_log(log, literals_in_console=False, path="logs.txt"):
    """
    Функция может писать логи в консоль,и записавать их в указанную директорию
    """
    # Если нужны литералы то выводим лог вместе с ними
    if literals_in_console:
        print(log)
    # Если не нужны литералы убираем их
    else:
        console_log = log.replace("\n", "")
        print(console_log)
    with open(path, "a", encoding="utf-8") as f:
        f.write(log)


def binary_search(array, item):
    # В переменных low и high хранятся границы той части списка, в которой выполняется поиск
    low = 0
    high = len(array) - 1

    # Пока эта часть не сократится до одного элемента...
    while low <= high:
        # ... проверяем средний элемент
        mid = (low + high) // 2
        guess = array[mid]
        # Значение найдено
        if guess == item:
            return mid
        # Много
        if guess > item:
            high = mid - 1
        # Мало
        else:
            low = mid + 1

    # Значение не существует
    return None


def search(arr, key):
    for i in arr:
        if i == key:
            return i
    return None


def search_in_array_json(arr, index, value):
    for el in arr:
        if el[index] == value:
            return arr.index(el)
    return None


def get_elements_folder(exclude=("./venv", "./.git", "./.idea", "__pycache__")):
    # Создаём список в который будет входить незапрёщенные папки
    elements = []
    # Получаем данные о всех элементах в этой папки
    tree = os.walk(".", topdown=True)
    # Создаём список какой должна быть папка чтобы её записали
    not_found = []
    # Генерируем список
    for i in range(len(exclude)):
        not_found.append(-1)
    # ----
    # Начинаем обход по элментам
    for root, dirs, files in tree:
        check_dir = []
        if root == ".":
            elements.append([root, files])
        for el in exclude:
            check_dir.append(root.find(el))
        if check_dir == not_found:
            if root != ".":
                elements.append([root, files])
    elements_folder = []
    # Добавляем размер к файлам
    for el in elements:
        file_size = []
        for file in el[1]:
            file_size.append((file, getsize(el[0] + "/" + file)))
        elements_folder.append([el[0], file_size])
    return elements_folder
