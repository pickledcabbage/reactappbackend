from flask import Flask
from modules.api_world import api_world
import json

app = Flask(__name__)

@app.route('/world')
def index():
    #Check if HTTP JSON is valid format
    #Maybe convert to python object

    #Do something here VVV
    return json.dumps(api_world("something"))

@app.route('/home')
def second_index():
    return "brave new home!"

if __name__ == '__main__':
    app.run(debug=True)