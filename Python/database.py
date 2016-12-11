'''
Introduction to Software Engineering, Team 3 | Project 3
@Team_Members: Team Members: Jonathan Sanchez
Date: December 9th, 2016
'''



''' IMPORTS '''
import mysql.connector
from mysql.connector import Error
import datetime
''' IMPORTS '''

''' Connect to MySQL database - START'''
try:
    print('Connecting to MySQL database...')
    global conn
    conn = mysql.connector.connect(
        user='nyit',
        password='nyit123',
        host='138.197.34.187',
        database='denton')
        
    if conn.is_connected():
        print("Connection established.")
            
        # Cursor object used to execute SQL commands.
        global cursor
        cursor = conn.cursor()

    else:
        print('Connection failed.')
        

except Error as e:
    print(e)