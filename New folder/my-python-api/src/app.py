from flask import Flask
from routes import *

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Python API!"

if __name__ == '__main__':
    app.run(debug=True)