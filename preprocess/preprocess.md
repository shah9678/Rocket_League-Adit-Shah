# Rocket League Gameplay Preprocessing and Feature Extraction

This repository contains a script for preprocessing Rocket League gameplay data and extracting key features for play style classification and strategic analysis.

---

## Overview

The script processes JSON files containing Rocket League match data, extracting essential gameplay metrics and calculating aggregate features. Based on these features, it categorizes play styles into **Aggressive**, **Defensive**, or **Hybrid**.

---

## Features Extracted

The script extracts and calculates the following features:

- **Average Ball Control (`avg_ball_control`)**: Measures how well players control the ball.
- **Average Boost Usage (`avg_boost_usage`)**: Tracks players' boost efficiency.
- **Shots on Goal (`shots_on_goal`)**: Total goal attempts in a match.
- **Saves (`saves`)**: Defensive actions preventing goals.
- **Play Style (`play_style`)**: Categorizes play styles based on thresholds for shots, saves, and boost usage:
  - **Aggressive**: High shots and boost usage.
  - **Defensive**: High saves and low boost usage.
  - **Hybrid**: Moderate levels of all metrics.

---

## Thresholds

The play style classification uses the following thresholds:

- **SHOTS_THRESHOLD**: 2 (Aggressive if exceeded).
- **SAVES_THRESHOLD**: 3 (Defensive if exceeded).
- **BOOST_USAGE_THRESHOLD**: 20 (Aggressive if exceeded, Defensive if not).

---

## Preprocessing Steps

1. **Load JSON Files**:  
   Reads all JSON files from the specified `Data` directory.

2. **Data Cleaning and Adjustment**:  
   - Extracts relevant fields (`clock`, `ball_control`, `boost_value`, `shots_on_goal`, `saves`).
   - Adjusts lengths to ensure consistent data structures.

3. **Feature Calculation**:  
   - Computes averages and sums for gameplay metrics.
   - Classifies the play style based on feature thresholds.

4. **Compile Dataset**:  
   - Stores the extracted features in a pandas DataFrame (`final_dataset`).

---
