import json


with open('Camelot_Warchest_20200331-185724.json') as f:
  tards = json.load(f)

initit = 0
for tard in tards['tards']['data']:
    print(tard)
    """pitard = tard[initit]
    if int(pitard['score']) < 3700:
        print('Leader: {} - Score: {} - Spies {}'.format(pitard['leader'], pitard['score'], pitard['spies']))
    initit = + 1"""