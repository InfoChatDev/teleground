from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Teleground"

app.run('0.0.0.0',8000,True)