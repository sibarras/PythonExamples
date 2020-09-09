import sqlite3
from sqlObject import Employee

class DB:
    def __init__(self, dbName:str):
        self.dbName = dbName
        conn = sqlite3.connect(db_name)


    def close(self):
        conn.close()
        
db_name  = 'employee.db'
employeeDB = DB()


conn.close()
# dirlist = os.listdir(sys.argv[0].rstrip('sqlite3.py'))

# print(dirlist)
# print(os.getcwd())

