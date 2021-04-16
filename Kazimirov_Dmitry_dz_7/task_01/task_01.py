#1
import os

path = r'C:\Users\Dmitry\Desktop\Kazimirov_Dmitry_dz_7\task_01'
project_name = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp'] #перечислил названия папок

full_path = os.path.join(path, project_name)
print(full_path) #проверил путь к папке
if not os.path.exists(full_path):#создаем условие если папки нет то создаем, без условия получаем ошибку!
    os.mkdir(full_path) #создал папку

for f in folders:
    folder = os.path.join(full_path, f) #создаем вложенные папки
    if not os.path.exists(folder):
        os.mkdir(folder)

#вижу что код повторяется, понимаю что можно ввести функцию для оптимизации но решил оставить развернутое решение



