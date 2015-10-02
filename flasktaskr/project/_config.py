import os
#grab the folder where this script lives
#basedir=os.path.abspath(os.path dirname(/home/jeanne/Documents/RealPython2/real_python_test/flasktaskr/project)
basedir=os.path.abspath(os.path.dirname(__file__))
key=os.urandom(24)
DATABASE='flasktaskr.db'
USERNAME='admin'
PASSWORD='admin'
WTF_CSRF_ENABLED=True
#SECRET_KEY='my_precious'
SECRET_KEY=key
DATABASE_PATH=os.path.join(basedir,DATABASE)
