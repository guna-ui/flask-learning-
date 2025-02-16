from flask import Flask,url_for,request

app = Flask(__name__)

@app.route('/')
def Hello_world():
    return "Hello World"

@app.route('/about')
def about():
    return "This is about Page"

@app.route('/contact')
def contact():
    return "Contact Us"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/greet/<name>/<int:age>')
def greet_age(name,age):
    return f"Hello {name} and your age is {age}"

if __name__ == '__main__':
    app.run(debug=True)
