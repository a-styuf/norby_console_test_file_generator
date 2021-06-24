import re
import os
import time
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

time_start = time.perf_counter()
# паттерн для поиска полетного задания на запсь
rd_fl_t_pattern = re.compile(r"ms get frames flight_task_decor2 1\n\([0-9]{2}:[0-9]{2}:[0-9]{2}\) RAW data to send:[\s0-9A-F]{73}\n\([0-9]{2}:[0-9]{2}:[0-9]{2}\) Пакет успешно отправлен!\n\([0-9]{2}:[0-9]{2}:[0-9]{2}\) Received RAW data:( [0-9A-F]{2}){15} (([0-9A-F\s]{3}){128})")
wr_fl_t_pattern = re.compile(r"reg write 6 8 ([0-9]{1,6}) 8 ([0-9A-F]{16})")

home_dir = os.getcwd()

try:
    os.mkdir("flight_task_data")
except OSError as error:
    print(error)


def list_files_in_dir_and_subdir(work_path):
    file_list = []
    all_list = os.listdir(work_path)
    all_list = [os.path.normpath(os.path.join(work_path, var)) for var in all_list]
    tmp_list = []
    while all_list:
        for path in all_list:
            if os.path.isfile(path):
                file_list.append(os.path.normpath(path))
                # print(len(file_list))
                pass
            else:
                subdir_list = os.listdir(path)
                subdir_list = [os.path.normpath(os.path.join(path, var)) for var in subdir_list]
                tmp_list.extend(subdir_list)
                pass
        all_list = tmp_list
        tmp_list = []
    return file_list


list_dir_and_file = list_files_in_dir_and_subdir("flight_task_data")
print("Найдено файлов: ", list_dir_and_file)


def get_time():
    return time.strftime("%H-%M-%S", time.localtime()) + "." + ("%.3f: " % time.perf_counter()).split(".")[1]


file_num = 0
rd_fl_t_result = []
wr_fl_t_result = []
tmp_wr_dict = {}

for num, file_path in enumerate(list_dir_and_file):
    if (".log" in file_path) or (".txt" in file_path):  # os.path.isfile(file_path):
        print("Обработка файла: ", file_path)

        file = open(file_path, "r", encoding='utf-8')
        file_lines_str = file.read()
        #
        find_result = rd_fl_t_pattern.findall(file_lines_str)
        for sample in find_result:
            for i in range(8):
                rd_fl_t_result.append(sample[1][0+i*3*16:16*3-1+i*3*16])
        #
        find_result = wr_fl_t_pattern.findall(file_lines_str)
        if find_result:
            #
            for sample in find_result:
                tmp_wr_dict[int(sample[0])] = sample[1]
            k_old = 0
            str_tmp = ""
            for k, v in sorted(tmp_wr_dict.items(), key=lambda item: item[0]):
                if (k - k_old) == 8:
                    str_tmp += v
                    str_with_space = ""
                    for i in range(0, len(str_tmp), 2):
                        str_with_space += str_tmp[0+i:2+i] + " "
                    wr_fl_t_result.append(str_with_space)
                    print(wr_fl_t_result[-1])
                    str_tmp = ""
                    k_old = 0
                else:
                    str_tmp = v
                    k_old = k
                pass
            #
        file_num += 1
    else:
        # print("Обработка файла: ", file_path)
        # print("Файл - не файл!", "\n")
        pass
print(rd_fl_t_result)
print(wr_fl_t_result)

# сортировка кадров по типам: актуальные, старые, из архива БДД
with open("rd_result.txt", "w") as test_file:
    for notice in rd_fl_t_result:
        test_file.write("".join(notice)+"\n")
with open("wr_result.txt", "w") as test_file:
    for notice in wr_fl_t_result:
        test_file.write("".join(notice)+"\n")
print("\nКоличество обработанных файлов: %d" % file_num)

#
print("\n", get_time(), "Конец. Выполненно за %.3f" % (time.perf_counter() - time_start))


