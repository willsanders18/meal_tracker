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
        
    def executeSqlWithParam(self, query:str, params:list):
        with self._getConnection() as con:
            cur: sqlite3.Cursor = con.cursor()
            cur.execute(query, params)
            con.commit()

    def executeSqlFromFileWithParam(self, filename:str, params:list):
        s = self._getSqlFromFile(filename)
        self.executeSqlWithParam(s, params)

    def queryToList(self, query:str) -> list[list]:
        with self._getConnection() as con:
            cur: sqlite3.Cursor = con.cursor()
            return cur.execute(query).fetchall()

    def queryToVal(self, query:str, dtype:type=str) -> str|int|bool|float:    
        if dtype not in [str, int, float, bool]:
            raise ValueError('Specified type is invalid')

        with self._getConnection() as con:
            cur: sqlite3.Cursor = con.cursor()
            return dtype(cur.execute(query).fetchall()[0][0])
        
    def queryToValWithParam(self, query:str, params:list, dtype:type=str) -> str|int|bool|float:
        if dtype not in [str, int, float, bool]:
            raise ValueError('Specified type is invalid')

        with self._getConnection() as con:
            cur: sqlite3.Cursor = con.cursor()
            return dtype(cur.execute(query, params).fetchall()[0][0])

    def queryToDict(self, query:str) -> list[dict]:
        with self._getConnection() as con:
            con.row_factory = sqlite3.Row
            cur: sqlite3.Cursor = con.cursor()
            return [dict(row) for row in cur.execute(query).fetchall()]
