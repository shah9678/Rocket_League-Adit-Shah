import json
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

# Define directory containing JSON files
json_dir = "Data"

# Preprocess JSON data (reusing your function)
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

# Collect data and extract features
feature_datasets = []
for filename in os.listdir(json_dir):
    if filename.endswith(".json"):
        filepath = os.path.join(json_dir, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
            processed_data = preprocess_game_data(data)
            # Calculate features
            features = {
                'avg_ball_control': np.mean(processed_data['ball_control']),
                'avg_boost_usage': np.mean(processed_data['boost_value']),
                'shots_on_goal': sum(processed_data['shots_on_goal']),
                'saves': sum(processed_data['saves']),
                'win_condition': data.get('win_condition', 0),  # Assume win_condition is 1 for win, 0 otherwise
                'file_name': filename
            }
            feature_datasets.append(features)

# Create a DataFrame with all features
final_dataset = pd.DataFrame(feature_datasets)
print("Final Dataset:", final_dataset.head())





#EDA -Feature Enginnerring 


import matplotlib.pyplot as plt
import seaborn as sns

# Plot distributions of each feature
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
sns.histplot(final_dataset['avg_ball_control'], kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Average Ball Control Distribution')

sns.histplot(final_dataset['avg_boost_usage'], kde=True, ax=axes[0, 1])
axes[0, 1].set_title('Average Boost Usage Distribution')

sns.histplot(final_dataset['shots_on_goal'], kde=True, ax=axes[1, 0])
axes[1, 0].set_title('Shots on Goal Distribution')

sns.histplot(final_dataset['saves'], kde=True, ax=axes[1, 1])
axes[1, 1].set_title('Saves Distribution')

plt.tight_layout()
plt.show()




# Correlation matrix heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(final_dataset.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Feature Correlation Matrix')
plt.show()





sns.pairplot(final_dataset, hue='win_condition', palette='Set2')
plt.suptitle('Pairplot of Features by Win Condition', y=1.02)
plt.show()

