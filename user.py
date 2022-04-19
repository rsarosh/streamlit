# pip  install mysql-connector-python
import mysql.connector
from configparser import ConfigParser
cnx: mysql.connector.connect = None

def login (userName: str, password: str) -> bool:
    args = [userName, password, 0]
    result_args = executeSQLQuery ("CheckUser", args)
    # returns => ('admin', 'admin', 1)
    if (result_args[2] == 1):
        return True
    else:
        return False;
    
def executeSQLQuery(query, args):
    global cnx;
    if (cnx == None):
        config = ConfigParser()
        config.read("config.ini")
        _host = config.get('MySQL', 'host')
        _port = config.get('MySQL', 'port')
        _database = config.get('MySQL', 'database')
        _user = config.get('MySQL', 'user')
        _password = config.get('MySQL', 'password')
        cnx = mysql.connector.connect(host=_host, database=_database, 
                                    user=_user, passwd=_password, port=_port)
    
    with cnx.cursor() as cur:  
        return cur.callproc(query, args)
        