
import sqlite3

class PipelineSQL:

    def __init__(self):
        self.connected = False

    def ConnectToDB(self, path):
        self.connection = sqlite3.connect(path)
        self.connected = True
        self.cursor = self.connection.cursor()
        
    def ExecuteSQL(self, SQLCommand):
        self.cursor.execute(SQLCommand)
        self.SaveSQL()
                
    def LoadFromSQLFile(self, filepath):
        sql_file = open(filepath)
        sql_as_string = sql_file.read()
        self.cursor.executescript(sql_as_string)
        self.connection.commit()
        
    
    def SaveSQL(self):
        self.connection.commit()
    


        
        
        

