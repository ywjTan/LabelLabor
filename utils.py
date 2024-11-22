import os
import json
import shutil


def get_file():
    existed_files = os.listdir('./data/')
    sorted(existed_files, key=lambda x: len(x))
    file_name = existed_files[0]
    tmp_file = 'tmp_' + file_name
    file_path = './data/' + file_name
    tmp_path = './data/' + tmp_file
    if not os.path.exists(tmp_path):
        shutil.copy(file_path, tmp_path)
    return tmp_path


def load_data(file):
    data = json.load(open(file, 'r', encoding='utf-8'))
    cur_id = 0
    if 'cur_id' in data[-1].keys():
        cur_id = data[-1]['cur_id']
    else:
        for i in range(len(data) - 1):
            if len(data[len(data) - 1 - i]['Private_Entities']) != 0:
                cur_id = len(data) - i
                break
        data.append({'cur_id': cur_id})
    json.dump(data, open(file, 'w', encoding='utf'), ensure_ascii=False, indent=4)
    return data, cur_id


def produce_shown_words(selected_words):
    s = ''
    for word in selected_words:
        s += word + '\n'
    return s


def write_tmp_file(data):
    file = get_file()
    json.dump(data, open(file, 'w', encoding='utf'), ensure_ascii=False, indent=4)

