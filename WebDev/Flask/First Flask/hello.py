from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return '<b>' + function() + '</b>'
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return '<em>' + function() + '</em>'
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return '<u>' + function() + '</u>'
    return wrapper_function

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello world</h1>'

#variable route example
@app.route("/username/<name>/<int:age>")
def greet(name, age):
    return f"hello {name} you are {age} years old!"

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return '<p>Bye</p>'

#automatically start flask and run the webapp when you run the app
if __name__ == "__main__":
    #run the app in debug mode
    app.run(debug=True)