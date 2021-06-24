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
        # чтение данных из памяти dcr
        for m in range(3):
            script_string += ms_get_frames("iss", 1)
        # чтение данных из памяти iss
        for m in range(7):
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
    # часть 1
    file_name = "write_dcrft_2_use_rd_ptr_shift_part_1"
    with open(set_script_name(file_name) + ".txt", "w") as test_file:
        file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
        #
        file_write(test_file, lm_power_ctrl(mode='on'))
        # инициализация памяти ДеКоР
        file_write(test_file, lm_pl_decor_cyclogram_run(mode='off'))
        file_write(test_file, ms_format_decor())
        for i in range(2):
            # полетное задание 2 (штатная работа с вычиткой по 0xC1) ~1440 кадров в сутки
            file_write(test_file, ms_decor_set_fl_task(2, 0, 1, 1, 5000, 0, [3, 0, 0, 0, 0, 0, 0, 0]))  # включение питания
            file_write(test_file, ms_decor_set_fl_task(2, 1, 3, 0, 1000, 0, [0, 0, 0, 0, 0, 0, 0, 0]))  # синхронизация времени
            file_write(test_file, ms_decor_set_fl_task(2, 2, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
            # 6 hours
            offset = 0+3
            for j in range(6):
                file_write(test_file, ms_decor_set_fl_task(2, offset + 0 + 2 * j, 8, 0, 36000, 99, [0, 0, 0, 0, 0, 0, 0, 0]))  # 3600s=1h fill
                file_write(test_file, ms_decor_set_fl_task(2, offset + 1 + 2 * j, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
            file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
            # 6 hours
            offset = 12+3
            for j in range(6):
                file_write(test_file, ms_decor_set_fl_task(2, offset + 0 + 2 * j, 8, 0, 36000, 99, [0, 0, 0, 0, 0, 0, 0, 0]))  # 3600s=1h fill
                file_write(test_file, ms_decor_set_fl_task(2, offset + 1 + 2 * j, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
            file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
            #
        file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
        # чтение из оперативных данных
        for i in range(10):
            file_write(test_file, reg_read(dev_id=6, var_id=8, offset=128+2048+128*i, length=128))
        #
        for i in range(10):
            file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
    # часть 2
    file_name = "write_dcrft_2_use_rd_ptr_shift_part_2"
    with open(set_script_name(file_name) + ".txt", "w") as test_file:
        file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
        #
        file_write(test_file, lm_power_ctrl(mode='on'))
        # инициализация памяти ДеКоР
        file_write(test_file, lm_pl_decor_cyclogram_run(mode='off'))
        file_write(test_file, ms_format_decor())
        for i in range(2):
            # полетное задание 2 (штатная работа с вычиткой по 0xC1) ~1440 кадров в сутки
            # 6 hours
            offset = 24 + 3
            for j in range(6):
                file_write(test_file, ms_decor_set_fl_task(2, offset + 0 + 2 * j, 8, 0, 36000, 99,
                                                           [0, 0, 0, 0, 0, 0, 0, 0]))  # 3600s=1h fill
                file_write(test_file, ms_decor_set_fl_task(2, offset + 1 + 2 * j, 2, 1, 1000, 0,
                                                           [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                            0x00]))  # ask status
            file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
            # 6 hours
            offset = 36 + 3
            for j in range(6):
                file_write(test_file, ms_decor_set_fl_task(2, offset + 0 + 2 * j, 8, 0, 36000, 99,
                                                           [0, 0, 0, 0, 0, 0, 0, 0]))  # 3600s=1h fill
                file_write(test_file, ms_decor_set_fl_task(2, offset + 1 + 2 * j, 2, 1, 1000, 0,
                                                           [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                            0x00]))  # ask status
            file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
            #
            offset = 48 + 3
            for j in range(10):
                file_write(test_file, ms_decor_set_fl_task(2, offset + j, 2, 1, 1000, 144,
                                                           [0x72, 0xC1, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                            0x00]))  # 60 monitoring block period 1s
            # 44 62 C8 69 00 00 69 00 00 3B 0D 0A
            file_write(test_file,
                       ms_decor_set_fl_task(2, 58, 2, 1, 1000, 0, [0x62, 0xC8, 0x69, 0x00, 0x00, 0x69, 0x00, 0x00]))
            file_write(test_file, ms_decor_set_fl_task(2, 59, 0, 0, 0, 0,
                                                       [0xDE, 0xAD, 0x00, 0x00, 0x00, 0x00, 0xDE, 0xAD]))  # empty
            file_write(test_file, ms_decor_set_fl_task(2, 60, 0, 0, 0, 0,
                                                       [0, 0, 0, 0, 0, 0, 0, 0]))  # empty
            file_write(test_file, ms_decor_set_fl_task(2, 61, 0, 0, 0, 0,
                                                       [0, 0, 0, 0, 0, 0, 0, 0]))  # empty
            #
            file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
            #
        # чтение из оперативных данных
        for i in range(10):
            file_write(test_file, reg_read(dev_id=6, var_id=8, offset=128 + 2048 + 128 * i, length=128))
        #
        for i in range(10):
            file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
    # часть 2
    file_name = "write_dcrft_2_use_rd_ptr_shift_part_3"
    with open(set_script_name(file_name) + ".txt", "w") as test_file:
        file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
        #
        file_write(test_file, lm_power_ctrl(mode='on'))
        # инициализация памяти ДеКоР
        file_write(test_file, lm_pl_decor_cyclogram_run(mode='off'))
        file_write(test_file, ms_format_decor())
        file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
        for i in range(2):
            # проверка записи полетного задания 1
            file_write(test_file, ms_set_pointer("flight_task_decor2", 0))
            file_write(test_file, ms_get_frames("flight_task_decor2", 1))
            file_write(test_file, ms_get_frames("flight_task_decor2", 1))
            file_write(test_file, ms_get_frames("flight_task_decor2", 1))
            file_write(test_file, ms_get_frames("flight_task_decor2", 1))
            file_write(test_file, ms_get_frames("flight_task_decor2", 1))
            file_write(test_file, ms_get_frames("flight_task_decor2", 1))
            file_write(test_file, ms_get_frames("flight_task_decor2", 1))
            file_write(test_file, ms_get_frames("flight_task_decor2", 1))
        file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
        #
        for i in range(20):
            file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
