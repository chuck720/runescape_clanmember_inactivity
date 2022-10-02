
'''
scraper that pulls clan members usernames from clan HiScores page
use with caution, it is against jagex's TOS to automatically request HTTP
'''

import bs4
import requests
from bs4 import BeautifulSoup
import json

def get_members(clan_name):
    print('getting clan members...')
    page_number = 1
    max_pages = 10
    clannies = []
    url = 'https://secure.runescape.com/m=clan-hiscores/a=13/members.ws?clanName=' + clan_name + '&ranking=-1&pageSize=45&pageNum='
    while page_number < max_pages:
        html = requests.get(url + str(page_number)).content
        soup = bs4.BeautifulSoup(html, features="html.parser")
        for div in soup.find_all('div', class_='membersListRow'):
            name = div.find('span', class_='name').string.replace('\xa0', ' ')
            if name in clannies:
                page_number = max_pages
                break
            clannies.append(name)
        page_number += 1
    print('{} members found'.format(len(clannies)))
    print('')
    return clannies

if __name__ == "__main__":
    get_members()