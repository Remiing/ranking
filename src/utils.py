from datetime import datetime, timezone, timedelta
import yaml
import pandas as pd
import os
import math


def read_data():
    with open('./_data/guild_members.yml', encoding='utf-8') as file:
        members = yaml.load(file, Loader=yaml.FullLoader)
        members = members['main_character'] + members['sub_character']
    return members


def load_yaml(path):
    with open(path, encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data


def update_log(filename):
    KST = timezone(timedelta(hours=9))
    update_time = datetime.now(KST).strftime('%y-%m-%d %H:%M:%S')
    log = {
        'filename': filename,
        'update_time': update_time
    }
    return [log]


def range_union_increase(folder_path, date_range=7):
    df_union = pd.DataFrame()
    file_list = os.listdir(folder_path)
    sorted_file_list = sorted(file_list)
    selected_files = sorted_file_list[-date_range:]
    for file_name in selected_files:
        date = file_name.replace('.csv', '')
        data_frame = pd.read_csv(folder_path + file_name)
        union_dict = data_frame.set_index('nickname')['union'].to_dict()
        new_df = pd.DataFrame(data=union_dict, index=[date])
        df_union = pd.concat([df_union, new_df])

    return df_union


def range_level_increase(folder_path, exp_path, date_range=7):
    exp_max = load_yaml(exp_path)
    df_level = pd.DataFrame()
    file_list = os.listdir(folder_path)
    sorted_file_list = sorted(file_list)
    selected_files = sorted_file_list[-date_range:]
    for file_name in selected_files:
        date = file_name.replace('.csv', '')
        data_frame = pd.read_csv(folder_path + file_name)
        level_dict = {row['nickname']: (row['level'], row['experience']) for _, row in data_frame.iterrows()}
        for key, value in level_dict.items():
            level_dict[key] = value[0] + math.floor(value[1] / exp_max[value[0]] * 100) / 100
        new_df = pd.DataFrame(data=level_dict, index=[date])
        df_level = pd.concat([df_level, new_df])

    return df_level


