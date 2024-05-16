from nba_api.live.nba.endpoints import scoreboard
from nba_api.live.nba.endpoints import playbyplay
from nba_api.stats.static import players
import gpt_processing
import json
import time

GAME_ID = '0042300224'
line = "{action_number}: {period}:{clock} {player_id} ({action_type})"

def process_stats(stats):
    return stats["description"]

mx = -1
live = True
while(live):
    pbp = playbyplay.PlayByPlay(GAME_ID)
    actions = pbp.get_dict()['game']['actions'] 
    for action in actions[:2]:
        if(action["actionNumber"] <= mx):
            continue
        mx = action["actionNumber"]
        stats_str = process_stats(action)
        comm = gpt_processing.commentate(stats_str)
        print(comm)
        if(action["actionType"]=='game'):
            live = False
        time.sleep(5)

print("done")
        