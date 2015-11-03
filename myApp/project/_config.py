import os
#grab the folder where this script lives
basedir=os.path.abspath(os.path.dirname(__file__))
key=os.urandom(24)
DATABASE='flasktaskr.db'
#WTF_CSRF_ENABLED=True
CSRF_ENABLED=False
DEBUG=False
#SECRET_KEY='my_precious'
SECRET_KEY=key
DATABASE_PATH=os.path.join(basedir,DATABASE)
SQLALCHEMY_DATABASE_URI='sqlite:///'+DATABASE_PATH
