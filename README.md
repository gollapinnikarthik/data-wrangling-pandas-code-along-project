### Project Overview

 # Data Wrangling with Pandas

IPL Dataset Analysis
Problem Statement
We want to know as to what happens during an IPL match which raises several questions in our mind with our limited knowledge about the game called cricket on which it is based. This analysis is done to know as which factors led one of the team to win and how does it matter.

About the Dataset :
The Indian Premier League (IPL) is a professional T20 cricket league in India contested during April-May of every year by teams representing Indian cities. It is the most-attended cricket league in the world and ranks sixth among all the sports leagues. It has teams with players from around the world and is very competitive and entertaining with a lot of close matches between teams.



### Learnings from the project

Reading the data using read_csv.
Using unique function in pandas module.
Difference between series and a dataframe.
Creating addational dataframes using conditional filtering.
Difference between unique and nunique and using sort_values function ascending as well as descending.
Using apply on data frame using lamda function.
Using groupby function and apply aggegrate on those saved variables.
Filling null values and finding out the null values. 
Removing duplicates values and resetting index.


### Approach taken to solve the problem

 Loaded the ‘ipl_dataset’ using the pandas csv module.
Found the list of unique cities where matches are being played throughout the world.
Found the columns containing null values.
Matches are played throughout the world in different countries but they may or may not have multiple venues(stadiums where matches are played). Found and displayed the top 5 venues where the most matches are played.
Found out how the runs were scored that is the runs count frequency table( number of singles, doubles, boundaries, sixes etc were scored seperately).
Extract how many seasons were played and which year were they played
Found out the total number of matches played in each season.
Found out the total number of runs scored in each season.
There are teams which are high performing and low performing. Looked at the aspect of performance of an individual team and filtered the data and aggregate the runs scored by each team. Displayed top 10 results which are having runs scored over 200.
Found out what were the chances that a team scoring runs above 200 in their 1st inning is chased by the opposition in 2nd inning.
Displayed team which has the highest win counts in their respective seasons.


