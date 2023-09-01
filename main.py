from datetime import datetime, timezone, timedelta
import yaml
from src import crawling, utils


def run():
    guild_members = utils.load_yaml('./_data/members.yml')

    df_members = crawling.gather_members(guild_members)

    path = './_data/chart/'
    KST = timezone(timedelta(days=-1, hours=9))
    date = datetime.now(KST).strftime('%y-%m-%d')
    filename = date + '.csv'
    df_members.to_csv(path + filename, index=False)
    log = utils.update_log(filename)
    with open('./_data/update_time.yml', 'a') as file:
        yaml.dump(log, file, default_flow_style=False)
    # df_union = utils.range_union_increase('./_data/chart/', 14)
    # df_union.to_csv('./_data/union_increase.csv')
    # df_level = utils.range_level_increase('./_data/chart/', './_data/experience.yml', 14)
    # df_level.to_csv('./_data/level_increase.csv')


if __name__ == '__main__':
    run()

