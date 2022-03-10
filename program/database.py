import pyodbc

class Database:
    __connection = None

    @classmethod
    def connect(cls):
        if cls.__connection is None:
            server = 'tcp:cisdbss.pcc.edu'
            database = 'NAMES'
            username = '275student'
            password = '275student'
            cls.__connection = pyodbc.connect(
                'DRIVER={SQL Server};SERVER=' + server
                + ';DATABASE=' + database
                + ';UID=' + username + ';PWD=' + password
            )

    #The two parameters passed into readNames should be used in a WHERE clause
    #in the SQL inquiry.
    #The WHERE clause should filter the data   and you should use
    # parameter binding in your query to guard against SQL injection attacks.
    # Regardless of the parameters you choose, you should return a list of Name objects
    # with all the properties filled in (Name, Year, NameCount and Gender)

    @classmethod
    def readNames(cls, name, gender):
        cls.connect()
        cursor = cls.__connection.cursor()
        sql = """
        SELECT Name, Year, Gender, NameCount
        FROM all_data
        WHERE Name = ?
        AND Gender = ?
        ORDER by Name DESC;
        """
        cursor.execute(sql, name, gender)
        rows = cursor.fetchall()
        return rows

