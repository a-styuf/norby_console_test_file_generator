﻿# Инструкция к работе с скриптом генерации команд для синхронизации времени *set_time_to_brk_script.py*
_______
Данный скрипт предназаначен для генерации команды для контроллера радиоканала НГУ по формату, используемому в **Норби 1**:
1. Запускать срипт необходимо с аргументом, в котором содержится информация о времени синхронизации по формату <%Y_%m_%d %H:%M:%S>. Пример:"2000_01_01 00:00:10"
2. Если срипт правильно распознает, то создастся файл следующего содержания:
  > \!(Delay(3000)) reg write 1 4 0 4 0D000000
  > \!(Delay(3000)) reg write 2 4 0 4 10000000
3. Время прописывается сразу в два БРК, во второй с задержкой 3 секунды (учтена задержка отправки из терминала)
4. Для удобства в проекте присутсвует *set_time_to_brk_script.bat*, в котором можно прописать необходимое вам время, и запустить его из командой строки.

Пример:
* Предположим вы решили синхронизовать Норби в ближайший сеанс, который произойдет 1 апреля 2021 года в 13:13:00.
* Тогда в аргументе вызова скрипта из командной строки (или правите .bat файл) вы пишите <python set_time_to_brk_script.py "2021_04_01 13:13:00">
* После чего запускаете скрипт (или .bat соответственно)
* В папке со скриптом появится файл *brk_set_time_script.txt* со следующим текстом (в консоли также появится данный текст):
> \!(Delay(3000)) reg write 1 4 0 4 5F83F827
> \!(Delay(3000)) reg write 2 4 0 4 6283F827
* Данные строчки необходимо отправить через терминал на контроллер радиоканала НГУ 1 апреля 2021 года в 13:13:00 (учитывая общие задержки необходимо это сделать приблизительно за 2 секунды).


# Проблемы и ошибки
В случае проблем, предложений и вопросов прошу создавать тему через github-овские [issues](https://github.com/a-styuf/oai_kpa_stm/issues)
и обращаться ко мне через whatsapp и почту  