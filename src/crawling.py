import requests
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


def get_characterInfo(name):
    streamerName, characterName = name
    url = f'https://maplestory.nexon.com/N23Ranking/World/Total?c={characterName}&w=0'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    profile = soup.select_one('.search_com_chk')

    if not profile:

        return

    className = profile.select_one('td > dl > dd').text
    level = profile.select_one('td:nth-child(3)').text.replace('Lv.', '')
    experience = profile.select_one('td:nth-child(4)').text.replace(',', '')
    popularity = profile.select_one('td:nth-child(5)').text.replace(',', '')
    image_url = profile.select_one('td > span > img:nth-child(1)')['src']
    urllib.request.urlretrieve(image_url, f'./assets/images/character/{characterName}.png')

    character_data = {
        'streamer': streamerName,
        'nickname': characterName,
        'class': className,
        'level': int(level),
        'experience': int(experience),
        'popularity': int(popularity),
        'image': image_url
    }

    return character_data


def gather_members(members):
    member_data_list = []
    for member in members.items():
        member_data = get_characterInfo(member)
        if member_data:
            member_data_list.append(member_data)
            print(f'{member_data["streamer"]:7} {member_data["nickname"]:7} {member_data["class"]:6} {member_data["level"]:3} {member_data["experience"]:12} {member_data["popularity"]:4} {member_data["image"]}')
            # print(member, 'complete')
        else:
            print(f'{member[0]:6} {member[1]:7} 캐럭터 정보가 없습니다')
            # print(member, 'fail')
    df_members = pd.DataFrame(data=member_data_list)
    df_members = df_members.sort_values(by=['level', 'experience'], ascending=[False, False])

    return df_members


if __name__ == '__main__':
    get_characterInfo('도적삼식')


