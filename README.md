# Deep Learning for Strategic Play Style Categorization in Rocket League


Rocket League Play Style Analysis: Insights and Feature Importance Using Deep Learning
This repository documents the development efforts focused on analyzing Rocket League gameplay data using deep learning and data analysis techniques.

# Motivation and Research Questions
The motivation behind this project is to explore and understand the strategic elements of Rocket League gameplay. In the Rocket League community, certain playstyles, car selections, and strategies are often considered optimal or "meta" for competitive success. However, much of this knowledge is anecdotal, with limited data-driven analysis available to substantiate these claims.

The goal of this project is to investigate these claims by formulating them into research questions and applying deep learning and data analysis to find answers. The main questions considered in this analysis are:

# What key factors contribute to winning a match in Rocket League?
Are there specific cars or team compositions that consistently lead to better match outcomes?
How does gameplay strategy shift between offensive and defensive phases?
Can we classify Rocket League players into distinct play styles based solely on gameplay data?
Do different car types (e.g., Octane, Dominus, Fennec) correspond to different strategies and gameplay mechanics?
Are there other roles or styles that better describe how players actually play the game?
These questions are further elaborated in the play_style and strategy sections of this repository.

# About the Data
The data used for this project is provided by Omnic Data, an AI-driven e-sports coaching platform that collects gameplay data from uploaded Rocket League matches. The dataset includes tens of thousands of matches from high-level competitive play, ensuring that the data is both rich and relevant for deep analysis. Each match is recorded as a time-series, with events and player actions captured at precise timestamps.

# Repository Overview
This repository is organized into several sections:

play_style: This section deals with the analysis of player behaviors, focusing on identifying different play styles using deep learning models.
strategy: This section investigates the factors that contribute to successful match outcomes, including car selection, positioning, and in-game decisions.
In addition, the preprocess directory details the extensive data preparation process, including parsing, cleaning, and feature engineering.

# Main Results
What Factors Contribute to Winning in Rocket League?
During the exploratory data analysis (EDA), it became clear that no single car or team composition was consistently linked to better outcomes. This suggests that winning in Rocket League is more about strategy and execution than simply choosing the "best" car or configuration.

Using both Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs) with Long Short-Term Memory (LSTM) layers, I attempted to classify matches into wins and losses. The models' performance was evaluated using metrics such as accuracy and F1 score, which ranged from 88% to 94% depending on the specific focus (e.g., offense vs. defense).

Key insights from the feature importance analysis indicated that boost management, positioning, and decision-making during critical moments were the most influential factors in determining match outcomes. These findings highlight the importance of maintaining optimal boost levels and making strategic positioning decisions.

Is It Possible to Classify Rocket League Players Into Distinct Play Styles?
For this question, I utilized a deep learning model with CNN and LSTM layers to classify players into different play styles based on gameplay data. Initial results were promising, with accuracy exceeding 90%. However, when filtering out factors like player choice (e.g., car type), the model's accuracy dropped to 80%. This suggests that while player choices do influence play style, gameplay data alone is still a strong indicator of a player’s preferred strategy.

# Challenges and Limitations
Limited Data Perspective
The data used for this project focuses on high-level players, which might introduce bias and limit the generalizability of the findings. Additionally, the dataset lacks team-based interaction data, which could provide deeper insights into cooperative play dynamics.

# Sparse Data
The combination of categorical and numerical features resulted in some sparsity in the data after preprocessing. This sparsity could have impacted the performance of certain models, particularly in unsupervised learning scenarios.

# Future Work
Team-Based Analysis: Future work could involve incorporating team-based data to better understand cooperative strategies in Rocket League.
Unsupervised Learning: With additional data, it would be worthwhile to revisit unsupervised clustering methods to identify more granular play styles or roles within the game.
Event-Based Analysis: A deeper analysis focusing on critical in-game events (e.g., goals, saves, boost pickups) could provide further insights into what actions lead to success or failure in matches.
Acknowledgments
The data for this academic project was provided by Omnic Data, with additional support and guidance from Northeastern University, Roux Institute.
