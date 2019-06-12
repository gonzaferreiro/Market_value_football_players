# Predicting market value of football players

## Introduction to the project

Football players market value is kind of a black box: more often than not it’s clear which players are worth more than others, but nobody knows with precision which are those features that move the price of a player, increasing o reducing it in thousands or even millions of dollars. That's why this project attempts to:

Introduce a systematic way of predicting the market value of football players. Independent of subjective assumption
 
Deep dive into the features that fix the market value of football players, bringing some clarity on the discussion about which things make a player more expensive than others

**[SPOILER ALERT]** The conclusions and results of the project can be found in this [Executive Summary of Conclusions](./Conclusions.md)

## Audience of these project

This project aims to attract the attention of two targets:

General audience: anybody who is into football will probably be interested in throwing some kind of certainty about what moves the price of a player. Any football fan around the world probably had one or several conversations about the topic and could be translated in any kind of publication of popular interest.
 
Football clubs: let’s remember the book and movie Moneyball, where the main character, Beane, needed to assemble a competitive baseball team with a limited budget. Rather than relying on scouts experience and intuition, Bean uses Data Science selecting players based on their on-base statistics. In the real world, many football teams are still buying players according to their intuition or popular knowledge about the price. This project could be translated into a concise purchase method for clubs.

## What are you going to find in this repository

This project was divided into 5 different stages:

1. Planning
2. Obtaining the data
3. Cleaning
4. Modelling 
5. Conclusions

### [STAGE 1] Planning

By popular knowledge, which are the things that usually we all talk about when discussing the price of a football player? This was the first question I made myself when I started to think about this project. Which I translated in trying to obtain:

1. Statistics about their performance
2. Some measure of the brand value (I'm going to explain this in detail later)
3. Demographic information
4. Behavioural data

From here I started gathering the following information.

### [STAGE 2] Obtaining the data

The biggest challenge around this, was indeed, not getting banned. All the websites I used to gather my dataset, have proactive banning systems to prevent large amounts of scraping. Therefore, I had to create some kind of incognito tool to prevent this situation. 

I ended up with two ways of scraping and not getting banned:

Using Tor Requests, in such a way that that the IP used in each iteration gets updated, preventing being banned in some websites as https://transfermarkt.co.uk/
 
Unfortunately, even though the previous one was the fastest way, https://whoscored.com was keeping banning me, so I created the souper class (also available in this repository), that uses Selenium’s webdriver, in order to create a new Chrome explorer in each iteration, using the headless option, to not open a window for each URL scraped. The class also includes several try-except conditions, in order to capture TimeOut exceptions, and has the possibility of passing a path if it’s necessary, to click on it.

Using the second method resulted in an unbeatable technique to not get banned, but also in an average of 40s per page. What ended up in approximately 47 hours of scraping, which will be detailed in the following points.

#### **[1. Obtaining the players](./Obtaining_players_and_teams.ipynb)**

The first step to gather all the data about the players was in fact to get the players. 
This task supposed to be easy didn’t was, since in https://transfermarkt.co.uk and https://whoscored.com each team and player has a unique identification number, that’s is present at their URL. Which makes unique each one of it. For example:

https://www.transfermarkt.co.uk/luis-suarez/profil/spieler/44352 : in Transfermkt, Luis Suárez is the player 44352. A number that’s at the end of the URL.

https://www.whoscored.com/Players/144175/History/Fabián-Noguera : in Whoscored, Fabián Noguera is the player 144175, having also his identification number inside the URL.

For the project, this situation implied:

Selecting by hand some leagues, to, first of all, obtain all the teams playing in that league. In the end, I scraped data from Tier 1 and 2 leagues from Europa, one league from South America (Argentina  Primera División), one league from North America (United States MLS) and one league from Asia (China Super League)
 
Later, once I had the URL of all the teams playing in each league, I went inside each one of those teams and grabbed all team’s players URL. Ending with   6000 players, from all around the world, different nationalities and characteristics.

All this was done in approximately 6 hours of scraping, mixing both webpages, and once I got all the players URL y was able to advance with the following scraping tasks.

#### **[2. Basic information](./Obtaining_basic_info_from_players.ipynb)**

Inevitable data as weight, height, the team where he is currently playing and position. This was all scraped from https://transfermarkt.co.uk in approximately 4 hours.

#### **[The age of each player](./Getting_age.ipynb)**

A key feature also scraped from https://transfermarkt.co.uk in approximately 3 hours.

#### **[3. Defensive statistics](./Obtaining_defensive_statistics_from_players.ipynb)**

A set of variables including interceptions, tackles, fouls, offsides won and own goals by season for the entire career of a player. Scraped from https://whoscored.com in approximately 4 hours.

#### **[4. Offensive statistics](./Obtaining_player_offensive_statistics.ipynb)**

As the previous data, but in this case about key passes, dribbles, bad controls and more, also for the entire career of each player and from https://whoscored.com in approximately 4 hours.

#### **[5. Summary statistics](./Obtaining_player_summary_statistics.ipynb)**

Some more general and shared data in between positions in the field, as minutes played, goals, yellow and red cards, passes, the number of times being the man of the match, average rating and some more, also scraped from https://whoscored.com in approximately 4 hours.

#### **[6. Suspensions and injuries](./Suspensions_and_injuries.ipynb)**

Anybody who supports any team knows that there is nothing worst that your club buying a player that’s just always injured, or is constantly sent out the field. Teams also know that when the moment of setting a price arrives. That’s why I also scraped from https://transfermarkt.co.uk the number of days and matches that each player has missed in their career because of suspensions or injuries. This scraping took about 3 hours.

#### **[7. Awards](./Scrapping_awards_class.ipynb)**

Under the hypothesis about the fact that winning an individual award (for example, being the best player of the year in a local league), playing and the Football World Cup or ending runner-up in an important competition, could increase the value of a football player, as it increases their salary, I scraped a wide range of awards from https://transfermarkt.co.uk. This was a scraping task of about 4 hours.

#### **[8. National appearences and agent](./Getting_national_ap.ipynb)**

In the same line of thought as the previous point, the fact of a player playing in the national team of his country could be a measure of how good he is. That’s why, in case of having played at any time, I got also from https://transfermarkt.co.uk the number of minutes played.

As a bonus track, I got from the same place the agent of each player. Since maybe all the best players were under the radar of a specific group of agents.

All this scraping took around 3 hours.

#### **[9. Target variable and other features](./Getting_several_features_from_profile.ipynb)**

https://transfermarkt.co.uk gave me the target feature, as they have the current value of all football players. From the same URL, I got some more data, about the highest value of each players career, and the last three teams were he played. Scrape all this was a job of approximately 3 hours.

#### **[10. Google results](./Google_results.ipynb)**

As every football fan knows, not always the value of a player is only measured in terms of his individual statistics or demographic information. Sometimes, it also depends of how many jerseys or tickets can his name sell, just because of the fact of playing.

In this sense, there’s some sort of ‘brand value’ each player has. To measure that, in the first instance I scraped the number of results that throws the Google search of their name + the team where he plays. The decision of adding the name of the team at the end was based on the fact that otherwise, for some players with very generic combinations of name-last name, I was getting some non-realistic numbers.

This scraping was directly done from Google in about 3 hours.

#### **[11. Twitter sentiment analysis](./Tweets_Sentiment_Analysis.ipynb)**

An entire Readme file could be done about this part, but I’ll try to summarize this in a few lines. Basically, I used Tweepy and Textblob libraries, to create a class capable of obtaining 200 tweets per player, obtain the polarity of each online, in order to classify Tweets as positives, negatives or neutrals. This task was done by connecting directly to Twitter’s API and sending requests every fifteen minutes, to obtain all players with tweets in about 5.5 hours.

#### **[12. Clubs and national teams ranking](./Team_and_national_teams_ranking_scraps-Final.ipynb)**

In previous points, I talked about some scraping done to obtain features as current and previous teams, and the number of minutes played at the national team. All of this would be incomplete if it wasn’t matched with ranking positions. Because, as we all know, it’s not the same having played 100 minutes in a team ranked 200, as in a team ranked 2.

The teams ranking scrape was done from the webpage of the Club World Ranking (https://www.clubworldranking.com) and it took approximately 10 minutes, as it was the only scrape I could do with the in-built request Python’s tool. The national teams ranking was done from https://transfermarkt.co.uk and it took around 20 minutes to be completed.


### [STAGE 3] Cleaning the data

The cleaning stage of the project, even though it was extensive and detailed, doesn't have much information to add to this executive summary. It consisted of importing the 16 datasets created out of the scraping, in order to clean columns, rename variables, update string values, change types, merging datasets and more tasks like this.

The only thing that it's worth the comment, it's that since the target variable had an extremely skewed distribution to the right, due to the presence of outliers, I applied some log transformation on the target variable to reduce the noise.

The next charts show the distribution of the target variable post and pre log transformation:

<img src="https://i.imgur.com/FKohaDH.png" height="400" />

In the same way, the next box plot shows the small presence of outliers after the transformation:

<img src="https://imgur.com/ZnHONXp.png" height="200" />

Some other interesting things that were done in this stage were:

1. Create some complex functions to match team names in between datasets, with the added complexity of having several teams with different names in each one, repeated words in between teams in the same League (for example, Manchester City and Manchester United).

2. Create categories for the different kind of awards in such a way of reducing the original awards dataset into less and maybe more relevant set of awards. Leaving alone just the most important ones, and grouping the rest.

3. For the stats features, two big groups were created: i) One for all the last and more recent stats, identified with the word 'last' at the beginning of each feature's name, ii) Another one with all previous stats grouped in one feature per stat. For this, in some cases, the average was used (for example, 'previous_owngoals' is the average number of own goals made per season) and in others the sum (for example, 'previous_minutes' is the sum of all the minuted played in previous seasons).

4. Also for the stats features, another group of variables was created, as the average number of goals, assistance, yellow cards, red cards and number of times selected as Man Of the Match, per year as a professional player, taking seventeen years old as the starting point of each player's career

5. In a similar way as the previous point, the variable 'miss_days_per_y' was calculated according to the number of days each player missed because of being injured of suspended, according to the number of years as professional.

All the cleaning can be find in [this notebook](./FINAL_1_Cleaning_stage.ipynb)

And the features dictionary with all the variables used, can be found in [this document](./Features Dictionary.txt)

### [STAGE 4] Modeling

Even though this stage was supposed to be just modelling, it ended up being necessary to do some cleaning tasks, mostly about dummifying some features and renaming columns, in order to merge the different dataset I had.

Once all the merging was done I worked with three different datasets:

1. **The teams dataset**: based on a project from Tilburg University about the same topic, I decided to create a dataset just with the dummy variables out of the last three teams were each player played.

2. **The complete dataset**: which all the data, excepting the teams

3. **The mega dataset**: which was created, at last, merging the remaining features after regularization, from both, the teams dataset, and the complete dataset. This ended up being the dataset used throughout the modelling.

Regarding the models used, I tried to apply as many models as possible, mixing some parametric and non-parametric models:

1. Simple Linear Regression
2. Linear Regression with Lasso Regularization
3. Linear Regression with Ridge Regularization
4. Decision Trees
5. Decision Trees + Bagging
6. Ransac Regressor
7. Huber Regressor

In the end, the best scores were obtained through:

**Parametric modelling: Linear Regression with Lasso, using the mega dataset**: this model scored 0.78 on the training group, 0.80 on the test group and 0.71 on the cross-validated groups.

** Non-parametric modelling: Decision Trees Regressor + Bagging, using Grid Search**: this model scored 0.96 on the training group, 0.89 on the test group and 0.87 on the cross-validated groups.

All the modeling can be find in [this notebook](./FINAL_2_Merging_and_modeling_v2.ipynb)

### [STAGE 5] Conclusiones

The conclusions of this project can be found in the following places:

1. [Executive Summary of Conclusions](./Conclusions.md)

2. [Notebook with code in detail](./FINAL_3_Post_visualizations.ipynb)
