
'''
uses the generated clan members list to search the HiScores for total lvl and current Xp
if a member has been inactive for a long time (aprox 6 mo) OR they have less than 12,000 total Xp
they don't show up on HiScores for these cases I set their Xp and total lvl to a Null value
'''

import os
import json
import requests
from rs3_api import Hiscores
from datetime import date
hiscore = Hiscores()


def get_highscore(clan_members, clan_name):

    member_data = {'players': []}
    member_index = 0
    member_length = len(clan_members)

    for member in clan_members:
        try:
            response = hiscore.get_index_lite('normal', member)
            player_name = response['name']
            player_expirience = response['skills']['overall']['experience']
            player_total_lvl = response['skills']['overall']['level']
            line = {'player_name': player_name, 'player_expirience': player_expirience,
                    'player_total_lvl': player_total_lvl}
            member_data['players'].append(line)
            member_index += 1
            print('{} out of {} loaded'.format(member_index, member_length))
        except:
            player_name = member
            player_expirience = None
            player_total_lvl = None
            line = {'player_name': player_name, 'player_expirience': player_expirience,
                    'player_total_lvl': player_total_lvl}
            member_data['players'].append(line)
            member_index += 1
            print('{} out of {} loaded'.format(member_index, member_length))

    with open(clan_name + '_' + str(date.today()) + '.json', 'w') as f:
        f.write(json.dumps(member_data, indent=2))

    print('')
    print('done!')

    return

if __name__ == "__main__":
    get_highscore()