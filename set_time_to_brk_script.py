from norby_console_test_file_generator import *
import sys

try:
    os.mkdir("time scripts")
except OSError as error:
    print(error)

file_name = "brk_set_time_script"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        desired_time = sys.argv[1]
        print(desired_time)
        with open("time scripts/" + file_name + "_" + desired_time + ".txt", "w") as test_file:
            file_write(test_file, brk_set_time(desired_time=desired_time))
    else:
        print("Time argument <%Y_%m_%d %H-%M-%S> is missing")
