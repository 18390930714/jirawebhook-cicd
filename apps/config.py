DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = '***'
PASSWORD = '***'
HOST = '*.*.*.*'
PORT = '3306'
DATABASE = 'cases'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)