# Project 1: Data Modeling with Postgres <h1>
### Introduction <h3>
A startup called Sparkify wants to analyze the data they have been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

The analytics team wanted a data enginner, like you, to create a Postgres database with tables designed to optimize queries on song play analysis. Your task is to create a database schema and ETL pipeline for this analysis. Then test your database and ETL pipeline by running queries given to you by the Sparkify's analytics team and compare your results with their expected results.

## 1. Database design description <h2>
Using two source datasets, one called "song" and another "log" to create a star schema database optimized for queries on song play analysis. This includes the following tables:

### 1.1 Fact Table <h3>
* songplays - records in "log" data associated with song plays i.e. records with page NextSong. It has the following columns: songplay_id (PK), start_time, user_id, level, song_id, artist_id, session_id, location, user_agent. NOTE: PK denotes PRIMARY KEY.
  
### 1.2 Dimension Tables <h3>
* users - keeps unique user details with the following columns: user_id (PK), first_name, last_name, gender, level.
* songs - records unique song details with the following columns: song_id (PK), title, artist_id, year, duration.
* artists - stores unique artist details with the following columns: artist_id (PK), name, location, latitude, longitude.
* time - maintains unique time details with the following columns: start_time (PK), hour, day, week, month, year, weekday.

## 2. Files in the project workspace <h2>
In addition to the data/song_data and data/log_data files, the project workspace has the following components:

### 2.1 create_tables.py <h3>
This script does the following:

* Drops (if exists) and creates the sparkify database
* Establishes connection with the sparkify database and gets the database cursor
* Calls the script "drop_table_queries" to drop all the sparkify's tables 
* Calls the script "create_table_queries" to create all the sparkify's tables
* Closes the database connection

### 2.2 sql_queries.py <h3>
This script does the following:

* Drops all the tables with the script "drop_tables_queries"
* Creates all the tables with the script "create_tables_queries"
* Inserts records into various tables when called by the ETL pipeline

### 2.3 etl.ipynb <h3>
This jupyter notedbook contains detailed instructions on the ETL process of each of the tables.

### 2.4 test.ipynb <h3>
This jupyter notedbook contains instructions to check the database construction process. 

### 2.5 etl.py <h3>
This script does the following:

* Reads, processes and loads data from the song_data and log_data files into the tables created in the previous steps
