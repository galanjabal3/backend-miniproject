from pony.orm import *
from config import config


# def db():
#     db = Database()
#     db.bind(config.driverDB, host=config.hostDB, user=config.userDB, passwd=config.passwordDB, db=config.dbName)
    
#     sql_debug(config.dbDebug)
#     return db

db2 = Database()
db2.bind(config.driverDB, host=config.hostDB, user=config.userDB, password=config.passwordDB, database=config.dbName)
sql_debug(config.dbDebug)