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
    frames = data.get('rounds', {}).get('0', {}).get('clock', [])
    ball_control = data.get('rounds', {}).get('0', {}).get('ball_control', [])
    boost_usage = data.get('rounds', {}).get('0', {}).get('boost_value', [])
    shots_on_goal = data.get('rounds', {}).get('0', {}).get('shots_on_goal', [])
    saves = data.get('rounds', {}).get('0', {}).get('saves', [])
    
    max_length = max(len(frames), len(ball_control), len(boost_usage), len(shots_on_goal), len(saves))
    
    def adjust_length(lst, fill_value):
        return lst + [fill_value] * (max_length - len(lst)) if len(lst) < max_length else lst
    
    frames = adjust_length(frames, [0, '0:00'])
    ball_control = adjust_length(ball_control, [0, False])
    boost_usage = adjust_length(boost_usage, [0, 0])
    shots_on_goal = adjust_length(shots_on_goal, [0, False])
    saves = adjust_length(saves, [0, False])
    df = pd.DataFrame({
        'frame': [f[0] for f in frames],
        'ball_control': [bc[1] for bc in ball_control],
        'boost_value': [b[1] for b in boost_usage],
        'shots_on_goal': [s[1] for s in shots_on_goal],
        'saves': [s[1] for s in saves]
    })
    return df
feature_datasets = []


for filename in os.listdir(json_dir):
    if filename.endswith(".json"):
        filepath = os.path.join(json_dir, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
            # Process individual JSON data
            processed_data = preprocess_game_data(data)
            print(f"Processed Data for {filename}:", processed_data.head())
            
            features = {
                'avg_ball_control': np.mean(processed_data['ball_control']),
                'avg_boost_usage': np.mean(processed_data['boost_value']),
                'shots_on_goal': processed_data['shots_on_goal'].sum(),
                'saves': processed_data['saves'].sum(),
                'file_name': filename
            }
            if features['shots_on_goal'] > SHOTS_THRESHOLD and features['avg_boost_usage'] > BOOST_USAGE_THRESHOLD:
                features['play_style'] = 'Aggressive'
            elif features['saves'] > SAVES_THRESHOLD and features['avg_boost_usage'] < BOOST_USAGE_THRESHOLD:
                features['play_style'] = 'Defensive'
            else:
                features['play_style'] = 'Hybrid'
            
            feature_datasets.append(features)
final_dataset = pd.DataFrame(feature_datasets)
print("Final Dataset with Play Styles and Encoded Labels:", final_dataset.head())
plt.figure(figsize=(14, 8))
sns.scatterplot(
    x=final_dataset['file_name'],
    y=final_dataset['shots_on_goal'],
    hue=final_dataset['play_style'],
    palette=palette,
    s=100 
)

sns.scatterplot(
    x=final_dataset['file_name'],
    y=final_dataset['saves'],
    hue=final_dataset['play_style'],
    palette=palette,
    s=100,
    marker='s'  
)

sns.scatterplot(
    x=final_dataset['file_name'],
    y=final_dataset['avg_boost_usage'],
    hue=final_dataset['play_style'],
    palette=palette,
    s=100,
    marker='^'  
)
plt.axhline(SHOTS_THRESHOLD, color="orange", linestyle="--", label="Shots Threshold")
plt.axhline(SAVES_THRESHOLD, color="purple", linestyle="--", label="Saves Threshold")
plt.axhline(BOOST_USAGE_THRESHOLD, color="brown", linestyle="--", label="Boost Usage Threshold")

plt.xlabel("Match ID (JSON Filename)")
plt.ylabel("Metric Values")
plt.title("Play Style Categorization Based on Thresholds for Each Match")
plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1))  

plt.xticks(rotation=90)
plt.tight_layout()  
plt.show()

