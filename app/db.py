# import MySQLdb.connections
import mysql.connector

# //SECTION: __init__  
class DB:
    def __init__(self, config):
        self.username = config.MYSQL_USER
        self.password = config.MYSQL_PASSWORD
        self.host = config.MYSQL_HOST
        self.schema = config.MYSQL_DB
        
        #CONNECTION
        self.cnx = mysql.connector.connect(
            user=self.username,
            password=self.password,
            host=self.host,
            database=self.schema
        )

        #CURSOR
        self.cur = self.cnx.cursor(dictionary=True)
    

    def get (self, tablename, col='column', value='value', getrandom=False, getall=False, getmany=False):
        statement = (f"""SELECT * FROM {tablename}
        WHERE {col} = "{value}" """)

        if getrandom is True:
            statement = (f"""SELECT * FROM {tablename}
                        ORDER BY RAND() LIMIT 1""")

        elif getall is True:
            statement = (f""" SELECT * FROM {tablename} """)
            self.cur.execute (statement)
            records = self.cur.fetchall ()
            return records

        
        if getmany is True:
            self.cur.execute (statement)
            records = self.cur.fetchall ()
            return records
            
        self.cur.execute (statement)
        record = self.cur.fetchone ()
        return record

    def create_table (self, statement):
        try:    
            self.cur.execute (statement)
            self.cnx.commit()
            return True
        except Exception as err:
            print ('Error Creating Table:')
            print ('-' * 30)
            print (err)
            return False


    def insert(self, statement):
        self.cur.execute (statement)
        self.cnx.commit()


    def insert_model(self, model):
        try:
            return True
        except Exception as err:
            print (f'Error Inserting {model._id} Table:')
            print ('-' * 30)
            print (err)
            return False

    def remove_model(self, model):
        try:
            return True
        except Exception as err:
            print (f'Error Removing {model._id} Table:')
            print ('-' * 30)
            print (err)
            return False

    def run (self):
        pass
        # self.__mk_table("scraped_words")
        # self.__mk_table("my_words")
    