import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':0, 'nation':1, 'league':2,'team':0, 'goals_selection':1, 'selections_nation':2,'end_contract':1, 'league':2
'goal_champ':0, 'assist_champ':1, 'own_goal_champ':2,'penalty_goal_champ':0, 
'goal_cup':0, 'assist_cup':1, 'own_goal_cup':2,'penalty_goal_cup':0,
'goal_continent':0, 'assist_continent':1, 'own_goal_continent':2,'penalty_goal_continent':0,
'AttackingMidfield':0, 'CentralMidfield':1, 'DefensiveMidfield':2,'LeftMidfield':0,
'LeftWinger':0, 'RightMidfield':1, 'RightWinger':2,'SecondStriker':0,'yellows_cards':2,'red_cards':0}

print(r.json())