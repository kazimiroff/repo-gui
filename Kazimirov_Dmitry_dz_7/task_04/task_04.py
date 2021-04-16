#4

import os

def files_stat():
    files_dict = {}

    for item in os.scandir(r'C:\Users\Dmitry\Desktop\Kazimirov_Dmitry_dz_7\task_03'):
        if item.is_file():
            size = item.stat().st_size
            round_up = 10 ** len(str(size))
            try:
                files_dict[round_up][0] +=1

            except (KeyError, IndexError):
                files_dict[round_up] = [1]

    files_stat()
    print(files_dict) #ничего не выводится, хотя посмотрел твоё решение и кое что оттуда скопипастил













