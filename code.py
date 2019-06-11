# --------------
import pandas as pd 
import numpy as np

# Read the data using pandas module.
data = pd.read_csv(path)
data.head()

# Find the list of unique cities where matches were played
list_of_unique_cities = data['city'].unique()
print('Unique Cities:- ', list_of_unique_cities)
number_of_unique_cities = len(data['city'].unique())
print('No of Unique cities:- ', number_of_unique_cities)

# Find the columns which contains null values if any ?
null_values = data.isnull().sum()
print('Null values in the dataset are:- ', null_values)

# List down top 5 most played venues
top_five_venues = data.groupby('venue')['match_code'].nunique().sort_values(ascending=False)[0:5]
print("Top five venues are:- ", top_five_venues)

# Make a runs count frequency table
runs_count = data['runs'].value_counts()
print('Runs Frequency Table:- ', runs_count)

# How many seasons were played and in which year they were played 
data['year'] = data['date'].apply(lambda date_year:date_year[:4])
print('No of seasons played:- ', len(data['year'].unique()))
print('Seasons played in years:- ', np.sort(data['year'].unique()))

# No. of matches played per season
matches_played_each_season = data.groupby('year')['match_code'].nunique().sort_values()
print('No of matches played per season are:- ', matches_played_each_season)

# Total runs across the seasons
total_runs_per_season = data.groupby('year')['total'].sum()
print('Total number of runs per season:- ', total_runs_per_season)

# Teams who have scored more than 200+ runs. Show the top 10 results
highest_score_makers = data.groupby(['match_code', 'inning', 'batting_team'])['total'].sum().reset_index()
print("Top 10 best performing teams are:- ", highest_score_makers[highest_score_makers['total']>200][:10])

print('======================================================================================')

# What are the chances of chasing 200+ target
high_scores1 = highest_score_makers[(highest_score_makers['inning'] == 1) & (highest_score_makers['total'] > 200)]
high_scores2 = highest_score_makers[(highest_score_makers['inning'] == 2) & (highest_score_makers['total'] > 200)]

high_scores1=high_scores1.merge(high_scores2[['match_code','inning','total']], on='match_code')

high_scores1.rename(columns={'inning_x':'inning_1','inning_y':'inning_2','total_x':'inning1_runs','total_y':'inning2_runs'}, inplace=True)
high_scores1['won_loss'] = np.where(high_scores1['inning2_runs'] > high_scores1['inning1_runs'], 'yes', 'no')
chances = high_scores1['won_loss'].value_counts()[1]/high_scores1['won_loss'].value_counts()[0]
print('Chances of opposition team in 2nd inning chasing the rival team in 1st innings are:- ',round(chances, 3))

# Which team has the highest win count in their respective seasons?
remove_duplicate_match_codes = data.drop_duplicates(subset='match_code', keep='first').reset_index(drop=True)
match_won_by_team = remove_duplicate_match_codes.groupby('year')['winner'].value_counts()
print('Match won by each team in respective seasons:- ', match_won_by_team)






















