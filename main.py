from datetime import datetime, timezone, timedelta
import yaml

from src.utils import load_yaml, update_log
from src import crawling


def run():
    guild_members = load_yaml('./_data/members.yml')

    df_members = crawling.gather_members(guild_members)

    path = './_data/chart/'
    KST = timezone(timedelta(days=-1, hours=9))
    date = datetime.now(KST).strftime('%y-%m-%d')
    filename = date + '.csv'
    df_members.to_csv(path + filename, index=False)
    log = update_log(filename)
    with open('./_data/update_time.yml', 'a') as file:
        yaml.dump(log, file, default_flow_style=False)


if __name__ == '__main__':
    run()

