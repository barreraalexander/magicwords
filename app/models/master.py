from app import db
from app.db import DB
from app.config import Mysql_Config
from secrets import token_hex
from datetime import datetime

class Model:
    mtype = 'model'
    tablename = 'none'
    db = DB(config=Mysql_Config)

#//SECTION: DB METHODS
    @classmethod
    def add (cls, model):
        """
        Model.add(model) inserts
        a new model into the databse.
        """
        ModelObj = cls._Model__getobj ()
        insert_statement = ModelObj.get_insert_statement (model)
        cls.db.insert(insert_statement)

    @classmethod
    def get (cls, by='', value='', getrandom=False, getall=False, getmany=False):
        """
        returns model object(s) 
        **by specifies the column to search

        **value specifies the value to search for in 'by'

        **getrandom=True always returns 1 random model from the table
        
        **getall=True returns all of the models in the table
        
        **getmany=True returns all of the models in the
                       table that match the query
        """
        ModelObj = cls._Model__getobj ()

        if getmany:
            records = cls.db.get(ModelObj.tablename, col=by,
                        value=value, getmany=True)
            models = [ModelObj(record) for record in records]
            return models

        if getall:
            records = cls.db.get(ModelObj.tablename, getall=True)
            models = [ModelObj(record) for record in records]
            return models


        record = cls.db.get(ModelObj.tablename, col=by, value=value, getrandom=getrandom)

        if record is None:
            return None
        
        model = ModelObj (record)
        return model

    @classmethod
    def mk_table (cls):
        """
        creates the model's
        complementary table 
        """
        ModelObj = cls._Model__getobj ()
        mk_table_statement = ModelObj.get_table_statement()
        cls.db.create_table (mk_table_statement)  

 
    @classmethod
    def update (cls, model):
        """
        updates a model in the db.
        Model.update(model) where model
        already exists in the db.
        """
        ModelObj = cls._Model__getobj ()
        update_statement = ModelObj.get_update_statement (model)
        cls.db.update(update_statement)

    @classmethod
    def __getobj (cls):
        return cls

    @classmethod
    def remove (cls, model):
        """
        model is deleted from the db,
        Model.remove(model) where model
        already exists in the db.
        """
        cls.db.remove(model)

#//SECTION: __init__
    def __init__(self, mdict):
        self._id = ""
        self.id = "" #accounts for some programs that use ._id as a built in
        self.upldate = 0 
        self.moddate = 0 
        self.__checkdict (mdict)

    def __checkdict (self, mdict):
        try:
            self._id = mdict['_id']
            self.id = mdict ['_id']
        except Exception as err:
            self._id = token_hex(15)
            self.id = token_hex(15)
        
        try:
            self.upldate = mdict ['upldate']
        except Exception as err:
            pass
            # print ('No Upload Date')

        try:
            self.moddate = mdict ['moddate']
        except Exception as setmoddate:
            pass 
            # print ('No Modification Date')



