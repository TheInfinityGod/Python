from flask import Flask
from routes import *

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Python API!"

@app.route('/add')
def add():
    result = 2 + 4
    return f"The result of 2 + 4 is {result}"

if __name__ == '__main__':
    app.run(debug=True)