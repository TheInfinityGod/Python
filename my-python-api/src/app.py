from flask import Flask
from routes import *
from handler import Handler  # Import the handler class

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Python API!"

@app.route('/add')
def add():
    result = 2 + 4
    return f"The result of 2 + 4 is {result}"

@app.route('/process')
def process():
    handler = Handler()       # Create an instance of the handler class
    result = handler.process()  # Call the process method
    return f"Handler returned: {result}"

if __name__ == '__main__':
    app.run(debug=True)