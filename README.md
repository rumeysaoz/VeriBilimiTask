# VeriBilimiTask

## Table of contents
* [General info and Technologies](#general-info-and-technologies)
* [Setup](#setup)

## General info and Technologies
First of all, I used the PostgreSQL database and the pgAdmin tool. 
I created my tables and types of data in order to be able to import the data of the files with the extension ".csv" given to me to my database

The first obstacle I encountered here was the problems that might arise with the given data names, 
for example; angular_velocity.in the csv file, I changed the name of the column named "time" to "gps_time".

I have discovered two ways to add the data in the given files to my database. The first of these is done using the QUERY TOOL;
```
Copy flights
From '?C:\Users\öz\Desktop\Task\flight .csv'
DELIMITER ','
CSV HEADER;
```
But since this way can only create problems in the future because reading is done, I preferred the second way I discovered.

In the second way, both reading and writing operations can be performed and it is done using the PSQL TOOL:
```
\copy flights_table from '?C:/Users/öz/Desktop/Task/flight .csv' with CSV;
```
Later, I used the "psycopy2" library to provide a connection between the python language and PostgreSQL. 
You can also use the library by following the steps below:

## Setup
```
$ pip install psycopg2
```
Now that we have established our library, we can include the library in our project. To do this, let's add the following code to the top of our file:
```
import psycopg2
```
