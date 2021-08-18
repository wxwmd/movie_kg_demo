import json
import pandas as pd

f=open('./small_movie_info.txt','r+',encoding='utf-8')

movies=[]

while True:
    line=f.readline()
    if not line:
        break
    movie=json.loads(line)
    movies.append(movie)


# 得到演员实体
actors=set()
for movie in movies:
    contains_actors=movie['actors']
    for contain_actor in contains_actors:
        actors.add(contain_actor['name'])

actor_entity=pd.DataFrame()
actor_entity['name']=[actor for actor in actors]
actor_entity.to_csv('./actors_entity.csv',index=False,header=True)

# 得到导演实体
directors=set()
for movie in movies:
    contains_directors=movie['directors']
    for contain_director in contains_directors:
        directors.add(contain_director['name'])

director_entity=pd.DataFrame()
director_entity['name']=[director for director in directors]
director_entity.to_csv('./directors_entity.csv',index=False,header=True)

# 得到电影实体
movie_names=[]
movie_countries=[]
movie_languages=[]
movie_pubdates=[]
movie_other_names=[]
movie_summary=[]
for movie in movies:
    movie_names.append(movie['name'])
    movie_countries.append(movie['countries'])
    movie_languages.append(movie['languages'])
    movie_pubdates.append(movie['pubdates'])
    movie_other_names.append(movie['other_names'])
    movie_summary.append(movie['summary'])
movie_entity=pd.DataFrame()
movie_entity['names']=movie_names
movie_entity['countries']=movie_countries
movie_entity['languages']=movie_languages
movie_entity['pubdates']=movie_pubdates
movie_entity['other_names']=movie_other_names
movie_entity['summary']=movie_summary

movie_entity.to_csv('./movie_entity.csv',index=False,header=True)

# 电影-导演关系
movie_name=[]
director_name=[]
for movie in movies:
    for director in movie['directors']:
        movie_name.append(movie['name'])
        director_name.append(director['name'])
movie2director=pd.DataFrame()
movie2director['movie']=movie_name
movie2director['director']=director_name
movie2director['relation']=['DirectBy']*len(movie_name)
movie2director.to_csv('./movie2director.csv',index=False,header=True)

# 电影-演员关系
movie_name=[]
actor_name=[]
for movie in movies:
    for actor in movie['actors']:
        movie_name.append(movie['name'])
        actor_name.append(actor['name'])
movie2actor=pd.DataFrame()
movie2actor['movie']=movie_name
movie2actor['actor']=actor_name
movie2actor['relation']=['ActBy']*len(movie_name)
movie2actor.to_csv('./movie2actor.csv',index=False,header=True)