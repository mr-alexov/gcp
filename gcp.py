import sys
import os


def check_sys_argv():
    if 1 >= len(sys.argv):
        print("Needs one command line argument")
        exit(1)


def folder_string(repo_url_str: str) -> str:
    # remove trailing '.git' substring
    pos = repo_url_str.rfind('.git')
    if pos > 0:
        repo_url_str = repo_url_str[:-4]

    # split and compose folder string from what is between '/' after 'github.com'
    str_parts = repo_url_str.split('/')
    github_index = str_parts.index("github.com")
    return_string = str_parts[github_index + 1] + '_' + str_parts[github_index + 2]
    return return_string


def compose_command_line_string(repo_url_str: str) -> str:
    command_line_str = ' '.join(['git clone', repo_url_str, folder_string(repo_url_str)])
    return command_line_str


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_sys_argv()
    my_cl_string = compose_command_line_string(sys.argv[1])
    os.system(my_cl_string)
