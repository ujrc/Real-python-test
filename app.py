from flask import Flask
app=Flask(__name__)

app.config["DEBUG"]=True
@app.route("/")
@app.route("/hello")

def hello_world():
	return "Hello World !?!?!?!"

@app.route("/test/<search_query>")

def search(search_query):
	#return"Hello"
	return search_query

@app.route("/integer/<int:value>")

def int_type(value):
	print value+1
	return "correct"

@app.route("/float/<float:value>")
def float_type(value):
	print value+1
	return"correct"

@app.route("/name/<name>")
def index(name):
	if name.lower()=="micheal":
		#return " {}".format(name),200
		return " {}".format(name)
	else:
		return "Not found",404 

@app.route("/path/<path:value>")
def path_type(value):
	return value
		

if __name__=="__main__":
	app.run()