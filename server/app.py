from flask import Flask, jsonify, request
from flask_cors import CORS

#Importing files that I made: 
# from support import *
# from data import *
# from db import *

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')



if __name__ == '__main__':
    app.run(debug=True)
