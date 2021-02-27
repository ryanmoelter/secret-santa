import json
import psycopg2 as pg

class Database:
    """ Handles the main connection to the database of the app setting """
    def __init__(self, db, username, password, port, host, sslmode):
        self.db = db
        self.username = username
        self.password = password
        self.port = port
        self.host = host
        self.sslmode = sslmode
        self.cur = None
        self.conn = None

    def connect(self):
        self.conn = pg.connect(database=self.db, user=self.username, password=self.password, port=self.port, host=self.host, sslmode=self.sslmode)
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


with open("creds.json") as f:
    data = json.load(f)[0]
dbConn = Database(data['database'], data['username'], data['password'], data['port'], data['host'], data['sslmode'])
dbConn.connect()