from datetime import datetime, timezone, timedelta
import yaml


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



