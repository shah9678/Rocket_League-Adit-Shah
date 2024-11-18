This project utilizes reinforcement learning, specifically a Deep Q Network (DQN), to predict the likelihood of winning Rocket League matches on a per-chunk basis. The gameplay is divided into time-based chunks, and the model provides actionable feedback to improve performance in each chunk.

## Features Used for Training
The model uses the following features from gameplay data to predict match outcomes:

Average Ball Control (avg_ball_control): Player control over the ball.
Average Boost Usage (avg_boost_usage): Efficiency in using boost.
Shots on Goal (shots_on_goal): Goal attempts.
Saves (saves): Defensive actions preventing goals.
![image](https://github.com/user-attachments/assets/dc3fe6e1-7af7-4a5e-baa5-3e56f68f4165)

![image](https://github.com/user-attachments/assets/4487a843-86cd-4d33-8210-7410aaf65bac)


## Workflow
1. Chunking Gameplay Data
The entire gameplay video is divided into millisecond-based chunks.
Each chunk is analyzed independently for its feature distribution.
2. Deep Q Network (DQN) Training
The model is trained using DQN, a reinforcement learning technique, to predict the win likelihood for each chunk.
States are defined by feature distributions, and actions involve improving specific gameplay metrics.
3. Win Likelihood Prediction
The model predicts the likelihood of winning for each chunk.
Predictions help assess how a team is performing in real-time.
4. Performance Insights
The system provides actionable feedback for each chunk.
Example: "In this chunk, increase ball control by 10% to improve your win likelihood."

## Model Evaluation
Reward Function: Encourages behaviors that increase the probability of winning.
Performance Metrics: Accuracy and chunk-level feedback are evaluated to ensure actionable insights.
## How to Use
Preprocess Gameplay Data:
Split the gameplay into time-based chunks.
Extract features for each chunk.
Train the DQN:
Use the provided training script to fit the model.
Run Predictions:
Predict win likelihood per chunk and receive performance insights.
Interpret Results:
Apply the feedback to improve gameplay for specific chunks.
