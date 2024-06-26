from flask import Flask, jsonify, request
from flask_cors import CORS

#Importing files that I made: 
from data import *
# from support import *
# from db import *

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        hashed = db.encrypt_pass(post_data)
        user_created = db.insert(post_data, hashed)
        return jsonify('5')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        email = post_data['email']
        password = post_data['password']
        login_values = {}
        # Checking to see if the user is in the database
        login_flag, not_found, password_no_match, user = db.verify_user(
            email, password)
        login_values['login_flag'] = login_flag
        login_values['Not_found'] = not_found
        login_values['Password_no_match'] = password_no_match
        login_values['user'] = user
    return jsonify(login_values)

@app.route('/buildMap', methods=['GET', 'POST'])
def buildGenreGraph():
    if request.method == 'POST':
        data = ExamineCSV()
        post_data = request.get_json()
        year = int(post_data['year'])
        mapdata = data.get_missing_by_year_for_map(year)
    return jsonify(mapdata)

@app.route('/getCoastData', methods=['GET', 'POST'])
def getCoastData():
    if request.method == 'POST':
        data = ExamineCSV()
        post_data = request.get_json()
        coast = post_data['payload']['coast']
        people_by_coast_data = data.get_data_for_one_coast_for_drilldown(coast)
        return jsonify(people_by_coast_data)

if __name__ == '__main__':
    app.run(debug=True)
