import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
json_dir = "Data"
SHOTS_THRESHOLD = 2
SAVES_THRESHOLD = 3
BOOST_USAGE_THRESHOLD = 20
palette = {"Aggressive": "red", "Defensive": "blue", "Hybrid": "green"}

def preprocess_game_data(data):
    frame_data = data.get('rounds', {}).get('0', {}).get('clock', [])
    ball_control_data = data.get('rounds', {}).get('0', {}).get('ball_control', [])
    boost_usage_data = data.get('rounds', {}).get('0', {}).get('boost_value', [])
    shots_on_goal_data = data.get('rounds', {}).get('0', {}).get('shots_on_goal', [])
    saves_data = data.get('rounds', {}).get('0', {}).get('saves', [])

    max_length = max(len(frame_data), len(ball_control_data), len(boost_usage_data), len(shots_on_goal_data), len(saves_data))

    def adjust_length(lst, fill_value):
        return lst + [fill_value] * (max_length - len(lst)) if len(lst) < max_length else lst

    frame_data = adjust_length(frame_data, [0, '0:00'])
    ball_control_data = adjust_length(ball_control_data, [0, False])
    boost_usage_data = adjust_length(boost_usage_data, [0, 0])
    shots_on_goal_data = adjust_length(shots_on_goal_data, [0, False])
    saves_data = adjust_length(saves_data, [0, False])

    df = pd.DataFrame({
        'frame': [f[0] for f in frame_data],
        'ball_control': [bc[1] for bc in ball_control_data],
        'boost_value': [b[1] for b in boost_usage_data],
        'shots_on_goal': [s[1] for s in shots_on_goal_data],
        'saves': [s[1] for s in saves_data]
    })

    features = {
        'avg_ball_control': np.mean(df['ball_control']),
        'avg_boost_usage': np.mean(df['boost_value']),
        'shots_on_goal': df['shots_on_goal'].sum(),
        'saves': df['saves'].sum(),
        'file_name': filename
    }

    if features['shots_on_goal'] > SHOTS_THRESHOLD and features['avg_boost_usage'] > BOOST_USAGE_THRESHOLD:
        features['play_style'] = 'Aggressive'
    elif features['saves'] > SAVES_THRESHOLD and features['avg_boost_usage'] < BOOST_USAGE_THRESHOLD:
        features['play_style'] = 'Defensive'
    else:
        features['play_style'] = 'Hybrid'

    return features

feature_datasets = []

for filename in os.listdir(json_dir):
    if filename.endswith(".json"):
        filepath = os.path.join(json_dir, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
            data=data.get('statistics',[None])[0]
            if data is None:
                continue
            features = preprocess_game_data(data)
            feature_datasets.append(features)

final_dataset = pd.DataFrame(feature_datasets)
