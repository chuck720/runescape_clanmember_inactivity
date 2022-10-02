'''
combines multiple steps into one. outputs current Xp of all clan members to a json file
'''

import get_clan_members
import get_HiScore

clan_name = 'The AFKers'
clan_name = clan_name.replace(' ', '+')

members = get_clan_members.get_members(clan_name)

get_HiScore.get_highscore(members, clan_name)
