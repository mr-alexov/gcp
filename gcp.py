import sys
import os
from typing import List


def check_sys_argv():
    if 1 >= len(sys.argv):
        print("Needs one command line argument")
        exit(1)


def prepare_and_split_string(repo_url_str: str) -> List[str]:
    # remove trailing '.git' substring
    pos = repo_url_str.rfind('.git')
    if pos > 0:
        repo_url_str = repo_url_str[:-4]

    # split and compose folder string from what is between '/' after 'github.com'
    return repo_url_str.split('/')


def folder_string(repo_url_str: str) -> str:
    str_parts = prepare_and_split_string(repo_url_str)
    github_index = str_parts.index("github.com")
    return_string = str_parts[github_index + 1] + '_' + str_parts[github_index + 2]
    return return_string


def repo_string(repo_url_str: str) -> str:
    str_parts = prepare_and_split_string(repo_url_str)
    slice_str_parts = str_parts[0:5]
    return '/'.join(slice_str_parts)


def compose_command_line_string(repo_url_str: str) -> str:
    command_line_str = ' '.join(['git clone', "", folder_string(repo_url_str)])
    return command_line_str


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_sys_argv()
    my_cl_string = compose_command_line_string(sys.argv[1])
    os.system(my_cl_string)
