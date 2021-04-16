#2
import os

path = r'C:\Users\Dmitry\Desktop\Kazimirov_Dmitry_dz_7\task_02'
project_name = 'my_project'
folders = [
    ['settings',[__init__.py], [dev.py], [prod.py]]
    ['mainapp',[] ], ['authapp',[] ] ] #перечислил названия папок

def create_folder(path): #функция для избежания повторов в коде
    if not os.path.exists(path):
        os.mkdir(path)

def build_structure(root, data): #функция для создания папок в папках
    if data:
        for d in data:
            name = d[0]
            path = os.path.join(root, name)
            create_folder(path)
            build_structure(path, d[1])


full_path = os.path.join(path, project_name)
create_folder(full_path)


build_structure(full_path, folders)
#print(full_path) #проверил путь к папке

#думал что нужно создавать структуру папок не из файла,а по принципу 1 го задания, посмотрел твоё решение понял что делаю не то







