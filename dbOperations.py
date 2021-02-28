import json
import psycopg2 as pg
import os

class Database:
    """ Handles the main connection to the database of the app setting """
    def __init__(self, db_url):
        self.db_url = db_url
        self.cur = None
        self.conn = None

    def connect(self):
        self.conn = pg.connect(self.db_url)
        self.cur = self.conn.cursor()

    def execute_insert(self,query,name):
        try:
            self.cur.execute(query, (name,))
            self.conn.commit()
            print(" Added {} to group_members table.".format(name))
        except Exception as e:
            self.conn.rollback()
            raise e

    def close(self):
        self.cur.close()
        self.conn.close()
    
    def execute_select(self,query):
        self.cur.execute(query)
        return self.cur.fetchall()

    """ Add/Alter/Drop DB Tables """    
    def create_group_table(self):
        """ creates group members tables """
        query = """CREATE TABLE group_members(Id serial PRIMARY KEY,Name varchar(100) NOT NULL,Request_time timestamp NOT NULL);"""
        self.cur.execute(query)
        self.conn.commit()

    def drop_group_table(self):
        """ Deletes group table in the app """
        query = """DROP TABLE IF EXISTS group_members;"""
        self.cur.execute(query)
        self.conn.commit

db = os.getenv('DATABASE_URL')
dbConn = Database(db)
dbConn.connect()