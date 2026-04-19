import mysql.connector


def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vishnu@9999",   
        database="university_db"
    )

    return conn