from bs4 import BeautifulSoup
import pandas as pd
import requests
import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(user = "postgres",
                                password = "light",
                                host = "127.0.0.1",
                                port = "5432",
                                database = "postgres")
cursor = connection.cursor()

create_table =  '''CREATE TABLE IMDB
                (ID INT PRIMARY KEY NOT NULL,
                MovieName TEXT NOT NULL,
                Raing TEXT NOT NULL,
                Star_Cast TEXT NOT NULL); '''

cursor.execute(create_table)
connection.commit()
print("Table created successfully in PostgreSQL ")

MovieName = []
imdbRating = []
StarCast = []
count=1
for page_index in range(1,1100,50):
    response = requests.get("https://www.imdb.com/search/title/?title=a&start="+str(page_idx)+"&ref_=adv_nxt")
    soup = BeautifulSoup(response.content,"lxml")
    for i in soup.findAll('div',attrs={'class' : 'lister-item-content'}):
        print(count)
        star_cast=[]
        for temp in i.findAll('a'):
                if len(temp.text)>4:
                        cast.append(temp.text)

        Name_movie=star_cast[0]
        Movie_rating = i.find('strong') 
        if rating== None :
                rating="Not Rated"
        else:
                Movie_rating=Movie_rating.text
        star_cast=str(";".join(cast[1:]))


        movieName.append(Name_movie)
        imdbRating.append(Movie_rating)
        StarCast.append(star_cast)

        insert_table = ''' INSERT INTO IMDB 
                                 VALUES (%s,%s,%s,%s) '''
        value_table = (str(counting),movieName,Movie_rating,star_cast)
        counting+=1

        cursor.execute(insert_table,value_table)
        connection.commit()

if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

