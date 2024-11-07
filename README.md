# Deep Learning for Strategic Play Style Categorization in Rocket League

## Rocket League Play Style Analysis: Insights and Feature Importance Using Deep Learning
This repository contains development efforts to analyze Rocket League gameplay data using deep learning and data analysis techniques.

---

### Motivation and Research Questions
The goal of this project is to explore and understand the strategic elements of Rocket League gameplay using data-driven methods to substantiate gameplay strategies often discussed in the Rocket League community. Key research questions addressed include:

- What factors contribute to winning a match in Rocket League?
- Are certain cars or team compositions consistently linked to better outcomes?
- How do gameplay strategies shift between offensive and defensive phases?
- Can we classify players into distinct play styles based on gameplay data?
- Do car types (e.g., Octane, Dominus, Fennec) correspond to unique strategies?
- Are there other roles or styles that better capture player behavior?

### About the Data
The dataset, sourced from Omnic Data, an AI-driven esports coaching platform, includes data from high-level competitive Rocket League matches. It consists of time-series data capturing player actions and events with precise timestamps, providing a rich basis for deep analysis.

### Repository Overview
- **play_style**: Analyzes player behavior to identify play styles using deep learning models.
- **strategy**: Investigates factors that contribute to successful match outcomes, including car choice, positioning, and decision-making.
- **preprocess**: Documents the data preparation process, including parsing, cleaning, and feature engineering.

### Methodology

#### Data Collection and Preprocessing
The raw data undergoes preprocessing to convert Rocket League match logs into sequences representing key features such as player and ball positions, boost levels, and outcomes, normalized and organized in a 3D tensor format suitable for deep learning.

#### CNN-LSTM Model for Play Style Categorization and Outcome Prediction
A CNN-LSTM hybrid model is used to classify player strategies into aggressive, defensive, or hybrid play styles and predict match outcomes based on spatial and temporal data. Convolutional layers capture spatial configurations, while LSTM layers model the sequential evolution of gameplay. 

#### Reinforcement Learning Model for Real-Time Win Likelihood Prediction
The RL model analyzes gameplay in discrete segments to predict win probabilities dynamically, learning from features like ball control, boost usage, and player positioning. This approach allows for real-time tactical adjustments.

### Main Results

#### What Factors Contribute to Winning in Rocket League?
- Winning in Rocket League appears to be more influenced by strategic decisions and execution rather than a particular car or team composition.
- Feature importance analysis highlighted that boost management, positioning, and critical decision-making significantly impact match outcomes.

#### Can We Classify Rocket League Players Into Distinct Play Styles?
- The CNN-LSTM model achieved >90% accuracy in classifying play styles, although removing player-specific choices like car type reduced accuracy to 80%, indicating a strong influence of player choices on play style.

### Experimental Results

- **Accuracy**: 89% for win/loss prediction and 91% for play style categorization.
- **Precision & Recall**: High precision and recall for both tasks, with F1-scores confirming model robustness.
- **Error Analysis**: Confusion matrices revealed occasional misclassification of hybrid play styles, highlighting the complexity of dynamic strategies.

### Visualization of Results
Figures illustrate the distribution of key metrics (ball possession, boost usage, etc.) across different play styles and player ranks, showcasing the evolution of strategies with experience and rank.

---

### Discussion and Implications

#### Implications for Esports
This study demonstrates how deep learning can enhance strategic understanding in Rocket League, allowing teams to make data-driven adjustments during and before matches. The RL model's real-time predictive capability opens possibilities for in-game tactical feedback, a valuable tool for high-stakes scenarios.

#### Broader Applications Beyond Rocket League
While designed for Rocket League, the framework is applicable to other esports (e.g., FIFA, Dota 2) and traditional sports (e.g., soccer, basketball), where spatial and temporal dynamics are key to strategy.

### Challenges and Limitations
- **Post-Match Data Dependency**: Real-time applications would require optimization for faster data processing.
- **Play Style Categorization**: Broad categories (aggressive, defensive, hybrid) may not capture nuanced behaviors, highlighting an area for further refinement.

### Future Work
- **Team-Based Analysis**: Adding team-level data could improve insights into cooperative strategies.
- **Granular Play Style Categories**: Developing finer distinctions within strategies could better capture dynamic shifts in play style.
- **Real-Time Processing Optimization**: Optimizing the RL framework for real-time feedback would allow immediate strategic adjustments.

---

### Acknowledgments
Data for this project was provided by Omnic Data, with additional support from Northeastern University, Roux Institute.
