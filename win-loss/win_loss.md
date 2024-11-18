This trains a machine learning model to predict the outcome of Rocket League matches based on player performance metrics. The model uses historical match data to learn patterns and predict whether a team will win or lose.

## Features Used for Prediction
The model leverages the following features from the dataset to predict the match outcome:

![image](https://github.com/user-attachments/assets/b892c4a7-355a-43e8-af02-528a08453d73)



Average Ball Control (avg_ball_control): Measures how well players control the ball during the game.
Average Boost Usage (avg_boost_usage): Tracks how efficiently players use their boost resources.
Shots on Goal (shots_on_goal): Counts the number of attempts to score goals.
Saves (saves): Indicates how many times players prevent the opposing team from scoring.

## Target Variable
Win Condition (win_condition): A binary label indicating the outcome of the match:
1: Win
0: Loss

## Model Training Process
## Data Preparation:

The dataset is split into features (X) and target (y).
The data is further split into training (80%) and testing (20%) sets.
Model Training:

A machine learning model (e.g., LSTM ) is trained on the training set.
The model learns to predict the win_condition based on the input features.
Evaluation:

The model's performance is evaluated using metrics such as accuracy, precision, and recall on the test set.

## How to Use
Preprocessing: Ensure your dataset contains the required features and target.
Training: Run the training script to fit the model to your data.
Prediction: Use the trained model to predict match outcomes for new data.

