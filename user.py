# pip  install mysql-connector-python
import mysql.connector
from configparser import ConfigParser
from torch import _fake_quantize_per_tensor_affine_cachemask_tensor_qparams
CNX: mysql.connector.connect = None


def login(userName: str, password: str) -> bool:
    if (userName is None):
        return False
    args = [userName, password, 0]
    result_args = execute_sql_query("CheckUser", args)
    return (result_args[2] == 1)

def execute_sql_query(query, args):
    global CNX
    if (CNX is None):
        config = ConfigParser()
        config. read("config.ini")
        _host = config.get('MySQL', 'host')
        _port = config.get('MySQL', 'port')
        _database = config.get('MySQL', 'database')
        _user = config.get('MySQL', 'user')
        _password = config.get('MySQL', 'password')
        CNX = mysql.connector.connect(host=_host, database=_database,
                                      user=_user, passwd=_password, port=_port)
    
    CNX.commit()
    
    with CNX.cursor() as cur:
        return cur.callproc(query, args)
