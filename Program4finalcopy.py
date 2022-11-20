# -*- coding: utf-8 -*-
#CIS 443-01: Program 4
#Due: 12/4/21
#Grading ID: P7161
#This program analyzes the sentiment and polarity of the reviews from a Trip Advisor CSV file
#And calculates percentages of agreement between rating sentiment and review sentiment

import pandas as pd
from textblob import TextBlob

def get_sentiment(rating):
    if rating >= 4:
        sentiment = 'positive'
    elif rating == 3:
        sentiment = 'neutral'
    else:
        sentiment = 'negative'
    return sentiment

def get_polarity(polarity):
    if polarity < -0.05:
        sentiment = 'negative'
    elif polarity > 0.05:
        sentiment = 'positive'
    else:
        sentiment = 'neutral'
    return sentiment

tripadvisor_hotel_reviews = pd.read_csv("tripadvisor_hotel_reviews.csv") #read file and create dataframe
tripadvisor_hotel_reviews['Sentiment'] = [get_sentiment(rating) for rating in tripadvisor_hotel_reviews.Rating] #for each rating calc sentiment and add to new column

tripadvisor_hotel_reviews['SentimentPolarity'] = [TextBlob(review).sentiment.polarity for review in tripadvisor_hotel_reviews.Review]

tripadvisor_hotel_reviews['Polarity'] = [get_polarity(polarity) for polarity in tripadvisor_hotel_reviews.SentimentPolarity]

tripadvisor_hotel_reviews["Agreement"] = tripadvisor_hotel_reviews.Sentiment == tripadvisor_hotel_reviews.Polarity


print("Overall Star-Sentiment Agreement")
review_count = tripadvisor_hotel_reviews.Review.count()
print("Number of reviews:", review_count)
print()
agreement_count = tripadvisor_hotel_reviews[tripadvisor_hotel_reviews.Agreement==True].Agreement.count() #from a section of the dataframe, find if agreement between rating sentiment and review sentiment is true
print("Number agree:", agreement_count, f'{100*agreement_count / review_count:.2f}%') #and then count the ones that agree
disagr_count = review_count - agreement_count #subtract to find the ones that disagree
print("Number disagree:", disagr_count, f'{100*disagr_count / review_count:.2f}%')
print()
print("Review Stars|Total Reviews|Num Agree|% Agree|Num Disagree|% Disagree")
print("------------|-------------|---------|-------|------------|----------")


#for each review, calculate the total reviews, # that agree/disagree, and their percentages
for review in range(5, 0, -1): 
    reviews = tripadvisor_hotel_reviews[tripadvisor_hotel_reviews.Rating==review]
    review_count = reviews.Review.count()
    agreement_count = reviews[reviews.Agreement==True].Agreement.count()
    disagr_count = review_count - agreement_count
    print(f'{review:^8}', f'{review_count:^21}', f'{agreement_count:^4}',f'{100*agreement_count / review_count:>7.2f}%', f'{disagr_count:>8}', f'{100*disagr_count / review_count:>10.2f}%')
    