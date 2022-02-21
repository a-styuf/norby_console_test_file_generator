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

script_dir = "Script/"


def set_script_name(name):
    return script_dir + str(name)


def read_pl_mem_30_s():
    script_string = ""
    for j in range(1):
        # чтение данных из памяти iss
        for m in range(3):
            script_string += ms_get_frames("iss", 1)
        # чтение данных из памяти dcr
        for m in range(7):
            script_string += ms_get_frames("decor", 1)
    return script_string


def read_pl_mem_1_min():
    script_string = ""
    for j in range(4):
        # чтение данных из памяти dcr
        for m in range(5):
            script_string += ms_get_frames("iss", 1)
        # чтение данных из памяти iss
        for m in range(15):
            script_string += ms_get_frames("decor", 1)
    return script_string


def read_pl_mem(frame_num=1, mem_type="iss"):
    script_string = ""
    for j in range(frame_num):
        if mem_type == "iss":
            script_string += ms_get_frames("iss", 1)
        elif mem_type == "decor":
            script_string += ms_get_frames("decor", 1)
        else:
            raise ValueError("incorrect mem_type")
        # чтение данных из памяти iss
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
    if mode == "single":
        command_val = 0x0100 | (c_num & 0xFF)
    elif mode == "cyclic":
        command_val = 0x0200 | (0 & 0xFF)
    elif mode == "off":
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
    if mode == "single":
        command_val = 0x00 | (ft_num & 0x03)
    elif mode == "cyclic":
        command_val = 0x10 | (ft_num & 0x03)
    elif mode == "off":
        command_val = 0x00
    elif mode == "pause":
        command_val = 0x04
    else:
        raise(TypeError, "Wrong mode parameter")
    script_string += reg_write(6, 4, 28, 1, command_val)
    return script_string


def lm_power_ctrl(mode='on'):
    """
    Command for power control
    :param mode: 'on' - power on, 'off' - power off
    :return: script strings
    """
    if mode == 'on':
        var = 0x0101
    elif mode == 'off':
        var = 0x0000
    else:
        raise(TypeError, "Wrong mode parameter")
    script_string = ""
    script_string += reg_write(3, 4, 34, 2, var & 0xFFFF)
    return script_string
    pass


def file_write(file, string):
    print(string, end="")
    file.write(string)


if __name__ == "__main__":
    file_name = "test_1"
    with open(set_script_name(file_name) + ".txt", "w") as test_file:
        file_write(test_file, norby_tmi_slice(tmi_list=[0, 1, 2, 3, 4, 5, 6, 7, 8]))
        file_write(test_file, lm_power_ctrl(mode='on'))
        # инициализация памяти ДеКоР
        file_write(test_file, ms_format_decor())
        # полетное задание 1
        # # # полетное задание 1 (штатная работа с вычиткой 0xC1)
        file_write(test_file, ms_decor_set_fl_task(1, 0, 1, 1, 5000, 0, [3, 0, 0, 0, 0, 0, 0, 0]))  # включение питания
        file_write(test_file, ms_decor_set_fl_task(1, 1, 3, 0, 1000, 0, [0, 0, 0, 0, 0, 0, 0, 0]))  # синхронизация времени
        file_write(test_file, ms_decor_set_fl_task(1, 2, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
        file_write(test_file, ms_decor_set_fl_task(1, 3, 8, 0, 50000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 800 s fill
        file_write(test_file, ms_decor_set_fl_task(1, 4, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
        file_write(test_file, ms_decor_set_fl_task(1, 5, 8, 0, 50000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 800 s fill
        file_write(test_file, ms_decor_set_fl_task(1, 6, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
        file_write(test_file, ms_decor_set_fl_task(1, 7, 2, 1, 1000, 99, [0x72, 0xC1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # 100 monitoring block period 1s
        # полетное задание 2
        file_write(test_file, ms_decor_set_fl_task(2, 0, 1, 1, 5000, 0, [3, 0, 0, 0, 0, 0, 0, 0]))  # включение питания
        file_write(test_file, ms_decor_set_fl_task(2, 1, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
        file_write(test_file, ms_decor_set_fl_task(2, 2, 3, 0, 1000, 0, [0, 0, 0, 0, 0, 0, 0, 0]))  # синхронизация времени
        file_write(test_file, ms_decor_set_fl_task(2, 3, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
        file_write(test_file, ms_decor_set_fl_task(2, 4, 2, 1, 500, 0, [0x62, 0xCA, 0x32, 0x00, 0x00, 0x00, 0x00, 0x00]))  # enable deffered record
        file_write(test_file, ms_decor_set_fl_task(2, 5, 2, 1, 1000, 4, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
        file_write(test_file, ms_decor_set_fl_task(2, 6, 2, 1, 500, 0, [0x62, 0xC8, 0xC0, 0xF9, 0x30, 0x60, 0x00, 0x00]))  # enable deffered record
        file_write(test_file, ms_decor_set_fl_task(2, 7, 2, 1, 1000, 4, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
        #
        file_write(test_file, norby_tmi_slice(tmi_list=[0, 1, 2, 3, 4, 5, 6, 7, 8]))
        # проверка полетного задания 1
        file_write(test_file, reg_read(6, 8, 128 + 0*128, 128))
        file_write(test_file, reg_read(6, 8, 128 + 1*128, 128))
        file_write(test_file, reg_read(6, 8, 128 + 2*128, 128))
        # проверка полетного задания 2
        file_write(test_file, reg_read(6, 8, 2176 + 0*128, 128))
        file_write(test_file, reg_read(6, 8, 2176 + 1*128, 128))
        file_write(test_file, reg_read(6, 8, 2176 + 2*128, 128))
        # запись полетного задания 1
        file_write(test_file, reg_write(6, 2, 3, 1, 0x01))
        # запись полетного задания 2
        file_write(test_file, reg_write(6, 2, 4, 1, 0x01))
        #
        file_write(test_file, norby_tmi_slice(tmi_list=[0, 1, 2, 3, 4, 5, 6, 7, 8]))
        # проверка записи полетного задания 1
        file_write(test_file, ms_set_pointer("flight_task_decor1", 0))
        file_write(test_file, ms_get_frames("flight_task_decor1", 4))
        # проверка записи полетного задания 2
        file_write(test_file, ms_set_pointer("flight_task_decor2", 0))
        file_write(test_file, ms_get_frames("flight_task_decor2", 4))
        # запуск полетного задания 1 одиночно
        file_write(test_file, reg_write(6, 4, 28, 1, 0x02))
        # чтение данных из памяти декор
        file_write(test_file, ms_get_frames("decor", 100))
        #
        file_write(test_file, norby_tmi_slice(tmi_list=[0, 1, 2, 3, 4, 5, 6, 7, 8]))


