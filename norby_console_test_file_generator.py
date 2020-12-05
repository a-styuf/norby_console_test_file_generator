"""
this script generates test file for norby console client
General interface:
    reg get <deviceId> <varId> <offset> <length>            - Запрос значения регистра данных
    reg write <deviceId> <varId> <offset> <length> <value>  - Запись значения в регистр данных
    reg assert <deviceId> <varId> <offset> <length> <valueMin> <valueMax>  - Проверка значения в регистре

Linking module (Модаль сопрядения) interface:
    ms get telemetry        - Выдача полной телеметрии МС
    ms get status           - Чтение статуса загрузки МС
    ms format iss           - Форматировать память ИСС
    ms format decor         - Форматировать память Декор
    ms get frames <volume> <count> - запрос на вычитку кадров из тома памяти (где \"volume\": iss, decor, all, flight_task_decor1, flight_task_decor2, decor_status)
    ms set pointer <volume> <offset> - установка указателя чтения в томе памяти на заданный кадр (где \"volume\": iss, decor, flight_task_decor1, flight_task_decor2, decor_status, all)
"""

from scr_gen_lib import *
import os

try:
    os.mkdir("Script")
except OSError as error:
    print(error)

file_name = "Script/norby_lm_test_script"


def read_pl_mem_30_s():
    script_string = ""
    for j in range(2):
        # чтение данных из памяти dcr
        for m in range(8):
            script_string += ms_get_frames("iss", 1)
        # чтение данных из памяти iss
        for m in range(12):
            script_string += ms_get_frames("decor", 1)
    return script_string


def read_pl_mem_1_min():
    script_string = ""
    for j in range(4):
        # чтение данных из памяти dcr
        for m in range(8):
            script_string += ms_get_frames("iss", 1)
        # чтение данных из памяти iss
        for m in range(12):
            script_string += ms_get_frames("decor", 1)
    return script_string


def lm_pl_iss_cyclogram_run(mode="single", c_num=1):
    """
    Command to run PL_ISS cyclogrammas
    :param mode: "single" - single run, "cyclic" - cyclic operation, "off" - pl switch off
    :param c_num: number of cyclogram for "single" mode
    :return: script strings
    """
    script_string = ""
    command_val = 0x0000
    if mode is "single":
        command_val = 0x0100 | (c_num & 0xFF)
    elif mode is "cyclic":
        command_val = 0x0200 | (0 & 0xFF)
    elif mode is "off":
        pass
    else:
        raise(TypeError, "Wrong mode parameter")
    script_string += reg_write(6, 4, 26, 2, command_val)
    return script_string


def lm_pl_decor_cyclogram_run(mode="single", ft_num=1):
    """
    Command to run PL_DeCoR flight task (ft)
    :param mode: "single" - single run, "cyclic" - cyclic operation, "off" - pl switch off, "pause" - ft pause
    :param ft_num: number of flight task  (1 - default, 2- ft_1, 3 - ft_2)
    :return: script strings
    """
    script_string = ""
    command_val = 0x00
    if mode is "single":
        command_val = 0x00 | (ft_num & 0x03)
    elif mode is "cyclic":
        command_val = 0x10 | (ft_num & 0x03)
    elif mode is "off":
        command_val = 0x00
    elif mode is "pause":
        command_val = 0x04
    else:
        raise(TypeError, "Wrong mode parameter")
    script_string += reg_write(6, 4, 28, 1, command_val)
    return script_string


def file_write(file, string):
    print(string, end="")
    file.write(string)


if __name__ == "__main__":
    with open(file_name + ".txt", "w") as test_file:
        # срез телеметрии
        file_write(test_file, norby_tmi_slice(tmi_list=[1, 4, 7, 8]))
        # телеметрия МС
        file_write(test_file, ms_get_telemetry())
        # включение МС
        file_write(test_file, reg_write(3, 4, 34, 2, 0x0101))
        # срез телеметрии
        file_write(test_file, norby_tmi_slice(tmi_list=[1, 4, 7, 8]))
        # телеметрия МС
        file_write(test_file, ms_get_telemetry())
        # запуск циклограммы 5
        file_write(test_file, lm_pl_iss_cyclogram_run(mode="single", c_num=5))
        # чтение на 6 минут
        for i in range(4):
            file_write(test_file, read_pl_mem_30_s())
            # срез телеметрии
            file_write(test_file, norby_tmi_slice(tmi_list=[1, 4, 7, 8]))
            # телеметрия МС
            file_write(test_file, read_pl_mem_30_s())
            # срез телеметрии
            file_write(test_file, norby_tmi_slice(tmi_list=[1, 4, 7, 8]))
            # телеметрия МС
            file_write(test_file, ms_get_telemetry())
        # запуск циклограммы 3
        file_write(test_file, lm_pl_iss_cyclogram_run(mode="single", c_num=3))
        # чтение на 2 минут
        for i in range(4):
            file_write(test_file, read_pl_mem_30_s())
            # срез телеметрии
            file_write(test_file, norby_tmi_slice(tmi_list=[1, 4, 7, 8]))
            # телеметрия МС
            file_write(test_file, read_pl_mem_30_s())
            # срез телеметрии
            file_write(test_file, norby_tmi_slice(tmi_list=[1, 4, 7, 8]))
            # телеметрия МС
            file_write(test_file, ms_get_telemetry())

