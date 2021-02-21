from bs4 import BeautifulSoup
import requests
import os
from lib import get_elements_folder, Date
from itertools import zip_longest
from os.path import relpath
import sys


class Update:
    """
    Класс обновления прогграмы на входе берёт названия репозитория,имя пользователя,
    также можно указать ветвь(по умолчанию ветвь=main) и сайт.
    """

    def __init__(self, repository, site=None, user=None, branch="main", file="repository.xml"):
        self.rp = repository
        self.repository_file = file
        self.date = date = Date()
        if site is None:
            self.username = user
            self.url = f"https://raw.githubusercontent.com/{self.username}/{self.rp}/{branch}/"
            self.xml = requests.get(self.url + file)
        else:
            self.url = site + "/"+self.rp+"/"
            self.xml = requests.get(self.url+self.repository_file)
        self.response = self.xml.content
        self.parser = BeautifulSoup(self.response, "lxml")

    def get_json(self, delete=-1):
        """
        Этот метод класс Update выдаёт json с обнолвениями.
        """
        releases_array = []
        releases = self.parser.find_all("release")
        for release in releases:
            dirs = release.update.find("create")
            if dirs is not None:
                dirs = dirs['directory'].split(';')
            files_array = release.files.find_all("file")
            files = []
            for file in files_array:
                files.append(file.text)
            exists_commit = release.find("commit")
            if exists_commit is not None:
                commit = release.find("commit").text
            else:
                commit = "None"
            releases_array.append({
                "version": release['version'],
                "date": release['date'],
                "description": release.description.text,
                "dirs": dirs,
                "files": files,
                "commit": commit
            })
        if delete != -1:
            for i in range(delete):
                releases_array.pop(0)
        return releases_array

    def get_update(self):
        """
        Этот метод смотрит если в локальным repository.xml и repository.xml которые
        на гитхабе есть различия  в версиях то он обновляет прогграму.
        Возращает True если прогграма обновилась,False если нет обновлений
        """
        release = self.get_json()
        try:
            f = open(self.repository_file, "r")
            bs = BeautifulSoup(f.read(), "lxml")
            version = bs.current.text
            f.close()
            # Если в локольном файле репозитория и на удалённом файл есть различия
            # То обновляем файл иначе отдаём false
            if version != release[-1]['version']:
                # Если в последним списке нам передали паки которые надо создать то создаём их
                if release[-1]['dirs'] is not None:
                    for directory in {release[-1]['dirs']}:
                        os.mkdir(directory)
                # Проходимя по списку файлов которые надо обновить
                for file in {release[-1]['files']}:
                    # Скачиваем текущий файл
                    r = requests.get(self.url + file)
                    # Берём данные файла
                    file_content = r.content
                    # Записаваем данные
                    f = open(file, 'w')
                    # Данные приходят в виде байтовой строки и поэтому используем decode()
                    # Чтобы перевести байтовую строку в обычную
                    f.write(file_content.decode())
                    f.close()
                print(f"Версия прогграмы обновленна до {release[-1]['version']}")
                return True
            else:
                return False
        except FileNotFoundError:
            # Если нету локального файла репозитория то скачиваем его
            print("repository.xml не найден!\nСкачиваем repository.xml")
            rq = requests.get(self.url + "repository.xml")
            xml_content = rq.content
            releases_file = open(self.repository_file, 'w')
            releases_file.write(xml_content.decode())
            releases_file.close()
            return False

    def smart_update(self):
        """
        Умно обновляет прогграму.Берёт и сравнивает локальный файлы с файлами на сервере.
        Сравнивает размер,папки,и файлы
        """
        # Получаем локальный список элментов
        elements = get_elements_folder()
        # Находим все теги directory
        directories_from_server = self.parser.find_all("directory")
        # Создаём массив directories куда будем складавать папки
        directories = []
        for directory in directories_from_server:
            # Начинаем парсить содержимое тегов directory
            files_array = []
            path = directory['path']
            files_arr = directory.find_all("file")
            for file in files_arr:
                file_size = file['size']
                file_name = file.text
                files_array.append((file_name, file_size))
            directories.append([path, files_array])
        # Начинаем сравнивать локальные элементы и удалённые элементы
        for local, destination in zip_longest(elements, directories):
            if destination is None:
                continue
            # Если локального элемента нет
            if local is None:
                # То создаём папку которой нет
                os.mkdir(destination[0])
                # Также создаём файлы папки
                for files in destination[1]:
                    path = destination[0] + "/" + files[0]
                    rq = requests.get(self.url + destination[0] + "/" + files[0])
                    file = open(path, 'w')
                    file_content = rq.content
                    file.write(file_content.decode())
                    file.close()
            else:
                # Иначе если локальная и удалённая папка существует
                # То смотрим файлы если они разные то начинаем сравнивать файлы
                if local[1] != destination[1]:
                    # Начинаем обход по файлам
                    for files in zip_longest(local[1], destination[1]):
                        if files[1] is None:
                            continue
                        # Если локального файла не существует то скачиваем его
                        if files[0] is None:
                            if destination[0] != ".":
                                path = destination[0] + "/" + files[1][0]
                                rq = requests.get(self.url + destination[0] + "/" + files[1][0])
                            else:
                                path = files[1][0]
                                rq = requests.get(self.url + files[1][0])
                            file = open(path, 'w')
                            file_content = rq.content
                            file.write(file_content.decode())
                            file.close()
                        # Иначе смотрим размер файлов
                        else:
                            # Если он не совподают то скачиваем
                            if files[0][1] != files[1][1] and files[1] is not None:
                                if destination[0] != ".":
                                    path = destination[0] + "/" + files[1][0]
                                    rq = requests.get(self.url + destination[0] + "/" + files[1][0])
                                else:
                                    path = files[1][0]
                                    rq = requests.get(self.url + files[1][0])
                                file = open(path, 'w')
                                file_content = rq.content
                                file.write(file_content.decode())
                                file.close()
        return True

    @staticmethod
    def generate_repository_file(filename="repository.xml", init_file="main.py"):
        local_elements = get_elements_folder()
        xml_elements = []
        for el in local_elements:
            directory = [f"<directory path='{el[0]}'>"]
            for files in el[1]:
                directory.append(f"         <file size='{files[1]}'>{files[0]}</file>")
            directory.append("    </directory>")
            xml_elements.append(directory)
        directories = []
        for i in xml_elements:
            full_directory = '\n\t'.join(i)
            directories.append(full_directory)
        full_directories = '\n\t\t'.join(directories)
        file = open(filename, 'w')
        file.write(f"""<?xml version="1.0" encoding="utf-8" ?>
<repository>
    <directories>
        {full_directories}
    </directories>
    <releases>
        <current>0.1</current>
        <release version="0.1" date="x.xx.xx">
            <description>Инициализирующее обновление</description>
            <update>
                <files>
                    <file>{init_file}</file>
                </files>
            </update>
        </release>
    </releases>
</repository>""")
        file.close()
        return relpath(filename)

    def make_update(self, version_release, description_release, updated_files,filename="repository.xml"):
        release = f"""        <release version="{version_release}" date="{self.date.get_date()}">
            <description>{description_release}</description>
            <update>
                <files>
                    {updated_files}
                </files>
            </update>
        </release>
"""
        # Открываем файл репозитория для чтения
        repository_file = open(filename, 'r')
        lines = repository_file.readlines()
        lines.insert(-2, release)
        repository_file.close()
        # Открываем файл для записи
        file = open(filename, 'w')
        file.writelines(lines)
        file.close()


if __name__ == '__main__':
    update = Update("Yaftp_client", user="roaldiopi")
    if "--make-update" in sys.argv:
        index = sys.argv.index("--make-update")
        version = sys.argv[index+1]
        description = sys.argv[index+2]
        files = sys.argv[index+3]
        update.make_update(version,description,files)
    elif "--generate-repository-file" in sys.argv:
        length = len(sys.argv)
        if sys.argv == 2:
            update.generate_repository_file()
        else:
            update.generate_repository_file(sys.argv[2])


