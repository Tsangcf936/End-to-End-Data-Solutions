# Project 1: Data Modeling with Postgres <h1>
### Introduction <h3>

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

The analytics team wanted a data enginner, like you, to create a Postgres database with tables designed to optimize queries on song play analysis. Your task is to create a database schema and ETL pipeline for this analysis. Then test your database and ETL pipeline by running queries given to you by the Sparkify's analytics team and compare your results with their expected results.

## 1. Database design description <h2>

There are two source datasets, one called "song" and another "log". And from these two datasetes the following star schema database will been created for optimized queries on song play analysis. The tables are as below:

### 1.1 Fact Table <h3>
The fact table in this star scheme will be named "songplays" and is designed to record "log" data associated with song plays. This fact table will have the following columns: songplay_id (PK), start_time (FK), user_id (FK), level, song_id (FK), artist_id (FK), session_id, location, user_agent. NOTE: PK denotes PRIMARY KEY and FK denotes FORIEGN KEY.
