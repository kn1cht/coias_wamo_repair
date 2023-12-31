import os
import re
import requests
import datetime
import urllib


def search_send_mpc(directory):
    print('gathering files...')
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt") and file.startswith("send_mpc"):
                file_list.append(os.path.join(root, file))
    print(f'found {len(file_list)}')
    return file_list

def post_request(send_mpc_txt):
    api_url = "https://web-coias.u-aizu.ac.jp/api/fix_send_mpc_2023nov"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    params = urllib.parse.urlencode({"send_mpc": send_mpc_txt})
    response = requests.post(api_url, data=params, headers=headers)
    result = response.json()["result"]
    return result

def create_new_file(file_path, send_mpc_txt, old_dir, new_dir):
    new_file_path = file_path.replace(old_dir, new_dir, 1)
    os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
    with open(new_file_path, "w") as new_file:
        new_file.write(send_mpc_txt)

def print_log(fname, old_txt, result):
    print(f"[{datetime.datetime.now()}] processing {fname}")

    header_count = len(re.findall(r"(?m)^([A-Z]{3}|[A-Z]\.|[A-Z]-[A-Z]\.) ", old_txt))
    old_lines = old_txt.splitlines(keepends=False)
    new_lines = result["new_send_mpc"].splitlines(keepends=False)
    changed_count = sum(
        1 for old_line, new_line
        in zip(old_lines, new_lines)
        if old_line != new_line
    )
    mpc80_count = len(new_lines) - header_count
    print(f"Number of changed lines: {changed_count} / {mpc80_count}")

    if len(result["not_mpc_80_lines"]):
        print(f"{len(result['not_mpc_80_lines'])} lines are not MPC 80 format!")
        print(result["not_mpc_80_lines"])
    if len(result["not_found_lines"]):
        print(f"{len(result['not_found_lines'])} lines are not found on database!")
        print(result["not_found_lines"])
