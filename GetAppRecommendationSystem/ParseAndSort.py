import numpy as np  
import pandas as pd

ratings_data = pd.read_csv("activityRanking.csv" )  
ratings_data.head()  
activity_names = pd.read_csv("activity.csv")  
activity_names.head()  
print ("*********ratings_data: *********")
print(ratings_data)
print ("*********/ratings_data: *********")
print("\n")
print ("*********Activity Name: *********")
print(activity_names)
print ("*********/Activity Name: *********")
print("\n")

# activity_names['activity_id'] = ratings_data['activity_id'].astype(float)

activity_data = pd.merge(ratings_data, activity_names, on='activity_id')  

print ("*********activity_data: *********")
print(activity_data)
print ("*********/activity_data: *********")
print("\n")

activity_data.head()  
activity_data.groupby('name')['rank'].mean().head()  
activity_data.groupby('name')['rank'].mean().sort_values(ascending=False).head()  
activity_data.groupby('name')['rank'].count().sort_values(ascending=False).head()  
print ("*********activity_data2: *********")
print(activity_data)
print ("*********/activity_data2: *********")
print("\n")



ratings_mean_count = pd.DataFrame(activity_data.groupby('name')['rank'].mean())  
print ("*********post ratings_mean_count: *********")
print(ratings_mean_count)
print ("*********/ post ratings_mean_count: *********")
print("\n")
ratings_mean_count['rating_counts'] = pd.DataFrame(activity_data.groupby('name')['rank'].count())



import matplotlib.pyplot as plt  
import seaborn as sns  
sns.set_style('dark')  

# plt.figure(figsize=(8,6))  
# plt.rcParams['patch.force_edgecolor'] = True  
# sns.jointplot(x='rank', y='rating_counts', data=ratings_mean_count, alpha=0.4) 
# plt.show()
# print(activity_data)
user_activity_rating = activity_data.pivot_table(index='user_id', columns='name', values='rank')  
# print(user_activity_rating)
user_activity_rating.head()  
football_rating = user_activity_rating['Football babyyyyy']  
football_rating.head()  
activities_like_football = user_activity_rating.corrwith(football_rating)
corr_football = pd.DataFrame(activities_like_football, columns=['Correlation'])  
corr_football.dropna(inplace=True)  
corr_football.head() 
corr_football.sort_values('Correlation', ascending=False).head(10)      
corr_football = corr_football.join(ratings_mean_count['rating_counts'])  
corr_football.head()  
corrResults = corr_football[corr_football ['rating_counts']>50].sort_values('Correlation', ascending=False)
print ("*********final corr results: *********")
print(corr_football)
print ("*********/ final corr results: *********")
print("\n")
