'''
uses the generated clan members list to search the HiScores for total lvl and current Xp
if a member has been inactive for a long time (aprox 6 mo) OR they have less than 12,000 total Xp
they don't show up on HiScores for these cases I set their Xp and total lvl to a Null value
'''

import json
import requests
from rs3_api import Hiscores
hiscore = Hiscores()

clan_name = 'The+AFKers'

with open('The+AFKers_members.json', 'r') as f:
    clan_members = json.loads(f.read())

member_data = {'players': []}

for member in clan_members['members']:
    try:
        response = hiscore.get_index_lite('normal', member)
        player_name = response['name']
        player_expirience = response['skills']['overall']['experience']
        player_total_lvl = response['skills']['overall']['level']
        line = {'player_name': player_name, 'player_expirience': player_expirience,
                'player_total_lvl': player_total_lvl}
        member_data['players'].append(line)
        print(player_name)
    except:
        player_name = member
        player_expirience = None
        player_total_lvl = None
        line = {'player_name': player_name, 'player_expirience': player_expirience,
                'player_total_lvl': player_total_lvl}
        member_data['players'].append(line)
        print(player_name)

f = open(clan_name + '_procesed_data.json', 'w')
f.write(json.dumps(member_data, indent=2))
f.close()
