import sqlite3
import os

class SqliteUtil:
    def __init__(self, dbpath:str='db/mealtracker.db', sqlpath:str='sql/') -> None:
        self.dbpath = dbpath
        self.sqlpath = sqlpath

        self._checkInit()
    
    def _checkInit(self):
        if not os.path.exists(self.dbpath):
            raise FileExistsError
        if not os.path.exists(self.sqlpath):
            raise FileExistsError

    def _getConnection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.dbpath)
    
    def _executeAnySql(self, sql:str):
        with self._getConnection() as con:
            cur: sqlite3.Cursor = con.cursor()
            cur.execute(sql)
            con.commit()

    def _getSqlFromFile(self, filename:str):
        """
        - check if file name exists in configured sql directory
        - if exists, return the contents of the file as a string
        - if not exists, raise an error
        """
        filepath = self.sqlpath + filename + '.sql'
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return f.read()
        else:
            raise FileNotFoundError(f'{filepath} not found in sql')
        
    def executeSqlFromFile(self, filename):
        s = self._getSqlFromFile(filename)
        self._executeAnySql(s)
        
