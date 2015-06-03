# from Flask module import Flask

from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

# use decorators to link the function to a url

@app.route("/")

@app.route("/hello")

#define the view using a function that 
# returns a string

def hello_world():
	return("hello world 123")

@app.route("/test/<search_query>")
def search(search_query):
	return(search_query)

@app.route("/integer/<int:value>")
def int_type(value):
    print value + 1
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print value + 1
    return "correct"

# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
    print value
    return "correct"
# dynamic route with explicit status codes
@app.route("/name/<name>")
def  index(name):
    if name.lower() == "michael" :
        return "Hello, {}".format(name)
    else :
        return "Not Found", 404



# start the development server

if __name__ == "__main__":
	app.run()


