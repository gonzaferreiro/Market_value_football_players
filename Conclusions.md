# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)  DSI8 | Gonzalo Ferreiro | Capstone Project: 
## Predicting market value of football players

## Intro to conclusions

At the beginning and definition of this project, we told that the football players market is kind of a black box since nobody can be sure about the features that move the price of a player. Because of that, the main objectives of this project were:

* To introduce a systematic way of predicting the market value of football players. Independent of assumption

* Deep dive into the features that fix the market value of football players, bringing some clarity on the discussion about which things make a player more expensive than others

Out of those objectives, we can say that both of them partially accomplished. Let's go one by one, checking out the results, what things are now clearer and which ones would need further analysis.

## Systematic way of predicting the market value

At the beginning of this project, the decision of facing this challenge as a regression problem set up the path through which a lot of decisions were taken. Collecting data in such a way of obtaining a 'photo' of each player present characteristics and some data about his history as a player; past clubs, previous stats, awards won, between others. This data, analyzing through regression models, gave us an amazing accuracy to predict current value of football players.

In other words, our final model has the ability to predict with a more than reasonable confidence the current value of a football player, in case of not having that information. This was the main goal of the project, it's true. However, the model, as it was developed, has no ability what so ever to find the future price at which each player could be sold in the next transfer window. This was checked by comparing the model predictions against the updated value of 9 players who were sold in the last weeks. 

This conclusion gives the idea that maybe a time series model, including for each period all or some of the features used, could have been a better option, since it's seems that the future selling price of a football player may be highly correlated with his previous selling prices, the evolution of those prices throughout the player professional life, and also the evolution of some player's stats, as his overall rating, number of minutes played, and passing accuracy.

## Deep dive into the features that fix the market value of football players

### Overall conclusions about feature importance

Some about this has been already mentioned in the previous point, but after studying the results, we can highlight the highest value of each player's career as the most important feature of the dataset by far, followed by a set of features as the league where he's playing, the number of minutes played in the last season, as well as the number of minutes played in previous seasons, his overall last rating and the average of the previous seasons, the same about his passing accuracy, his age and the number of results obtained out of searching in Google his name + name of the team where he's right now.

How did we arrive to this?

First of all, by checking the feature importance of our best model, which was a Decision Tree Regressor, built as a combination of bagging (with 2.000 iterations) and grid search. This model scored 0.96 on the training group, 0.89 on the test group and 0.87 on the cross-validated groups. Even though the scores are great, this kind of model it's really a black box to find the most important features. However, taking the best estimator for each iteration and checking out the feature importance of each one and average the results to at least have an idea of what's happening inside that box.

<img src="https://imgur.com/dhOcgyn.png" height="400" />

To the left, we can the feature importance of individual features, post dummifying. While to the right we have the original variables grouped. Pay special attention to the logarithmic scale needed to reduce the difference between the highest value and the rest of the features.

An interesting analysis was done be modelling the same data only with the highest_value feature, and afterwards without it:

* Only with it, we get a score of 0.63 on the training group and 0.59 on the test group. Pretty amazing for just one feature, but not good enough to have reasonable predictions

* Without the highest value, the picture is not much better: 0.88 on the train group, but only 0.66 on the test

A conclusion out of this is that we need the combination of all the features, to arrive at our previous scores.

On the other hand, we also took one model, done with the same dataset, but using Linear Regression with Lasso regularization. T his model scored 0.78 on the training group, 0.80 on the test group and 0.71 on the cross-validated groups. Even though the predictions are not that great, this kind of model allows us to analyze our feature importance in a more friendly way:

<img src="https://imgur.com/INcswrC.png" height="400" />

Here, no logarithmic scale is needed, and we can see that some grouped features were even more important than the highest value. The interesting thing about this analysis is that we actually can trust in these features coefficients since the residuals of this model are pretty normally distributed, as we can see in the following plots:

<img src="https://imgur.com/NoLA0Pt.png" height="300" />

Finally, we repeated the features analysis throw Permutation Importance. This tool gives us a way to compute feature importance for any black-box estimator by measuring how the score decreases when a feature is not available. The idea is the following: feature importance can be measured by looking at how much the score decreases when a feature is not available. To do that one can remove the feature from the dataset, re-train the estimator and check the score. That's why this method of knowing feature importance is also known as “Mean Decrease Accuracy (MDA)”.

<img src="https://imgur.com/hB6E13b.png" height="300" width="900"/>

In this case, the analysis throws some similar results to the ones we saw through our Decision Tree Regressor model. However, the interesting thing about this is that although the highest value is the most important feature by far, it's also the one with the highest variance. That's probably why we cannot rely only on this variable to make our predictions.

We can see a summary of the three analysis in the following plot:

<img src="https://imgur.com/MJkBTES.png" height="400" />

### The role that the highest value of each players career has in our model

As we saw before, the highest value of their career is the most important feature of my dataset by far, but it's also the one with the highest variance. Let's go deep into that, to understand how is it impacting the predictions.

One of the things we observed through Permutation Importance, is that the highest value was the feature with the greatest variance throughout the dataset. This can be confirmed by the following plot:

<img src="https://imgur.com/DdOZUXG.png" height="200" />

This chart shows us indeed, that this feature has a massive right-skewed distribution, with a mean far to the right of the median, and a long tail, even setting a logarithmic scale. Doing some bootstrap on its variance should show us that's really hard to achieve a normal distribution:

<img src="https://imgur.com/fyu5vqN.png" height="500" />

Not even with 5000 samples, we can achieve a perfect normal distribution, since we can see some outliers in both tails.

**But how is this impacting our predictions?**

Let's check the following chart:

<img src="https://imgur.com/onqJU9B.png" height="400" />

Now, even though this chart seems to show that the model is making better predictions to those players who lost value versus those players that are right now at their best moment, this difference could be due to the presence of outliers. So let's check it out:

<img src="https://imgur.com/SGUY6mz.png" height="400" />

As we can see, even though we have outliers in both groups, for those players in shape there seems to be a higher amount of unusually expensive players. So let's individualize outliers and non_outliers, to see their difference in predictions individually and close our conclusions.

<img src="https://imgur.com/eFLuAMl.png" height="400" />

Even though the difference in predictions is around three times bigger in both groups (outliers and non_outliers), for those players in shape, and those which lost value throughout their career, in absolute terms, the real difference in predictions is approximately 10 times larger for outliers than for non_outliers. But let's see this difference in proportion with the real value of each group:

<img src="https://imgur.com/dsfrDT8.png" height="200" />

So in conclusion:

* For players in shape the difference in predictions, in proportion with the real average value, is around the double than in players that are not at their best moment. Therefore there seems to be that the highest_value feature is indeed introducing some bias into our model

* On the other hand, the presence of extreme outliers, far away from the upper fence, it's also an important point, since it's in part what is reducing the predicting power of the model

One last thing I tried to correct this situation, was to create a new dataset, with all the dummy and non-dummy variables I used throughout the project, to check if there was a model able to predict the residuals. For that, I used a Linear Regression model with Lasso regularization, and even though I obtain a 0.45 on the train score, the test group scored 0.21 and the cross-validated score -0.23. Therefore, when some outliers are in or out of the evaluated score, the model fails.

In conclusion, the extremely skewed distribution of the highest value of each players career it's needed for the accuracy of the model, but it's also introducing some bias into it. Pivoting to a time series model could solve this, keeping the features used, and adding changes throughout each player career.

### The role that the highest value of each players career has in our model

Another important feature according to the analysis previously shown, was the league where each player is right now.

As we can see in the following chart, our model is not being able to predict with the same accuracy players in the top 50, that below that threshold. Which is more than logical, since top players play in top leagues, top players mean more expensive players and more expensive players is synonymous of outliers. And there's where the model fails.

<img src="https://imgur.com/XNsQf5o.png" height="400" />

<img src="https://imgur.com/gX05O6b.png" height="300" />

## Mins, Ratings and real-life tool for clubs

Last rating, last mins and previous mins resulted in being three of the most important features of the dataset.

Let's check the relationship between them, adding up the previous ranking as an extra feature.

<img src="https://imgur.com/qLGGpgF.png" height="900" />

Things we can see here:

* There seems to be a positive correlation between last minutes and last rating. Which means that players who played more minutes in the last season, had a better overall rating. And the same happens with the previous season

* There seems to be also a positive correlation between previous ratings and last ratings. That means improvement

* The relationship between mins is more diffuse. Even though our plot indicates a positive correlation, and for some players, more mins in previous seasons implied more min in the last one, the chart it's a mess and we cannot back a positive correlation between variables

* Between the number of minutes played last season and the rating from the previous one, there seems to be a small relationship, in the sense that having more minutes in the last season could have been because of higher previous ratings. An even smaller relationship can be also seen the other way around, between the number of minutes played in the previous season and the rating from the last one

So, the big question now is:

**What if a player would have had more minutes in the last and previous seasons? What impact could that have had on their ratings and value?**. For that, I created a function which tries try to find players in between a given range of values find their value change according to:

* That they already have stats above a certain threshold

* That they will have more minutes, and as a result of that, also an improvement on their ratings

The following example is a search given the following conditions:

* Players with an original predicted value between 2.5 and 7.5mm
* Which in their last season had an overall rating above the percentile 50
* Which in their previous seasons had an overall rating above the percentile 70
* Which in their last season had fewer minutes than the percentile 30
* And with the promise of given them minutes above the percentile 80

The function follows the next steps:

1. Finds the players in between the given value
2. Sets the threshold for ratings and number of minutes
3. Filters the players according to those thresholds

The final task is to update their stats. The new ratings are found multiplying their real ratings by the improvement rate obtained from the relationship between the average rating of players above the new minute's threshold over the average rating of players under the threshold set for the player. For example: 7.6/6.1 = 1.24. The number of minutes it's just updated by the last and previous minutes played by players on the percentile indicated. In this case 80.

In this way, we obtain updated predictions, of how much more could a set of players be worth, according to this:

<img src="https://imgur.com/sG2Ddcr.png" height="300" />

Even though this tool is still not matching with the updated value of players after recent transactions, this tool could be improved, by updating also things as:

* The league, if the player is moving to another one
* The current club
* All the stats, according to more precise rates of improvement within the team's players real performance

## Overall conclusions

Let's remember once again the objectives we had at the beginning of this project:

* To introduce a systematic way of predicting the market value of football players.

* Deep dive into the features that fix the market value of football players

Out of those objectives, we can say that both of them were partially accomplished. Since this model proved to be a systematic way of predicting the CURRENT market value of football players and thrown some light into the things that make a player be more expensive. However, it also showed to have some weakness and no ability to predict future market value, even though this could be achieved by pivoting to a time series problem or improve the tool for searching players.
