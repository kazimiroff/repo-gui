#2

import os
import shutil as sh

root_path = r'C:\Users\Dmitry\Desktop\Kazimirov_Dmitry_dz_7\task_03\my_project'
dest_path = r'C:\Users\Dmitry\Desktop\Kazimirov_Dmitry_dz_7\task_03\my_templates'

for dirpath, dnames, fnames in os.walk(root_path):
    for f in fnames:
        if f.endswith(".html"):
            sourse_file_path = os.path.join(dirpath, f)
            dest_file_path = os.path.join(dest_path, f)
            sh.copyfile(sourse_file_path, dest_file_path)

#файлы копируются в директорию но тк они с одинаковыми названиями идёт наложение












