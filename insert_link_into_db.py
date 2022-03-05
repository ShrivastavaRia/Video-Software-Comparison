import mysql.connector
from mysql.connector import Error

MYSQL_HOST = "sql11.freemysqlhosting.net"
MYSQL_DATABASE = "sql11476489"
MYSQL_USERNAME = "sql11476489"
MYSQL_PASSWORD = "6I6Z6kIDl3"

def insert_link(link):
    connection = mysql.connector.connect(host=MYSQL_HOST,
                                            database=MYSQL_DATABASE,
                                            user=MYSQL_USERNAME,
                                            password=MYSQL_PASSWORD,)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS zoom_link")
        cursor.execute("CREATE TABLE zoom_link (link VARCHAR(255))")
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute("SHOW TABLES;")
        records = cursor.fetchall()
        print("All tables: {}".format(records))
        query = "INSERT INTO zoom_link (link) VALUES (\"%s\")" % link
        cursor.execute(query)
        connection.commit()