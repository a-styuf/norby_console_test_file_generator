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
    file_name = "brk_link_test_by_gorev"
    with open(set_script_name(file_name) + ".txt", "w") as test_file:
        for j in range(12):
            file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))  # 17.6 s
            for i in range(28):  # 4.4 * 28 s
                file_write(test_file, set_brk_address(brk=i % 2 + 1))  # 2.2 s
                #
                file_write(test_file, norby_tmi_slice(tmi_list=[1]))  # 2.2 s
                #


