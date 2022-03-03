import mysql.connector
from mysql.connector import Error

MYSQL_HOST = "sql11.freemysqlhosting.net"
MYSQL_DATABASE = "sql11476489"
MYSQL_USERNAME = "sql11476489"
MYSQL_PASSWORD = "6I6Z6kIDl3"

def get_link():
    connection = mysql.connector.connect(host=MYSQL_HOST,
                                            database=MYSQL_DATABASE,
                                            user=MYSQL_USERNAME,
                                            password=MYSQL_PASSWORD)
    cursor = connection.cursor()
    query  = "SELECT link from zoom_link limit 1"
    cursor.execute(query)
    result = cursor.fetchone()
    if result is None:
      raise Exception("No zoom links found in db")
    return result[0]