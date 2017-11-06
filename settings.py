SECRET_KEY = 'you-will-never-guess'
DEBUG = True

DB_HOST = 'jamesonhm.mysql.pythonanywhere-services.com'
DB_USERNAME = 'jamesonhm'
DB_PASSWORD = 'learnFlask1'
DB_NAME = 'jamesonhm$blog'
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
