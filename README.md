# SBSPS-Challenge-5230-Super-Predictor-of-Indian-Premier-League-IPL-
## We did Exploratory Analysis on Indian Premier League Dataset, and extracted the important features from it.
## It was made in Jupyter Notebook and also separately as Python Script. The files are in
📦source \
 ┣ 📜IPL_objectives.ipynb \
 ┗ 📜IPL_objectives.py
### Before running script make sure that all modules are installed. Use either jupyter notebook or directly run it as python file.
# Here the objective are explained.
## 1) To find the team that won the most number of matches in the entire IPL
`
most_no_of_wins = df.groupby('winner').apply(lambda x: x).reset_index() 
most_no_of_wins = most_no_of_wins.groupby('winner').count()
most_no_of_wins = most_no_of_wins.city.reset_index(name='No_Of_Wins')
most_no_of_wins = most_no_of_wins.sort_values(by='No_Of_Wins',ascending=False)
`
## The most wins are founded by grouping winner teams and counting the number of matches they won and sorting them and finnally plotting it in graph.

## All the Extracted features and data are saved in output directory

