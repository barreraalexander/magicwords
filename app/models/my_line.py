from app.models.master import Model

class MyLine(Model):
    m_type = 'my_line'
    tablename = 'my_lines'

#//SECTIONS: DB STATEMENTS 
    @classmethod
    def get_insert_statement (cls, model):
        """
        Returns the record/statement insertion
        command to be executed by the db
        """
        statement = (f"""
            INSERT INTO {model.tablename}
                (_id, position, line, used_in)
            VALUES
                ("{model._id}","{model.position}",
                "{model.line}", "{model.used_in}")
            """)
        return statement
    
    @classmethod
    def get_table_statement (cls):
        """ Returns the DB statement that
            creates this model's table"""
        statement= (f""" 
        CREATE TABLE {cls. tablename} (
            _id varchar(50) PRIMARY KEY,
            position int,
            line text,
            used_in text,
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
                position  ="{model.position}",
                used_in  ="{model.used_in}",
                moddate = CURRENT_TIMESTAMP()
            WHERE _id = "{model._id}" """)
        return statement

#//SECTION: __init__ METHOD
    def __init__(self, mdict):
        super().__init__(mdict)
        self.position = mdict['position']
        self.line = mdict['line']
        self.used_in = mdict['used_in']

    def __str__(self):
        return (f""" 
        ID: {self._id}
        Position: {self.position}
        Line: {self.line}
        Used In: {self.used_in}
        Modification Date: {self.moddate}
        Upload Date: {self.upldate}
        """)