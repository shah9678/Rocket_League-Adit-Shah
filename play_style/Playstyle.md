# Rocket League Playstyle Detection

This project analyzes Rocket League match data to extract features and detect player playstyles (Aggressive, Defensive, and Hybrid) based on gameplay metrics. Additionally, the project includes a focused analysis of the `ball_control` feature to explore its influence across different ranks.

## Features

- **Feature Extraction:** Extracts relevant gameplay metrics from Rocket League match data.
- **Threshold Setup:** Defines thresholds for gameplay metrics to differentiate between playstyles.
- **Playstyle Detection:** Categorizes players into:
  - **Aggressive:** High engagement in offensive maneuvers.
  - **Defensive:** Prioritizes saving goals and maintaining defensive positioning.
  - **Hybrid:** Balances offensive and defensive strategies.
- **Rank-Based Analysis:** Adapts the detection logic to specific player ranks.
- **Ball Control Analysis:** Isolates and evaluates the `ball_control` feature to observe its variation and impact across ranks.
![Screenshot 2024-11-21 at 5 56 26 PM](https://github.com/user-attachments/assets/372aaccd-953e-4fcf-b518-74bed623022e)

## Workflow

1. **Data Loading:**
   - Rocket League match data is loaded and preprocessed.
2. **Feature Engineering:**
   - Extracted features include metrics like possession time, goal attempts, saves, and ball control percentage.
3. **Thresholds Definition:**
   - Thresholds are determined for each metric based on rank-specific patterns.
4. **Playstyle Classification:**
   - Players are classified as Aggressive, Defensive, or Hybrid based on the extracted features and thresholds.
5. **Ball Control Focus:**
   - A separate analysis highlights how ball control behavior differs across ranks.
