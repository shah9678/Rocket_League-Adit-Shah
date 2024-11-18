# Deep Learning for Strategic Play Style Categorization in Rocket League

## Rocket League Play Style Analysis: Insights and Feature Importance Using Deep Learning

This repository leverages deep learning to analyze and classify Rocket League play styles. Using convolutional and sequential models, it provides actionable feedback to help players enhance their performance and optimize their strategies.

---

## Motivation and Research Questions

This project explores the strategic elements of Rocket League through a data-driven approach. Key research questions include:

- **What factors influence match outcomes in Rocket League?**
- **How do car types (e.g., Octane, Dominus, Fennec) impact play styles?**
- **How do offensive and defensive strategies evolve over time?**
- **Can distinct play styles be identified from gameplay data?**
- **What feedback can players adopt to improve performance in specific gameplay chunks?**

---

## About the Data

The dataset is sourced from Omnic Data, an esports coaching platform, featuring competitive Rocket League match data. Each match is represented as a time-series of events and player actions, including key gameplay metrics like:

- **Ball Control**
- **Boost Management**
- **Shots on Goal**
- **Saves**

---

## Repository Overview

- **`play_style`**: Analyzes individual player behavior and classifies play styles using a CNN-LSTM model.
- **`strategy`**: Investigates factors contributing to match outcomes, including car types and positioning.
- **`preprocess`**: Prepares and cleans data, including feature engineering and time-series structuring.

---

## Methodology

### 1. Data Collection and Preprocessing
- **Feature Engineering**: Extracts key features (player positions, boost usage, etc.).
- **Time-Series Structuring**: Organizes gameplay events into sequential data snapshots, creating 3D tensors for CNN-LSTM input.

### 2. CNN-LSTM Model for Play Style Categorization
A hybrid CNN-LSTM model captures spatial and temporal gameplay aspects:
- **Convolutional Layers**: Extract spatial patterns from player and ball positions.
- **LSTM Layer**: Models temporal dependencies across gameplay sequences.
- **Output Layer**: 
  - **Sigmoid** for binary win/loss prediction.
  - **Softmax** for play style categorization (aggressive, defensive, hybrid).

### 3. Reinforcement Learning (RL) for Real-Time Win Prediction
An RL model predicts win likelihood dynamically and provides actionable feedback:
- **State (S)**: Metrics such as ball control, boost usage, and positioning.
- **Action (A)**: Strategy adjustments, e.g., defensive positioning.
- **Reward (R)**: Positive for actions increasing win likelihood.

---

## Key Results

### Play Style Classification
- **>90% Accuracy** for play style classification.
- **80% Accuracy** when excluding player choices like car selection.

### Win Prediction
- **89% Accuracy** for win/loss prediction.
- **F1-Score**: 0.87 for win/loss, 0.90 for play style categorization.

### Insights
- Boost management and positioning are crucial for success.
- Specific car types correlate with certain play styles but are not sole determinants of winning.

---

## Visualization

- **Graphs**: Feature importance for win likelihood.
- **Pair Plots**: Play style distribution across ranks.
- **Liklihood Plots**: Win_liklihood distribution based on chunks per game. 

![image](https://github.com/user-attachments/assets/2f42e1eb-ea22-4fa9-b6ab-9e5c9d9a6bb9)

![image](https://github.com/user-attachments/assets/30ac0123-802d-4b25-b313-85cf472b13b1)

![image](https://github.com/user-attachments/assets/e8867ef1-adb9-4004-9664-7419510d8083)


---

## Evaluation Metrics
- **Accuracy**: 89% (win/loss), 91% (play style).
- **Precision & Recall**: High across play styles.
- **Confusion Matrix**: Highlights minor misclassifications in hybrid strategies.

---

## Examples

- **Chunk Analysis Feedback**:
  - *"In this chunk, increase ball control by 10% to boost win likelihood."*
  - *"Focus on defensive positioning during this phase."*

---

## Future Work
1. **Team-Based Analysis**: Incorporate team dynamics for cooperative strategies.
2. **Unsupervised Learning**: Use clustering to uncover granular play styles.
3. **Real-Time Optimization**: Streamline RL models for in-game feedback.

---

## Acknowledgments
Thanks to Omnic Data for providing high-quality Rocket League match data.

---

## How to Use

1. **Preprocess Gameplay Data**:
   ```python
   python preprocess.py
python train_play_style.py

python rl_win_prediction.py
