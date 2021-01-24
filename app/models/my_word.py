from app.models.master import Model

class MyWord(Model):
    m_type = 'my_word'
    tablename = 'my_words'

#//SECTIONS: DB STATEMENTS 
    @classmethod
    def get_insert_statement (cls, model):
        """
        Returns the record/statement insertion
        command to be executed by the db
        """
        statement = (f"""
            INSERT INTO {model.tablename}
                (_id, word, used_in, weight)
            VALUES
                ('{model._id}', '{model.word}',
                '{model.used_in}', '{model.weight}')
            """)
        return statement
    
    @classmethod
    def get_table_statement (cls):
        """ Returns the DB statement that
            creates this model's table"""
        statement= (f""" 
        CREATE TABLE {cls. tablename} (
            _id varchar(50) PRIMARY KEY,
            word varchar(100) UNIQUE,
            used_in text,
            weight float,
            upldate datetime DEFAULT CURRENT_TIMESTAMP(),
            moddate datetime DEFAULT CURRENT_TIMESTAMP()
        );""")
        return statement

    @classmethod
    def get_update_statement(cls, model):
        """ Returns the DB statement that
            updates models in this table"""
        statement =(f"""UPDATE {cls.tablename}
            SET
                used_in  ="{model.used_in}",
                weight = "{model.weight}",
                moddate = CURRENT_TIMESTAMP()
            WHERE _id = "{model._id}" """)
        return statement

#//SECTION: __init__ METHOD
    def __init__(self, mdict):
        super().__init__(mdict)
        self.word = mdict['word']
        self.used_in = mdict['used_in']
        self.weight = mdict['weight']


    def __str__(self):
        return (f""" 
        ID: {self._id}
        Word: {self.word}
        Modification Date: {self.moddate}
        Upload Date: {self.upldate}
        """)