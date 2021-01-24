from app.models.master import Model

class Scraped_Word(Model):
    m_type = 'scraped_word'
    tablename = 'scraped_words'

#//SECTIONS: DB STATEMENTS 
    @classmethod
    def get_insert_statement (cls, model):
        """
        Returns the record/statement insertion
        command to be executed by the db
        """
        statement = (f"""
            INSERT INTO {model.tablename}
                (_id, word, pos, definitions, rels, syns,
                ants, weight, scraped_from,
                scraped_url, used)
            VALUES
                ('{model._id}', '{model.word}',
                '{model.pos}', '{model.definitions}',
                '{model.rels}',  '{model.syns}',
                '{model.ants}', {model.weight},
                '{model.scraped_from}', '{model.scraped_url}',
                '{model.used}')
            """)
        return statement

    @classmethod
    def get_table_statement (cls):
        """ 
        Returns the DB statement that
        creates this model's table
        """
        statement= (f""" 
            CREATE TABLE {cls.tablename} (
                _id varchar(100) PRIMARY KEY,
                word varchar(100) UNIQUE,
                pos text,
                definitions text,
                rels text,
                syns text,
                ants text,
                weight float,
                scraped_from varchar(50),
                scraped_url text,
                used int DEFAULT 0,
                upldate datetime DEFAULT CURRENT_TIMESTAMP(),
                moddate datetime DEFAULT CURRENT_TIMESTAMP()
            );""")
        return statement

    @classmethod
    def get_update_statement(cls, model):
        """
        Returns the DB statement that
        updates models in this table
        """
        statement =(f"""UPDATE {cls.tablename}
            SET
                weight = "{model.weight}",
                moddate = CURRENT_TIMESTAMP()
            WHERE _id = "{model._id}" """)
        return statement

#//SECTION: __init__ METHOD
    def __init__(self, mdict):
        super().__init__(mdict)
        self.word = mdict['word']
        self.pos = mdict['pos']
        self.definitions = mdict['definitions']
        self.rels = mdict['rels']
        self.syns = mdict['syns']
        self.ants = mdict['ants']
        self.weight = 0
        self.scraped_from = mdict['scraped_from']
        self.scraped_url = mdict['scraped_url']
        self.used = 0

        self._check_scraped_word (mdict)


    def _check_scraped_word(self, mdict):
        """
        helper method for __init__ that sets defaults
        to dictionaries missing certain keys
        """
        try:
            self.weight = mdict['weight']
        except Exception as err:
            self.weight = 0

        try:
            self.used = mdict['used']
        except Exception as err:
            self.used = 0


        # try:
        #     self.definitions = "$".join(self.definitions)
        # except Exception as err:
        #     print (err)

    def __str__(self):
        return (f"""
        ID: {self._id}
        Word: {self.word}
        Modification Date: {self.moddate}
        Upload Date: {self.upldate}
                """)