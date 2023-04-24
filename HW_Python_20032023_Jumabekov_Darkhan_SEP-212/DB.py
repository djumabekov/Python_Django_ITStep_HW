import sqlite3
import sqlite3.dbapi2

from Product import Product


class DB(object):
    __conn: sqlite3.Connection
    __cursor: sqlite3.Cursor

    def __init__(self, db_name):
        try:
            self.__conn = sqlite3.connect(f'{db_name}.sqlite3')
            self.__cursor = self.__conn.cursor()
            self.__create_table()
        except sqlite3.DatabaseError as e:
            print('Exception: ', e)

    def __create_table(self):

        sql = '''
            CREATE TABLE if not exists Products
            (
              Id             INTEGER   primary key autoincrement  NOT NULL,
              Name           VARCHAR(30) NOT NULL,
              Manufacturer   VARCHAR(30) NOT NULL,
              Price          DECIMAL(2)  DEFAULT(1),
              Count          INT         DEFAULT(1),
              Description    VARCHAR(30)
            );
            CREATE UNIQUE INDEX if not exists IdxProducts ON Products (Id);
            '''
        params = ()
        return self.__sql_execute(sql, params)

    def insert(self, product: Product):

        sql = "INSERT INTO Products (Name, Manufacturer, Price, Count, Description)\
                        VALUES(?, ?, ?, ?, ?);"
        params = (product.name, product.manufacturer, \
                  product.price, product.count, product.description)
        return self.__sql_execute(sql, params)

    def __sql_execute(self, sql, params) -> list:
        try:
            with self.__conn:
                if sql.__contains__('CREATE'):
                    self.__cursor.executescript(sql)
                    self.__conn.commit()
                else:
                    self.__cursor.execute(sql, params)
                    self.__conn.commit()
                    data = self.__cursor.fetchall()
                    return data
        except sqlite3.DatabaseError as e:
            print('Exception: ', e)
            self.__conn.rollback()
            return None
        except sqlite3.DataError as e:
            print('Exception: ', e)
            self.__conn.rollback()
            return None

    def getProductsByPrice(self, from_price: float, to_price: float) -> list:
        sql = "SELECT * FROM Products WHERE Price BETWEEN ? AND ?;"
        params = (from_price, to_price)
        return self.__sql_execute(sql, params)

    def getProductByParam(self, param: str, column: str) -> list:
        sql = f"SELECT * FROM Products WHERE {column} LIKE ?;"
        params = (f'%{param}%',)
        return self.__sql_execute(sql, params)

    def sortProductsByParam(self, param: str) -> list:
        sql = f"SELECT * FROM Products ORDER BY {param} ASC;"
        params = ()
        return self.__sql_execute(sql, params)

    def delete(self, id: int):
        sql = "DELETE FROM Products WHERE id=?;"
        params = (id,)
        return self.__sql_execute(sql, params)

    def readOne(self, product: Product):
        sql = "SELECT * FROM Products WHERE Name=? AND Manufacturer=? AND Price=? AND Count=? AND Description=?;"
        params = (product.name, product.manufacturer, product.price, product.count, product.description)
        return self.__sql_execute(sql, params)

    def readAll(self):
        sql = "SELECT * FROM Products;"
        params = ()
        return self.__sql_execute(sql, params)

    def getById(self, id):
        sql = "SELECT * FROM Products WHERE Id=?;"
        params = (id,)
        return self.__sql_execute(sql, params)
