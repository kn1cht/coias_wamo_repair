import time
from wamo_repair_util import *

user_input = input('directory to search OLD send_mpc.txt (required): ')
if user_input:
    old_sendmpc_directory = user_input
else:
    print('Please specify directory name !!!')

user_input = input('directory to save NEW send_mpc.txt (option): ')
if user_input:
    new_sendmpc_directory = user_input
else:
    new_sendmpc_directory = 'new_' + old_sendmpc_directory

file_array = search_send_mpc(old_sendmpc_directory)

for fname in file_array:
    with open(fname, "r") as file:
        old_txt = file.read()
    result = post_request(old_txt)
    print_log(fname, old_txt, result)
    create_new_file(fname, result["new_send_mpc"],
                    old_sendmpc_directory, new_sendmpc_directory)
    time.sleep(0.25)
