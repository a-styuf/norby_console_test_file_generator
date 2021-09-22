# # Тестирование декор
#     # запись полетного задания 1
#     file_write(test_file, reg_write(6, 2, 3, 1, 0x00))
#     # чтение данных из памяти декор
#     file_write(test_file, ms_get_frames("decor", 50))
#     # инициализация памяти ДеКоР
#     file_write(test_file, ms_format_decor())
#     # полетное задание 1
#     file_write(test_file, ms_decor_set_fl_task(1, 0, 1, 1, 5000, 0, [3, 0, 0, 0, 0, 0, 0, 0]) ) # включение питания
#     file_write(test_file, ms_decor_set_fl_task(1, 1, 2, 1, 1000, 4, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#     file_write(test_file, ms_decor_set_fl_task(1, 2, 2, 1, 5000, 0, [0x62, 0xDC, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # erase system memory
#     file_write(test_file, ms_decor_set_fl_task(1, 3, 2, 1, 500, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#     file_write(test_file, ms_decor_set_fl_task(1, 4, 3, 0, 2000, 0, [0, 0, 0, 0, 0, 0, 0, 0]))  # синхронизация времени
#     file_write(test_file, ms_decor_set_fl_task(1, 5, 2, 1, 500, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#     file_write(test_file, ms_decor_set_fl_task(1, 6, 2, 1, 500, 0, [0x62, 0xD2, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # enable deffered record
#     file_write(test_file, ms_decor_set_fl_task(1, 7, 2, 1, 500, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#     file_write(test_file, ms_decor_set_fl_task(1, 8, 2, 1, 15000, 5, [0x72, 0xC1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # 1 monitoring block
#     file_write(test_file, ms_decor_set_fl_task(1, 9, 2, 1, 500, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#     file_write(test_file, ms_decor_set_fl_task(1, 10, 2, 1, 15000, 5, [0x72, 0xC3, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # 1 massive block
#     file_write(test_file, ms_decor_set_fl_task(1, 11, 2, 1, 1000, 4, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#     file_write(test_file, ms_decor_set_fl_task(1, 12, 1, 0, 2000, 0, [3, 0, 0, 0, 0, 0, 0, 0]))  # выключение питания
#     # полетное задание 2
#     file_write(test_file, ms_decor_set_fl_task(2, 0, 1, 1, 5000, 0, [3, 0, 0, 0, 0, 0, 0, 0]))  # включение питания
#     file_write(test_file, ms_decor_set_fl_task(2, 1, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#     file_write(test_file, ms_decor_set_fl_task(2, 2, 3, 0, 1000, 0, [0, 0, 0, 0, 0, 0, 0, 0]))  # синхронизация времени
#     file_write(test_file, ms_decor_set_fl_task(2, 3, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#     file_write(test_file, ms_decor_set_fl_task(2, 4, 2, 1, 500, 0, [0x62, 0xD2, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # enable deffered record
#     file_write(test_file, ms_decor_set_fl_task(2, 5, 2, 1, 1000, 4, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#     # проверка полетного задания 1
#     file_write(test_file, reg_read(6, 8, 128 + 0*128, 128))
#     file_write(test_file, reg_read(6, 8, 128 + 1*128, 128))
#     file_write(test_file, reg_read(6, 8, 128 + 2*128, 128))
#     # проверка полетного задания 2
#     file_write(test_file, reg_read(6, 8, 2176 + 0*128, 128))
#     file_write(test_file, reg_read(6, 8, 2176 + 1*128, 128))
#     file_write(test_file, reg_read(6, 8, 2176 + 2*128, 128))
#     # запись полетного задания 1
#     file_write(test_file, reg_write(6, 2, 3, 1, 0x01))
#     # запись полетного задания 2
#     file_write(test_file, reg_write(6, 2, 4, 1, 0x01))
#     # проверка записи полетного задания 1
#     file_write(test_file, ms_set_pointer("flight_task_decor1", 0))
#     file_write(test_file, ms_get_frames("flight_task_decor1", 4))
#     # проверка записи полетного задания 2
#     file_write(test_file, ms_set_pointer("flight_task_decor2", 0))
#     file_write(test_file, ms_get_frames("flight_task_decor2", 4))
#     # запуск полетного задания 1 одиночно
#     file_write(test_file, reg_write(6, 4, 28, 1, 0x02))
#     # чтение данных из памяти декор
#     file_write(test_file, ms_get_frames("decor", 100))

# # # полетное задание 1 (штатная работа с вычиткой 0xC1)
# # file_write(test_file, ms_decor_set_fl_task(1, 0, 1, 1, 5000, 0, [3, 0, 0, 0, 0, 0, 0, 0]))  # включение питания
# # file_write(test_file, ms_decor_set_fl_task(1, 1, 3, 0, 1000, 0, [0, 0, 0, 0, 0, 0, 0, 0]))  # синхронизация времени
# # file_write(test_file, ms_decor_set_fl_task(1, 2, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
# # file_write(test_file, ms_decor_set_fl_task(1, 3, 8, 0, 50000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 800 s fill
# # file_write(test_file, ms_decor_set_fl_task(1, 4, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
# # file_write(test_file, ms_decor_set_fl_task(1, 5, 8, 0, 50000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 800 s fill
# # file_write(test_file, ms_decor_set_fl_task(1, 6, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
# # file_write(test_file, ms_decor_set_fl_task(1, 7, 2, 1, 1000, 99, [0x72, 0xC1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # 100 monitoring block period 1 s
# # # полетное задание 2
# # file_write(test_file, ms_decor_set_fl_task(2, 0, 1, 1, 5000, 0, [3, 0, 0, 0, 0, 0, 0, 0]))  # включение питания
# # file_write(test_file, ms_decor_set_fl_task(2, 1, 3, 0, 1000, 0, [0, 0, 0, 0, 0, 0, 0, 0]))  # синхронизация времени
# # file_write(test_file, ms_decor_set_fl_task(2, 2, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
# # file_write(test_file, ms_decor_set_fl_task(2, 3, 2, 1, 1000, 0, [0x72, 0x17, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask monitoring levels
# # file_write(test_file, ms_decor_set_fl_task(2, 4, 2, 1, 1000, 0, [0x62, 0xE4, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00]))  # set decor number 3
# # # -------------------------------------------------------------
# # file_write(test_file, ms_decor_set_fl_task(2, 5, 2, 1, 1000, 0, [0x62, 0x91, 0x7D, 0x00, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH1_X1 125
# # file_write(test_file, ms_decor_set_fl_task(2, 6, 2, 1, 1000, 0, [0x62, 0x92, 0xD0, 0x07, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH1_X2 2000
# # file_write(test_file, ms_decor_set_fl_task(2, 7, 2, 1, 1000, 0, [0x62, 0x93, 0xA0, 0x0F, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH1_X3 4000
# # file_write(test_file, ms_decor_set_fl_task(2, 8, 2, 1, 1000, 0, [0x62, 0x94, 0xA0, 0x0F, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH1_X4 4000
# # #
# # file_write(test_file, ms_decor_set_fl_task(2, 9, 2, 1, 1000, 0, [0x62, 0x95, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH1_Y1 5
# # file_write(test_file, ms_decor_set_fl_task(2, 10, 2, 1, 1000, 0, [0x62, 0x96, 0x88, 0x13, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH1_Y2 5000
# # file_write(test_file, ms_decor_set_fl_task(2, 11, 2, 1, 1000, 0, [0x62, 0x97, 0x88, 0x13, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH1_Y3 5000
# # file_write(test_file, ms_decor_set_fl_task(2, 12, 2, 1, 1000, 0, [0x62, 0x98, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH1_Y4 5
# # # -------------------------------------------------------------
# # file_write(test_file, ms_decor_set_fl_task(2, 13, 2, 1, 1000, 0, [0x62, 0x99, 0xFA, 0x00, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH2_X1 250
# # file_write(test_file, ms_decor_set_fl_task(2, 14, 2, 1, 1000, 0, [0x62, 0x9A, 0x5E, 0x01, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH2_X2 350
# # file_write(test_file, ms_decor_set_fl_task(2, 15, 2, 1, 1000, 0, [0x62, 0x9B, 0xA0, 0x0F, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH2_X3 4000
# # file_write(test_file, ms_decor_set_fl_task(2, 16, 2, 1, 1000, 0, [0x62, 0x9C, 0xA0, 0x0F, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH2_X4 4000
# # #
# # file_write(test_file, ms_decor_set_fl_task(2, 17, 2, 1, 1000, 0, [0x62, 0x9D, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH2_Y1 5
# # file_write(test_file, ms_decor_set_fl_task(2, 18, 2, 1, 1000, 0, [0x62, 0x9E, 0x8C, 0x00, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH2_Y2 140
# # file_write(test_file, ms_decor_set_fl_task(2, 19, 2, 1, 1000, 0, [0x62, 0x9F, 0xDC, 0x05, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH2_Y3 1500
# # file_write(test_file, ms_decor_set_fl_task(2, 20, 2, 1, 1000, 0, [0x62, 0xA0, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH2_Y4 5
# # # -------------------------------------------------------------
# # file_write(test_file, ms_decor_set_fl_task(2, 21, 2, 1, 1000, 0, [0x62, 0xA1, 0x60, 0x04, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH3_X1 1120
# # file_write(test_file, ms_decor_set_fl_task(2, 22, 2, 1, 1000, 0, [0x62, 0xA2, 0xF4, 0x01, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH3_X2 500
# # file_write(test_file, ms_decor_set_fl_task(2, 23, 2, 1, 1000, 0, [0x62, 0xA3, 0xA0, 0x0F, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH3_X3 4000
# # file_write(test_file, ms_decor_set_fl_task(2, 24, 2, 1, 1000, 0, [0x62, 0xA4, 0xA0, 0x0F, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH3_X4 4000
# # #
# # file_write(test_file, ms_decor_set_fl_task(2, 25, 2, 1, 1000, 0, [0x62, 0xA5, 0xB3, 0x01, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH3_Y1 435
# # file_write(test_file, ms_decor_set_fl_task(2, 26, 2, 1, 1000, 0, [0x62, 0xA6, 0xE8, 0x03, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH3_Y2 1000
# # file_write(test_file, ms_decor_set_fl_task(2, 27, 2, 1, 1000, 0, [0x62, 0xA7, 0x04, 0x29, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH3_Y3 10500
# # file_write(test_file, ms_decor_set_fl_task(2, 28, 2, 1, 1000, 0, [0x62, 0xA8, 0xDC, 0x05, 0x00, 0x00, 0x00, 0x00]))  # Set MONITOR_COORD_CH3_Y4 1500
# # # -------------------------------------------------------------
# # file_write(test_file, ms_decor_set_fl_task(2, 29, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
# # file_write(test_file, ms_decor_set_fl_task(2, 30, 2, 1, 1000, 0, [0x72, 0x17, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask monitoring levels
# # file_write(test_file, ms_decor_set_fl_task(2, 31, 8, 0, 10000, 60, [0, 0, 0, 0, 0, 0, 0, 0]))  # fill 600 s
# # file_write(test_file, ms_decor_set_fl_task(2, 32, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
# #
# # # проверка полетного задания 1
# # file_write(test_file, reg_read(6, 8, 128 + 0*128, 128))
# # file_write(test_file, reg_read(6, 8, 128 + 1*128, 128))
# # file_write(test_file, reg_read(6, 8, 128 + 2*128, 128))
# # # проверка полетного задания 2
# # file_write(test_file, reg_read(6, 8, 2176 + 0*128, 128))
# # file_write(test_file, reg_read(6, 8, 2176 + 1*128, 128))
# # file_write(test_file, reg_read(6, 8, 2176 + 2*128, 128))
# # file_write(test_file, reg_read(6, 8, 2176 + 3*128, 128))
# # file_write(test_file, reg_read(6, 8, 2176 + 4*128, 128))
# # file_write(test_file, reg_read(6, 8, 2176 + 5*128, 128))
# # # запись полетного задания 1
# # file_write(test_file, reg_write(6, 2, 3, 1, 0x01))
# # # запись полетного задания 2
# # file_write(test_file, reg_write(6, 2, 4, 1, 0x01))
# # # проверка записи полетного задания 1
# # file_write(test_file, ms_set_pointer("flight_task_decor1", 0))
# # file_write(test_file, ms_get_frames("flight_task_decor1", 4))
# # # проверка записи полетного задания 2
# # file_write(test_file, ms_set_pointer("flight_task_decor2", 0))
# # file_write(test_file, ms_get_frames("flight_task_decor2", 8))

#2021_02_18
# file_write(test_file, norby_tmi_slice(tmi_list=[0, 1, 2, 3, 4, 5, 6, 7, 8]))
#         file_write(test_file, lm_power_ctrl(mode='on'))
#         # инициализация памяти ДеКоР
#         file_write(test_file, ms_format_decor())
#         # полетное задание 1
#         # # # полетное задание 1 (штатная работа с вычиткой 0xC1)
#         file_write(test_file, ms_decor_set_fl_task(1, 0, 1, 1, 5000, 0, [3, 0, 0, 0, 0, 0, 0, 0]))  # включение питания
#         file_write(test_file, ms_decor_set_fl_task(1, 1, 3, 0, 1000, 0, [0, 0, 0, 0, 0, 0, 0, 0]))  # синхронизация времени
#         file_write(test_file, ms_decor_set_fl_task(1, 2, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#         file_write(test_file, ms_decor_set_fl_task(1, 3, 8, 0, 50000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 800 s fill
#         file_write(test_file, ms_decor_set_fl_task(1, 4, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#         file_write(test_file, ms_decor_set_fl_task(1, 5, 8, 0, 50000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 800 s fill
#         file_write(test_file, ms_decor_set_fl_task(1, 6, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#         file_write(test_file, ms_decor_set_fl_task(1, 7, 2, 1, 1000, 99, [0x72, 0xC1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # 100 monitoring block period 1s
#         # полетное задание 2
#         file_write(test_file, ms_decor_set_fl_task(2, 0, 1, 1, 5000, 0, [3, 0, 0, 0, 0, 0, 0, 0]))  # включение питания
#         file_write(test_file, ms_decor_set_fl_task(2, 1, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#         file_write(test_file, ms_decor_set_fl_task(2, 2, 3, 0, 1000, 0, [0, 0, 0, 0, 0, 0, 0, 0]))  # синхронизация времени
#         file_write(test_file, ms_decor_set_fl_task(2, 3, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#         file_write(test_file, ms_decor_set_fl_task(2, 4, 2, 1, 500, 0, [0x62, 0xCA, 0x32, 0x00, 0x00, 0x00, 0x00, 0x00]))  # enable deffered record
#         file_write(test_file, ms_decor_set_fl_task(2, 5, 2, 1, 1000, 4, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#         file_write(test_file, ms_decor_set_fl_task(2, 6, 2, 1, 500, 0, [0x62, 0xC8, 0xC0, 0xF9, 0x30, 0x60, 0x00, 0x00]))  # enable deffered record
#         file_write(test_file, ms_decor_set_fl_task(2, 7, 2, 1, 1000, 4, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#         #
#         file_write(test_file, norby_tmi_slice(tmi_list=[0, 1, 2, 3, 4, 5, 6, 7, 8]))
#         # проверка полетного задания 1
#         file_write(test_file, reg_read(6, 8, 128 + 0*128, 128))
#         file_write(test_file, reg_read(6, 8, 128 + 1*128, 128))
#         file_write(test_file, reg_read(6, 8, 128 + 2*128, 128))
#         # проверка полетного задания 2
#         file_write(test_file, reg_read(6, 8, 2176 + 0*128, 128))
#         file_write(test_file, reg_read(6, 8, 2176 + 1*128, 128))
#         file_write(test_file, reg_read(6, 8, 2176 + 2*128, 128))
#         # запись полетного задания 1
#         file_write(test_file, reg_write(6, 2, 3, 1, 0x01))
#         # запись полетного задания 2
#         file_write(test_file, reg_write(6, 2, 4, 1, 0x01))
#         #
#         file_write(test_file, norby_tmi_slice(tmi_list=[0, 1, 2, 3, 4, 5, 6, 7, 8]))
#         # проверка записи полетного задания 1
#         file_write(test_file, ms_set_pointer("flight_task_decor1", 0))
#         file_write(test_file, ms_get_frames("flight_task_decor1", 4))
#         # проверка записи полетного задания 2
#         file_write(test_file, ms_set_pointer("flight_task_decor2", 0))
#         file_write(test_file, ms_get_frames("flight_task_decor2", 4))
#         # запуск полетного задания 1 одиночно
#         file_write(test_file, reg_write(6, 4, 28, 1, 0x02))
#         # чтение данных из памяти декор
#         file_write(test_file, ms_get_frames("decor", 100))
#         #
#         file_write(test_file, norby_tmi_slice(tmi_list=[0, 1, 2, 3, 4, 5, 6, 7, 8]))

# 2020_02_19
# file_name = "lm_pwr_on_full_tmi_read_pl_mem_run_iss_pl_5_pl_dcr_on"
# with open(set_script_name(file_name) + ".txt", "w") as test_file:
#     file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#     file_write(test_file, lm_power_ctrl(mode='on'))
#     file_write(test_file, norby_tmi_slice(tmi_list=[1]))
#     file_write(test_file, ms_get_telemetry())
#     #
#     file_write(test_file, lm_pl_decor_cyclogram_run(mode="cyclic", ft_num=1))
#     file_write(test_file, lm_pl_iss_cyclogram_run(mode='single', c_num=5))
#     for i in range(10):
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         file_write(test_file, ms_get_telemetry())
#         file_write(test_file, read_pl_mem_30_s())
#     for i in range(3):
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         file_write(test_file, ms_get_telemetry())
#         file_write(test_file, read_pl_mem_30_s())

# 27_02_2021
# file_name = "lm_pwr_on_full_tmi_read_pl_mem_run_iss_pl_1_pl_dcr_on_flight_task_read"
# with open(set_script_name(file_name) + ".txt", "w") as test_file:
#     file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#     file_write(test_file, lm_power_ctrl(mode='on'))
#     file_write(test_file, norby_tmi_slice(tmi_list=[1]))
#     file_write(test_file, ms_get_telemetry())
#     #
#     for k in range(2):
#         file_write(test_file, ms_set_pointer("flight_task_decor1", 0))
#         file_write(test_file, ms_set_pointer("flight_task_decor2", 0))
#         for j in range(10):
#             # проверка записи полетного задания 1
#             file_write(test_file, ms_get_frames("flight_task_decor1", 1))
#         #
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         for j in range(10):
#             # проверка записи полетного задания 2
#             file_write(test_file, ms_get_frames("flight_task_decor2", 1))
#         #
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#     #
#     file_write(test_file, lm_pl_decor_cyclogram_run(mode="cyclic", ft_num=1))
#     file_write(test_file, lm_pl_iss_cyclogram_run(mode='single', c_num=1))
#     for i in range(10):
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         file_write(test_file, ms_get_telemetry())
#         file_write(test_file, read_pl_mem_30_s())
#     for i in range(3):
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         file_write(test_file, ms_get_telemetry())
#         file_write(test_file, read_pl_mem_30_s())

# 2021_02_27
# file_name = "write_dcrft_1_2_change _dcr_period_5s_run_iss_c5"
# with open(set_script_name(file_name) + ".txt", "w") as test_file:
#     file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#     #
#     file_write(test_file, lm_power_ctrl(mode='on'))
#     # инициализация памяти ДеКоР
#     file_write(test_file, lm_pl_decor_cyclogram_run(mode='off'))
#     file_write(test_file, ms_format_decor())
#     for i in range(2):
#         # полетное задание 1 (штатная работа с вычиткой 0xC1)
#         file_write(test_file, ms_decor_set_fl_task(1, 0, 1, 1, 5000, 0, [3, 0, 0, 0, 0, 0, 0, 0]))  # включение питания
#         file_write(test_file,
#                    ms_decor_set_fl_task(1, 1, 3, 0, 1000, 0, [0, 0, 0, 0, 0, 0, 0, 0]))  # синхронизация времени
#         file_write(test_file, ms_decor_set_fl_task(1, 2, 2, 1, 1000, 0,
#                                                    [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#         file_write(test_file, ms_decor_set_fl_task(1, 3, 8, 0, 25000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 400 s fill
#         file_write(test_file, ms_decor_set_fl_task(1, 4, 8, 0, 25000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 400 s fill
#         file_write(test_file, ms_decor_set_fl_task(1, 5, 2, 1, 1000, 0,
#                                                    [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#         file_write(test_file, ms_decor_set_fl_task(1, 6, 8, 0, 25000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 400 s fill
#         file_write(test_file, ms_decor_set_fl_task(1, 7, 8, 0, 25000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 400 s fill
#         file_write(test_file, ms_decor_set_fl_task(1, 8, 2, 1, 1000, 0,
#                                                    [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#         file_write(test_file, ms_decor_set_fl_task(1, 9, 2, 1, 1000, 99, [0x72, 0xC1, 0x00, 0x00, 0x00, 0x00, 0x00,
#                                                                           0x00]))  # 100 monitoring block period 1s24
#         #
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         # полетное задание 2
#         file_write(test_file, ms_decor_set_fl_task(2, 0, 1, 1, 5000, 0, [3, 0, 0, 0, 0, 0, 0, 0]))  # включение питания
#         file_write(test_file, ms_decor_set_fl_task(2, 1, 2, 1, 1000, 0,
#                                                    [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#         file_write(test_file,
#                    ms_decor_set_fl_task(2, 2, 3, 0, 1000, 0, [0, 0, 0, 0, 0, 0, 0, 0]))  # синхронизация времени
#         file_write(test_file, ms_decor_set_fl_task(2, 3, 2, 1, 1000, 0,
#                                                    [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#         file_write(test_file, ms_decor_set_fl_task(2, 4, 2, 1, 500, 0, [0x62, 0xCA, 0x32, 0x00, 0x00, 0x00, 0x00,
#                                                                         0x00]))  # change decor polling period
#         file_write(test_file, ms_decor_set_fl_task(2, 5, 2, 1, 1000, 4,
#                                                    [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#         file_write(test_file, ms_decor_set_fl_task(2, 6, 2, 1, 10000, 0, [0x62, 0xC8, 0x00, 0xDD, 0x3A, 0x60, 0x00,
#                                                                           0x00]))  # enable deffered record
#         file_write(test_file, ms_decor_set_fl_task(2, 7, 2, 1, 1000, 4,
#                                                    [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#         #
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#     for i in range(2):
#         # запись полетного задания 1
#         file_write(test_file, reg_write(6, 2, 3, 1, 0x01))
#         # запись полетного задания 2
#         file_write(test_file, reg_write(6, 2, 4, 1, 0x01))
#     for i in range(3):
#         # проверка записи полетного задания 1
#         file_write(test_file, ms_set_pointer("flight_task_decor1", 0))
#         file_write(test_file, ms_get_frames("flight_task_decor1", 3))
#         # проверка записи полетного задания 2
#         file_write(test_file, ms_set_pointer("flight_task_decor2", 0))
#         file_write(test_file, ms_get_frames("flight_task_decor2", 3))
#     # запуск полетного задания 1 одиночно
#     #
#     file_write(test_file, lm_pl_iss_cyclogram_run(mode='single', c_num=5))
#     for i in range(5):
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))

# file_name = "write_dcrft_1_2_change_dcr_period_5s_run_iss_c5_ver3"
#     with open(set_script_name(file_name) + ".txt", "w") as test_file:
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         #
#         file_write(test_file, lm_power_ctrl(mode='on'))
#         # инициализация памяти ДеКоР
#         file_write(test_file, lm_pl_decor_cyclogram_run(mode='off'))
#         file_write(test_file, ms_format_decor())
#         for i in range(1):
#             # полетное задание 1 (штатная работа с вычиткой 0xC1)
#             file_write(test_file, ms_decor_set_fl_task(1, 0, 1, 1, 5000, 0, [3, 0, 0, 0, 0, 0, 0, 0]))  # включение питания
#             file_write(test_file, ms_decor_set_fl_task(1, 1, 3, 0, 1000, 0, [0, 0, 0, 0, 0, 0, 0, 0]))  # синхронизация времени
#             file_write(test_file, ms_decor_set_fl_task(1, 2, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#             file_write(test_file, ms_decor_set_fl_task(1, 3, 8, 0, 25000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 400 s fill
#             file_write(test_file, ms_decor_set_fl_task(1, 4, 8, 0, 25000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 400 s fill
#             file_write(test_file, ms_decor_set_fl_task(1, 5, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#             file_write(test_file, ms_decor_set_fl_task(1, 6, 8, 0, 25000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 400 s fill
#             file_write(test_file, ms_decor_set_fl_task(1, 7, 8, 0, 25000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 400 s fill
#             file_write(test_file, ms_decor_set_fl_task(1, 8, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#             file_write(test_file, ms_decor_set_fl_task(1, 9, 2, 1, 1000, 99, [0x72, 0xC1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # 100 monitoring block period 1s
#             file_write(test_file, ms_decor_set_fl_task(1, 10, 0, 0, 0, 0, [0xDE, 0xAD, 0x00, 0x00, 0x00, 0x00, 0xDE, 0xAD]))  # empty
#             #
#             file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#             # полетное задание 2
#             file_write(test_file, ms_decor_set_fl_task(2, 0, 1, 1, 5000, 0, [3, 0, 0, 0, 0, 0, 0, 0]))  # включение питания
#             file_write(test_file, ms_decor_set_fl_task(2, 1, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#             file_write(test_file, ms_decor_set_fl_task(2, 2, 3, 0, 1000, 0, [0, 0, 0, 0, 0, 0, 0, 0]))  # синхронизация времени
#             file_write(test_file, ms_decor_set_fl_task(2, 3, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#             file_write(test_file, ms_decor_set_fl_task(2, 4, 2, 1, 500, 0, [0x62, 0xCA, 0x32, 0x00, 0x00, 0x00, 0x00, 0x00]))  # change decor polling period
#             file_write(test_file, ms_decor_set_fl_task(2, 5, 2, 1, 1000, 4, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#             file_write(test_file, ms_decor_set_fl_task(2, 6, 2, 1, 10000, 0, [0x62, 0xC8, 0x00, 0xD7, 0x3C, 0x60, 0x00, 0x00]))  # enable deffered record
#             file_write(test_file, ms_decor_set_fl_task(2, 7, 2, 1, 1000, 4, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#             file_write(test_file, ms_decor_set_fl_task(2, 8, 0, 0, 0, 0, [0xDE, 0xAD, 0x00, 0x00, 0x00, 0x00, 0xDE, 0xAD]))  # empty
#             #
#             file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         for i in range(2):
#             # запись полетного задания 1
#             file_write(test_file, reg_write(6, 2, 3, 1, 0x01))
#             # запись полетного задания 2
#             file_write(test_file, reg_write(6, 2, 4, 1, 0x01))
#         for i in range(4):
#             # проверка записи полетного задания 1
#             file_write(test_file, ms_set_pointer("flight_task_decor1", 0))
#             file_write(test_file, ms_get_frames("flight_task_decor1", 1))
#             file_write(test_file, ms_get_frames("flight_task_decor1", 1))
#             file_write(test_file, ms_get_frames("flight_task_decor1", 1))
#             # проверка записи полетного задания 2
#             file_write(test_file, ms_set_pointer("flight_task_decor2", 0))
#             file_write(test_file, ms_get_frames("flight_task_decor2", 1))
#             file_write(test_file, ms_get_frames("flight_task_decor2", 1))
#             file_write(test_file, ms_get_frames("flight_task_decor2", 1))
#         # запуск полетного задания 1 одиночно
#         file_write(test_file, lm_pl_iss_cyclogram_run(mode='single', c_num=5))
#         for i in range(5):
#             file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))

#  #  standart cyclogramms
# file_name = "lm_pwr_on_iss_c5_dcr_cyclic_ft_5"
# with open(set_script_name(file_name) + ".txt", "w") as test_file:
#     file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#     file_write(test_file, lm_power_ctrl(mode='on'))
#     file_write(test_file, norby_tmi_slice(tmi_list=[1]))
#     file_write(test_file, ms_get_telemetry())
#     #
#     file_write(test_file, lm_pl_decor_cyclogram_run(mode="cyclic", ft_num=2))
#     file_write(test_file, lm_pl_iss_cyclogram_run(mode='single', c_num=5))
#     for i in range(15):
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         file_write(test_file, ms_get_telemetry())
#         file_write(test_file, read_pl_mem_30_s())

# 2021_03_18
# file_name = "lm_on_iss&dcr_cyclic"
# with open(set_script_name(file_name) + ".txt", "w") as test_file:
#     file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))  # 24 s
#     file_write(test_file, ms_get_telemetry())  # 3
#     file_write(test_file, lm_power_ctrl(mode='on'))  # 3
#     file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))  # 24 s
#     file_write(test_file, ms_get_telemetry())  # 3
#     #
#     file_write(test_file, lm_pl_decor_cyclogram_run(mode="cyclic", ft_num=2))  # 3
#     file_write(test_file, lm_pl_iss_cyclogram_run(mode='cyclic', c_num=1))  # 3
#     for i in range(10):
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))  # 27
#         file_write(test_file, ms_get_telemetry())  # 3
#         file_write(test_file, read_pl_mem_30_s())  # 30

# 2021_06_18
# if __name__ == "__main__":
#     file_name = "write_dcrft_1_change_period_of_dcr_polling_60_fr_per_hour"
#     with open(set_script_name(file_name) + ".txt", "w") as test_file:
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         #
#         file_write(test_file, lm_power_ctrl(mode='on'))
#         # инициализация памяти ДеКоР
#         file_write(test_file, lm_pl_decor_cyclogram_run(mode='off'))
#         file_write(test_file, ms_format_decor())
#         for i in range(1):
#             # полетное задание 1 (штатная работа с вычиткой 0xC1) ~1500 кадров в сутки
#             file_write(test_file, ms_decor_set_fl_task(1, 0, 1, 1, 5000, 0, [3, 0, 0, 0, 0, 0, 0, 0]))  # включение питания
#             file_write(test_file, ms_decor_set_fl_task(1, 1, 3, 0, 1000, 0, [0, 0, 0, 0, 0, 0, 0, 0]))  # синхронизация времени
#             file_write(test_file, ms_decor_set_fl_task(1, 2, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#             file_write(test_file, ms_decor_set_fl_task(1, 3, 8, 0, 25000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 400 s fill
#             file_write(test_file, ms_decor_set_fl_task(1, 4, 8, 0, 25000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 400 s fill
#             file_write(test_file, ms_decor_set_fl_task(1, 5, 8, 0, 25000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 400 s fill
#             file_write(test_file, ms_decor_set_fl_task(1, 6, 8, 0, 25000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 400 s fill
#             file_write(test_file, ms_decor_set_fl_task(1, 7, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#             #
#             file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#             #
#             file_write(test_file, ms_decor_set_fl_task(1, 8, 8, 0, 25000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 400 s fill
#             file_write(test_file, ms_decor_set_fl_task(1, 9, 8, 0, 25000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 400 s fill
#             file_write(test_file, ms_decor_set_fl_task(1, 10, 8, 0, 25000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 400 s fill
#             file_write(test_file, ms_decor_set_fl_task(1, 11, 8, 0, 25000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 400 s fill
#             file_write(test_file, ms_decor_set_fl_task(1, 12, 8, 0, 25000, 15, [0, 0, 0, 0, 0, 0, 0, 0]))  # 400 s fill
#             file_write(test_file, ms_decor_set_fl_task(1, 13, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#             file_write(test_file, ms_decor_set_fl_task(1, 14, 2, 1, 1000, 59, [0x72, 0xC1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # 60 monitoring block period 1s
#             file_write(test_file, ms_decor_set_fl_task(1, 15, 0, 0, 0, 0, [0xDE, 0xAD, 0x00, 0x00, 0x00, 0x00, 0xDE, 0xAD]))  # empty
#             #
#             file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#             #
#         for i in range(2):
#             # запись полетного задания 1
#             file_write(test_file, reg_write(6, 2, 3, 1, 0x01))
#             #
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         for i in range(4):
#             # проверка записи полетного задания 1
#             file_write(test_file, ms_set_pointer("flight_task_decor1", 0))
#             file_write(test_file, ms_get_frames("flight_task_decor1", 1))
#             file_write(test_file, ms_get_frames("flight_task_decor1", 1))
#             file_write(test_file, ms_get_frames("flight_task_decor1", 1))
#             file_write(test_file, ms_get_frames("flight_task_decor1", 1))
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         # запуск полетного задания 1 одиночно
#         file_write(test_file, lm_pl_iss_cyclogram_run(mode='single', c_num=5))
#         for i in range(5):
#             file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))

# # 2021_07_05
# if __name__ == "__main__":
#     # часть 1
#     file_name = "write_dcrft_2_use_rd_ptr_shift_part_1"
#     with open(set_script_name(file_name) + ".txt", "w") as test_file:
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         #
#         file_write(test_file, lm_power_ctrl(mode='on'))
#         # инициализация памяти ДеКоР
#         file_write(test_file, lm_pl_decor_cyclogram_run(mode='off'))
#         file_write(test_file, ms_format_decor())
#         for i in range(2):
#             # полетное задание 2 (штатная работа с вычиткой по 0xC1) ~1440 кадров в сутки
#             file_write(test_file, ms_decor_set_fl_task(2, 0, 1, 1, 5000, 0, [3, 0, 0, 0, 0, 0, 0, 0]))  # включение питания
#             file_write(test_file, ms_decor_set_fl_task(2, 1, 3, 0, 1000, 0, [0, 0, 0, 0, 0, 0, 0, 0]))  # синхронизация времени
#             file_write(test_file, ms_decor_set_fl_task(2, 2, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#             # 6 hours
#             offset = 0+3
#             for j in range(6):
#                 file_write(test_file, ms_decor_set_fl_task(2, offset + 0 + 2 * j, 8, 0, 36000, 99, [0, 0, 0, 0, 0, 0, 0, 0]))  # 3600s=1h fill
#                 file_write(test_file, ms_decor_set_fl_task(2, offset + 1 + 2 * j, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#             file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#             # 6 hours
#             offset = 12+3
#             for j in range(6):
#                 file_write(test_file, ms_decor_set_fl_task(2, offset + 0 + 2 * j, 8, 0, 36000, 99, [0, 0, 0, 0, 0, 0, 0, 0]))  # 3600s=1h fill
#                 file_write(test_file, ms_decor_set_fl_task(2, offset + 1 + 2 * j, 2, 1, 1000, 0, [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#             file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#             #
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         # чтение из оперативных данных
#         for i in range(10):
#             file_write(test_file, reg_read(dev_id=6, var_id=8, offset=128+2048+128*i, length=128))
#         #
#         for i in range(10):
#             file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#     # часть 2
#     file_name = "write_dcrft_2_use_rd_ptr_shift_part_2"
#     with open(set_script_name(file_name) + ".txt", "w") as test_file:
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         #
#         file_write(test_file, lm_power_ctrl(mode='on'))
#         # инициализация памяти ДеКоР
#         file_write(test_file, lm_pl_decor_cyclogram_run(mode='off'))
#         file_write(test_file, ms_format_decor())
#         for i in range(2):
#             # полетное задание 2 (штатная работа с вычиткой по 0xC1) ~1440 кадров в сутки
#             # 6 hours
#             offset = 24 + 3
#             for j in range(6):
#                 file_write(test_file, ms_decor_set_fl_task(2, offset + 0 + 2 * j, 8, 0, 36000, 99,
#                                                            [0, 0, 0, 0, 0, 0, 0, 0]))  # 3600s=1h fill
#                 file_write(test_file, ms_decor_set_fl_task(2, offset + 1 + 2 * j, 2, 1, 1000, 0,
#                                                            [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00,
#                                                             0x00]))  # ask status
#             file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#             # 6 hours
#             offset = 36 + 3
#             for j in range(6):
#                 file_write(test_file, ms_decor_set_fl_task(2, offset + 0 + 2 * j, 8, 0, 36000, 99,
#                                                            [0, 0, 0, 0, 0, 0, 0, 0]))  # 3600s=1h fill
#                 file_write(test_file, ms_decor_set_fl_task(2, offset + 1 + 2 * j, 2, 1, 1000, 0,
#                                                            [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00,
#                                                             0x00]))  # ask status
#             file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#             #
#             offset = 48 + 3
#             for j in range(10):
#                 file_write(test_file, ms_decor_set_fl_task(2, offset + j, 2, 1, 1000, 144,
#                                                            [0x72, 0xC1, 0x00, 0x00, 0x00, 0x00, 0x00,
#                                                             0x00]))  # 60 monitoring block period 1s
#             # 44 62 C8 69 00 00 69 00 00 3B 0D 0A
#             file_write(test_file,
#                        ms_decor_set_fl_task(2, 61, 2, 1, 1000, 0, [0x62, 0xC8, 0x69, 0x00, 0x00, 0x69, 0x00, 0x00]))
#             file_write(test_file, ms_decor_set_fl_task(2, 62, 0, 0, 0, 0,
#                                                        [0xDE, 0xAD, 0x00, 0x00, 0x00, 0x00, 0xDE, 0xAD]))  # empty
#             file_write(test_file, ms_decor_set_fl_task(2, 63, 0, 0, 0, 0,
#                                                        [0, 0, 0, 0, 0, 0, 0, 0]))  # empty
#             file_write(test_file, ms_decor_set_fl_task(2, 64, 0, 0, 0, 0,
#                                                        [0, 0, 0, 0, 0, 0, 0, 0]))  # empty
#             #
#             file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#             #
#         # чтение из оперативных данных
#         for i in range(10):
#             file_write(test_file, reg_read(dev_id=6, var_id=8, offset=128 + 2048 + 128 * i, length=128))
#         #
#         for i in range(10):
#             file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#     # часть 2
#     file_name = "write_dcrft_2_use_rd_ptr_shift_part_3"
#     with open(set_script_name(file_name) + ".txt", "w") as test_file:
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         #
#         file_write(test_file, lm_power_ctrl(mode='on'))
#         # инициализация памяти ДеКоР
#         file_write(test_file, lm_pl_decor_cyclogram_run(mode='off'))
#         file_write(test_file, ms_format_decor())
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         for i in range(2):
#             # проверка записи полетного задания 1
#             file_write(test_file, ms_set_pointer("flight_task_decor2", 0))
#             file_write(test_file, ms_get_frames("flight_task_decor2", 1))
#             file_write(test_file, ms_get_frames("flight_task_decor2", 1))
#             file_write(test_file, ms_get_frames("flight_task_decor2", 1))
#             file_write(test_file, ms_get_frames("flight_task_decor2", 1))
#             file_write(test_file, ms_get_frames("flight_task_decor2", 1))
#             file_write(test_file, ms_get_frames("flight_task_decor2", 1))
#             file_write(test_file, ms_get_frames("flight_task_decor2", 1))
#             file_write(test_file, ms_get_frames("flight_task_decor2", 1))
#             file_write(test_file, ms_get_frames("flight_task_decor2", 1))
#             file_write(test_file, ms_get_frames("flight_task_decor2", 1))
#             file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         #
#         for i in range(20):
#             file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))

#  2020_07_19
# for i in range(1, 6):
#     file_name = "lm_on_iss_%d_dcr_3" % i
#     with open(set_script_name(file_name) + ".txt", "w") as test_file:
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         file_write(test_file, lm_power_ctrl(mode='on'))
#         file_write(test_file, norby_tmi_slice(tmi_list=[1]))
#         file_write(test_file, ms_get_telemetry())
#         #
#         file_write(test_file, lm_pl_decor_cyclogram_run(mode="cyclic", ft_num=3))
#         file_write(test_file, lm_pl_iss_cyclogram_run(mode='single', c_num=i))
#         #
#         file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#         for i in range(3):
#             file_write(test_file, read_pl_mem(frame_num=10, mem_type="iss"))
#             file_write(test_file, read_pl_mem(frame_num=100, mem_type="decor"))
#             file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#             file_write(test_file, ms_get_telemetry())

# 2020_08_23
# file_name = "write_dcrft_2_2H_use_rd_ptr_shift"
# with open(set_script_name(file_name) + ".txt", "w") as test_file:
#     file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#     #
#     file_write(test_file, lm_power_ctrl(mode='on'))
#     # инициализация памяти ДеКоР
#     file_write(test_file, lm_pl_decor_cyclogram_run(mode='off'))
#     file_write(test_file, ms_format_decor())
#     #
#     for i in range(3):
#         # полетное задание 2 (штатная работа с вычиткой по 0xC1) 800 кадров в сутки
#         file_write(test_file, ms_decor_set_fl_task(2, 0, 1, 1, 5000, 0, [3, 0, 0, 0, 0, 0, 0, 0]))  # включение питания
#         file_write(test_file,
#                    ms_decor_set_fl_task(2, 1, 3, 0, 1000, 0, [0, 0, 0, 0, 0, 0, 0, 0]))  # синхронизация времени
#         file_write(test_file, ms_decor_set_fl_task(2, 2, 2, 1, 1000, 0,
#                                                    [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#         # 1 hours
#         file_write(test_file, ms_decor_set_fl_task(2, 3, 8, 0, 36000, 99, [0, 0, 0, 0, 0, 0, 0, 0]))  # 1h fill
#         file_write(test_file, ms_decor_set_fl_task(2, 4, 2, 1, 1000, 0,
#                                                    [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#         # вычитка 100 кадров
#         file_write(test_file, ms_decor_set_fl_task(2, 5, 2, 1, 1000, 99, [0x72, 0xC1, 0x00, 0x00, 0x00, 0x00, 0x00,
#                                                                           0x00]))  # 100 monitoring block period 1s
#         # 1 hours
#         file_write(test_file, ms_decor_set_fl_task(2, 6, 8, 0, 36000, 99, [0, 0, 0, 0, 0, 0, 0, 0]))  # 1h fill
#         file_write(test_file, ms_decor_set_fl_task(2, 7, 2, 1, 1000, 0,
#                                                    [0x72, 0xC7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))  # ask status
#         # вычитка 100 кадров
#         file_write(test_file, ms_decor_set_fl_task(2, 8, 2, 1, 1000, 99, [0x72, 0xC1, 0x00, 0x00, 0x00, 0x00, 0x00,
#                                                                           0x00]))  # 100 monitoring block period 1s
#         # сдвиг времени в будущее
#         file_write(test_file,
#                    ms_decor_set_fl_task(2, 9, 2, 1, 1000, 0, [0x62, 0xC8, 0x69, 0x00, 0x00, 0x69, 0x00, 0x00]))
#         #
#         file_write(test_file, ms_decor_set_fl_task(2, 10, 0, 0, 30000, 0,
#                                                    [0xDE, 0xAD, 0x00, 0x00, 0x00, 0x00, 0xDE, 0xAD]))  # empty
#         for j in range(5):
#             file_write(test_file, ms_decor_set_fl_task(2, 11 + j, 0, 0, 0, 0, [0, 0, 0, 0, 0, 0, 0, 0]))  # empty
#         #
#     file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#     # чтение из оперативных данных
#     for i in range(5):
#         file_write(test_file, reg_read(dev_id=6, var_id=8, offset=128 + 2048 + 128 * i, length=128))
#     #
#     file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#     # запись полетного задания в ПЗУ
#     file_write(test_file, reg_write(6, 2, 4, 1, 0x01))
#     #
#     for i in range(5):
#         # проверка записи полетного задания 1
#         file_write(test_file, ms_set_pointer("flight_task_decor2", 0))
#         file_write(test_file, ms_get_frames("flight_task_decor2", 1))
#         file_write(test_file, ms_get_frames("flight_task_decor2", 1))
#         file_write(test_file, ms_get_frames("flight_task_decor2", 1))
#     file_write(test_file, norby_tmi_slice(tmi_list=[1, 2, 3, 4, 5, 6, 7, 8]))
#     #