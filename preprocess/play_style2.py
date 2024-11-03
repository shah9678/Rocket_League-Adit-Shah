import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
json_dir = "Data"  
BALL_CONTROL_THRESHOLD = 0.5  # Adjust this threshold as per requirements
BOOST_USAGE_THRESHOLD = 25
palette = {"Aggressive": "red", "Defensive": "blue", "Hybrid": "green"}

def preprocess_game_data(data):
    frames = data.get('rounds', {}).get('0', {}).get('clock', [])
    ball_control = data.get('rounds', {}).get('0', {}).get('ball_control', [])
    boost_usage = data.get('rounds', {}).get('0', {}).get('boost_value', [])
    
    max_length = max(len(frames), len(ball_control), len(boost_usage))
    
    def adjust_length(lst, fill_value):
        return lst + [fill_value] * (max_length - len(lst)) if len(lst) < max_length else lst
    
    frames = adjust_length(frames, [0, '0:00'])
    ball_control = adjust_length(ball_control, [0, False])
    boost_usage = adjust_length(boost_usage, [0, 0])
    
    df = pd.DataFrame({
        'frame': [f[0] for f in frames],
        'ball_control': [bc[1] for bc in ball_control],
        'boost_value': [b[1] for b in boost_usage]
    })
    return df

feature_datasets = []

for filename in os.listdir(json_dir):
    if filename.endswith(".json"):
        filepath = os.path.join(json_dir, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
            processed_data = preprocess_game_data(data)
            print(f"Processed Data for {filename}:", processed_data.head())
            
            features = {
                'avg_ball_control': np.mean(processed_data['ball_control']),
                'avg_boost_usage': np.mean(processed_data['boost_value']),
                'file_name': filename
            }
            
            # Determine play style based on ball control and boost usage thresholds
            if features['avg_ball_control'] > BALL_CONTROL_THRESHOLD and features['avg_boost_usage'] > BOOST_USAGE_THRESHOLD:
                features['play_style'] = 'Aggressive'
            elif features['avg_ball_control'] < BALL_CONTROL_THRESHOLD and features['avg_boost_usage'] < BOOST_USAGE_THRESHOLD:
                features['play_style'] = 'Defensive'
            else:
                features['play_style'] = 'Hybrid'
            
            feature_datasets.append(features)

final_dataset = pd.DataFrame(feature_datasets)
print("Final Dataset with Play Styles and Encoded Labels:", final_dataset.head())

plt.figure(figsize=(14, 8))

sns.scatterplot(
    x=final_dataset['file_name'],
    y=final_dataset['avg_ball_control'],
    hue=final_dataset['play_style'],
    palette=palette,
    s=100 
)

sns.scatterplot(
    x=final_dataset['file_name'],
    y=final_dataset['avg_boost_usage'],
    hue=final_dataset['play_style'],
    palette=palette,
    s=100,
    marker='^'  
)

plt.axhline(BALL_CONTROL_THRESHOLD, color="orange", linestyle="--", label="Ball Control Threshold")
plt.axhline(BOOST_USAGE_THRESHOLD, color="brown", linestyle="--", label="Boost Usage Threshold")

plt.xlabel("Match ID (JSON Filename)")
plt.ylabel("Metric Values")
plt.title("Play Style Categorization Based on Ball Control and Boost Usage")
plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1))  

plt.xticks(rotation=90)
plt.tight_layout()  
plt.show()
