import sys
import os


def check_sys_argv():
    if 1 >= len(sys.argv):
        print("Needs one command line argument")
        exit(1)


def compose_command_line_string(arg_str: str) -> str:
    str_parts = arg_str.split('/')
    command_line_str = ' '.join(['git clone', arg_str, str_parts[-2] + '_' + str_parts[-1]])
    return command_line_str


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_sys_argv()
    my_cl_string = compose_command_line_string(sys.argv[1])
    os.system(my_cl_string)
