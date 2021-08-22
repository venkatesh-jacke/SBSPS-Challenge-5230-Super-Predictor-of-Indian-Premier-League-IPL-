# SBSPS-Challenge-5230-Super-Predictor-of-Indian-Premier-League-IPL-
## We did Exploratory Analysis on Indian Premier League Dataset, and extracted the important features from it.
## It was made in Jupyter Notebook and also separately as Python Script. The files are in








# Objective
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The objective of this solution is to create dashboard that visualizes following capabilities and also forecast the future results 
<div align="center">

1. To find the team that won the most number of matches in the entire IPL. 
2. To find the team that lost the most number of matches in the entire IPL. 
3. Does winning a toss increase the chances of victory. 
4. To find the player with the most player of the match awards. 
5. To find the city that hosted the maximum number of IPL matches. 
6. To find the most winning team for each season. 
7. To find the on-field umpire with the maximum number of IPL matches. 
8. To find the biggest victories in IPL while defending a total and while chasing a total. 
9. Which team won the most matches while batting first. 
10. Which team won the most matches while batting second. 
11. List of teams which have won matches by most runs cumulatively 
</div>
# Using this extracted data file, we created a dashboard 
<object data="workflow/dashboardP.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="Dashboard.pdf">
        <p>Click here to <a href="Dashboard.pdf">Download PDF</a>.</p>
    </embed>
</object>

## Proposed solution working flow
<div align="center">
<img src="https://www.researchgate.net/profile/Jayash-Sharma/publication/335572825/figure/fig1/AS:846755302215682@1578893604900/Block-Diagram-for-Proposed-Model.ppm" alt="sol-flow" hight="100" width="350"/>
</div>

## Project Workflow Diagram
<div align="center">
<img src="https://drive.google.com/uc?export=view&id=1Yr4yPMYReyavstmbkC9LPez2xiL3hBYM" alt="proj-flow" hight="100" width="500"/>
</div>

# Experimental Investigations
<div style="font-size:25px;">While analysiing the solution for this problem we have found some unwanted and some 
duplicate data that need to  be processed in a manner such that to get a accurate results. 
So, that we have removed some unwanted data also merged the duplicate data. In our 
project there are such constratints which can affect the analysis such as</div>

* There are some IPL Teams which changes their name at some seasons Eg:Delhi Daredevils, Royal Challengers Banglore, Sunrises Hyderabad etc... 
* There are some new IPL Teams which played for only few ipl seasons Eg: Kochi Tuskers 
Kerala etc.. 
* There is also teams like Pune Warriors played for some season. 
* There is also some teams like chennai and Rajasthan got banned for couple of years. 
* There evolved a 2 teams Gujarat Lions and  Rising Pune Spergiants which was  replacing 
the Chennai and Rajasthan. 