"""
Library contains functions to generate YAT script strings for Norby CubeSat

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

import time

line_delay_ms = 2500
delay_ms = 400

reg_read_str = "reg get"
reg_write_str = "reg write"
reg_assert_str = "reg assert"

ms_get_telemetry_str = "ms get telemetry"
ms_get_status_str = "ms get status"
ms_format_iss_str = "ms format iss"
ms_format_decor_str = "ms format decor"
ms_get_frames_str = "ms get frames"
ms_set_pointer_str = "ms set pointer"
set_brk_address_str = "set brk_address"


def delay(value_ms):
    """
    Function sets delay strings to fill delay value
    :param value_ms: delay in ms
    :return: string set according to delay
    """
    script_str = ""
    script_str += "\\!(Delay(%d))\n" % value_ms
    return script_str


def reg_write(dev_id, var_id, offset, length, value):
    script_str = "\\!(Delay(%d)) " % line_delay_ms
    script_str += reg_write_str
    script_str += " " + "%d" % dev_id
    script_str += " " + "%d" % var_id
    script_str += " " + "%d" % offset
    script_str += " " + "%d" % length
    script_str += " " + ("%016X" % value)[-length*2:]
    script_str += "\n"
    return script_str


def reg_write_string(dev_id, var_id, offset, length, value_str):
    script_str = "\\!(Delay(%d)) " % line_delay_ms
    script_str += reg_write_str
    script_str += " " + "%d" % dev_id
    script_str += " " + "%d" % var_id
    script_str += " " + "%d" % offset
    script_str += " " + "%d" % length
    script_str += " " + value_str
    script_str += "\n"
    return script_str


def reg_read(dev_id, var_id, offset, length):
    script_str = "\\!(Delay(%d)) " % line_delay_ms
    script_str += reg_read_str
    script_str += " " + "%d" % dev_id
    script_str += " " + "%d" % var_id
    script_str += " " + "%d" % offset
    script_str += " " + "%d" % length
    script_str += "\n"
    return script_str


def reg_assert(dev_id, var_id, offset, length, vaalue_min, value_max):
    script_str = "\\!(Delay(%d)) " % line_delay_ms
    script_str += reg_assert_str
    script_str += " " + "%d" % dev_id
    script_str += " " + "%d" % var_id
    script_str += " " + "%d" % offset
    script_str += " " + "%d" % length
    script_str += " " + "%d" % vaalue_min
    script_str += " " + "%d" % value_max
    script_str += "\n"
    return script_str


def ms_get_telemetry():
    script_str = "\\!(Delay(%d)) " % line_delay_ms
    script_str += ms_get_telemetry_str
    script_str += "\n"
    return script_str


def norby_tmi_slice(tmi_list=None):
    script_str = ""
    for tmi_num in tmi_list:
        script_str += "\\!(Delay(%d)) " % line_delay_ms
        script_str += "tmi %d" % tmi_num
        script_str += "\n"
    return script_str


def set_brk_address(brk=1):
    script_str = ''
    script_str += "\\!(Delay(%d)) " % line_delay_ms
    script_str += set_brk_address_str + " "
    brk_ip_str = "10.6.1.201" if brk == 1 else "10.6.1.202"
    script_str += brk_ip_str
    script_str += "\n"
    return script_str


def ms_get_status():
    script_str = "\\!(Delay(%d)) " % line_delay_ms
    script_str += ms_get_status_str
    script_str += "\n"
    return script_str


def ms_format_iss():
    script_str = "\\!(Delay(%d)) " % line_delay_ms
    script_str += ms_format_iss_str
    script_str += "\n"
    return script_str


def ms_format_decor():
    script_str = "\\!(Delay(%d)) " % line_delay_ms
    script_str += ms_format_decor_str
    script_str += "\n"
    return script_str


def ms_get_frames(volume_str, frame_count):
    script_str = "\\!(Delay(%d)) " % line_delay_ms
    script_str += ms_get_frames_str
    _check_str_param(volume_str, "iss", "decor", "iss", "all", "flight_task_decor1", "flight_task_decor2",
                     "decor_status", error="Wrong LM volume name")
    script_str += " " + "%s" % volume_str
    script_str += " " + "%d" % frame_count
    if (frame_count - 1) != 0:
        script_str += "\n\\!(Delay(%d)) " % (line_delay_ms*(frame_count - 1))
    script_str += "\n"
    return script_str


def ms_set_pointer(volume_str, pointer_value):
    script_str = "\\!(Delay(%d)) " % line_delay_ms
    script_str += ms_set_pointer_str
    _check_str_param(volume_str, "iss", "decor", "iss", "all", "flight_task_decor1", "flight_task_decor2",
                     "decor_status", error="Wrong LM volume name")
    script_str += " " + "%s" % volume_str + " %d" % pointer_value
    script_str += "\n"
    return script_str


def ms_decor_set_fl_task(ft_num, step_number, cmd_type, cmd, delay_ms, repeat_cnter, data_list):
    write_str_1 = "%02X" % cmd_type
    write_str_1 += "%02X" % cmd
    write_str_1 += "%08X" % delay_ms
    write_str_1 += "%04X" % repeat_cnter
    write_str_2 = ""
    while len(data_list) < 8:
        data_list.append(0)
    write_str_2 += "".join([("%02X" % var) for var in data_list[:8]])
    if ft_num == 1:
        fl_task_offset = 128
    else:
        fl_task_offset = 2176
    script_str_1 = reg_write_string(6, 8, fl_task_offset + 16*step_number, 8, write_str_1)
    script_str_2 = reg_write_string(6, 8, fl_task_offset + 8 + 16*step_number, 8, write_str_2)
    return script_str_1 + script_str_2


def brk_set_time(desired_time="2000_01_01 00-00-00"):
    time_from_2000 = int(time.mktime(time.strptime(desired_time, "%Y_%m_%d %H-%M-%S")) - time.mktime(time.strptime("2000 01 01 00-00-00", "%Y %m %d %H-%M-%S"))) + 3  # из-за задержки отправки
    time_from_2000_plus_3 = time_from_2000 + 3
    time_from_2000_reverce = (((time_from_2000 >> 24) & 0xFF) << 0) + (((time_from_2000 >> 16) & 0xFF) << 8) + (
                ((time_from_2000 >> 8) & 0xFF) << 16) + (((time_from_2000 >> 0) & 0xFF) << 24)
    time_from_2000_reverce_plus_3 = (((time_from_2000_plus_3 >> 24) & 0xFF) << 0) + (((time_from_2000_plus_3 >> 16) & 0xFF) << 8) + (
            ((time_from_2000_plus_3 >> 8) & 0xFF) << 16) + (((time_from_2000_plus_3 >> 0) & 0xFF) << 24)
    script_str_1 = reg_write(1, 4, 0, 4, time_from_2000_reverce)
    script_str_2 = reg_write(2, 4, 0, 4, time_from_2000_reverce_plus_3)
    return script_str_1 + script_str_2


def _check_str_param(param, *arg, error="No one"):
    for check_str in arg:
        if param == check_str:
            return
    raise ValueError(error)
