'''
uses the generated JSON data and finds all instances of Null Xp values
and prints their name out
'''
import json

clan_name = 'The+AFKers'

with open(clan_name + '_procesed_data.json', 'r') as f:
    data = f.read()
    data = json.loads(data)

long_inactive = []

for instance in data['players']:
    if instance['player_expirience'] == None:
        long_inactive.append(instance['player_name'])
        print(instance['player_name'])

print('\ntotal number of long inactives:', len(long_inactive))

