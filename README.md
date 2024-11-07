# Deep Learning for Strategic Play Style Categorization in Rocket League

## Rocket League Play Style Analysis: Insights and Feature Importance Using Deep Learning
This repository explores the use of deep learning to analyze and classify play styles in Rocket League, focusing on strategic insights and feature importance using convolutional and sequential modeling.

---

### Motivation and Research Questions
The aim of this project is to uncover and understand the strategic elements of Rocket League gameplay by employing a data-driven approach to assess the effectiveness of common play styles and strategies. Key questions addressed include:

- **What factors contribute to winning a match in Rocket League?**
- **Are certain car types or team compositions consistently linked to better outcomes?**
- **How do strategies shift between offensive and defensive play phases?**
- **Can distinct play styles be identified based solely on gameplay data?**
- **Do car types (e.g., Octane, Dominus, Fennec) correlate with specific play styles?**
- **Are there other roles or strategies that better describe players' behaviors?**

### About the Data
The data is sourced from Omnic Data, an esports coaching platform, providing a high-quality dataset from competitive Rocket League matches. Each match is represented as a time-series of events and player actions recorded at specific timestamps, capturing in-game actions like ball control, boost management, and team interactions, all essential for detailed analysis.

### Repository Overview
- **play_style**: Analyzes individual player behavior and categorizes play styles using a CNN-LSTM model.
- **strategy**: Investigates the factors associated with match outcomes, including car type, player positioning, and critical decision points.
- **preprocess**: Outlines data preparation steps, including parsing match logs, data cleaning, and feature engineering.

### Methodology

#### Data Collection and Preprocessing
The data preprocessing involves structuring raw match logs into a usable format for machine learning. Steps include:

1. **Feature Engineering**: Extracts critical features such as player and ball positions, boost levels, and match outcomes. Key features are normalized, with categorical variables (e.g., car choice) encoded to enhance model learning.
2. **Time-Series Structuring**: Organizes events into sequential data snapshots, creating 3D tensors for input into the CNN-LSTM model.

#### CNN-LSTM Model for Play Style Categorization and Outcome Prediction
A CNN-LSTM hybrid model captures both spatial and temporal aspects of gameplay. Key architectural elements include:

1. **Input Layer**: Accepts a 3D tensor representing time-series sequences of spatial and temporal features.
2. **Convolutional Layers**: Two 1D CNN layers extract spatial patterns from positions of players and the ball.
3. **LSTM Layer**: Models temporal dependencies between sequential game events.
4. **Fully Connected Layers**: Dense layers with ReLU activation combine spatial and temporal features.
5. **Output Layer**: Uses sigmoid activation for binary win/loss classification and softmax activation for categorizing play styles (aggressive, defensive, hybrid).

#### Reinforcement Learning (RL) Model for Real-Time Win Likelihood Prediction
The RL model dynamically calculates win probabilities based on the game state at specific time segments. Key components include:

- **State (S)**: Defined by metrics such as ball control, boost usage, and player positioning.
- **Action (A)**: Discrete actions predicted by the model, representing strategic choices like defensive positioning or boost control.
- **Reward (R)**: Rewards positive outcomes (e.g., successful defense) and penalizes actions that reduce win probability.
  
The RL model optimizes its policy to maximize win likelihood, updating Q-values iteratively to approximate optimal strategic decisions.

### Main Results

#### Factors Contributing to Winning in Rocket League
Feature analysis highlights that strategic decisions, especially around boost management, positioning, and critical moments, play a crucial role in match outcomes. Unlike popular belief, specific car types or team compositions alone do not significantly impact winning.

#### Classifying Rocket League Players into Distinct Play Styles
The CNN-LSTM model achieved >90% accuracy in classifying players' play styles. However, removing player choices, such as car selection, reduced the accuracy to 80%, indicating a link between car type and play style.

### Experimental Setup and Performance

- **Data Split**: 80% training, 20% testing, to ensure robust evaluation.
- **Optimizer**: Adam optimizer selected for efficient handling of sparse gradients.
- **Metrics**: Accuracy, Precision, Recall, and F1-score calculated to measure model performance.

### Evaluation Metrics

1. **Accuracy**: Overall accuracy for win/loss prediction was 89%, and for play style categorization, 91%.
2. **Precision & Recall**: Both precision and recall were high across play styles, indicating the model’s ability to correctly classify play styles and match outcomes.
3. **F1-Score**: F1-score for win/loss prediction was 0.87, and 0.90 for play style categorization, showcasing a strong balance between precision and recall.

#### Confusion Matrix and Error Analysis
The confusion matrix highlighted that the model occasionally misclassified hybrid play styles as either aggressive or defensive, which could be attributed to the context-dependent nature of hybrid strategies.

### Visualization of Results
Graphs and scatter plots illustrate key metrics (e.g., ball possession, boost usage) across play styles and competitive ranks. The analysis shows that aggressive play styles are more common at higher ranks, while defensive play is more prevalent at lower ranks.

---

### Discussion and Implications

#### Implications for Esports
The CNN-LSTM model's predictive accuracy for play styles and match outcomes has significant implications for esports, enabling teams to make data-driven decisions. RL-based real-time win likelihood predictions could eventually be integrated into in-game feedback systems.

#### Broader Applications Beyond Rocket League
The methodologies here can be extended to other competitive games (e.g., FIFA, Dota 2) and traditional sports (e.g., soccer, basketball) that depend on spatial and temporal dynamics.

### Challenges and Limitations
- **Latency in Real-Time Analysis**: Real-time prediction would require optimized data pipelines for rapid processing.
- **Broad Play Style Categories**: Expanding categories beyond aggressive, defensive, and hybrid could capture more nuanced play behaviors.

### Future Work
1. **Team-Based Analysis**: Incorporating team dynamics to understand cooperative strategies.
2. **Unsupervised Learning**: Applying clustering methods to detect granular play styles within broader categories.
3. **Real-Time Optimization**: Streamlining RL models for in-match applications, providing real-time strategic feedback.

---

### Acknowledgments
This project is supported by data from Omnic Data. Special thanks to these organizations for facilitating the research.

---
