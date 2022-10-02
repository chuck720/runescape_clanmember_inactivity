
'''
uses the generated Json files and takes the difference in Xp from current and previous data, then prints out a list
of clan members who didn't gain a certian amount of Xp, as well as a list of people inactive for longer than 6 mo.
it also generates a Json file of in-depth data if you want to dive deeper.
'''

import json

previous_data = 'The+AFKers_2022-09-30'
current_data = 'The+AFKers_2022-10-01.json'
inactive_xp_threshold = 0

# loading data

with open(previous_data, 'r') as f:
    first_data_loaded = f.read()
    previous_data = json.loads(first_data_loaded)

with open(current_data, 'r') as f:
    second_data_loaded = f.read()
    current_data = json.loads(second_data_loaded)

# cleaning up the data and creating the long inactive list

long_inactive = []

i = 0
while i < len(previous_data['players']):
    if previous_data['players'][i]['player_expirience'] == None:
        del previous_data['players'][i]
        i = 0
    else:
        i += 1

i = 0
while i < len(current_data['players']):
    if current_data['players'][i]['player_expirience'] == None:
        long_inactive.append(current_data['players'][i]['player_name'])
        del current_data['players'][i]
        i = 0
    else:
        i += 1

# taking the difference

delta = []
new_players = []

for member in current_data['players']:

    name = member['player_name']
    current_expirience = member['player_expirience']
    current_total = int(member['player_total_lvl'])

    for member in previous_data['players']:

        if member['player_name'] == name:
            delta_expirience = int(current_expirience) - int(member['player_expirience'])
            line = {'player_name': name, 'delta_expirience': delta_expirience, 'current_expirience': current_expirience, 'total_lvl': current_total}
            delta.append(line)

# finding inactives

inactive_data = []
inactive_members = []

for member in delta:
    if member['delta_expirience'] <= inactive_xp_threshold:
        inactive_data.append(member)
        inactive_members.append(member['player_name'])

# present data

with open('inactive_data.json', 'w') as f:
    f.write(json.dumps(inactive_data, indent=2))

print('\n{} members did not reach the goal of {} Xp\n'.format(len(inactive_members), inactive_xp_threshold))
for username in inactive_members:
    print(username)

print('\n{} members have been inactive longer than 6 months\n'.format(len(long_inactive)))
for username in long_inactive:
    print(username)

