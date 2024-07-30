from flask import Flask, jsonify, request
from flask_cors import CORS

# Importing files that I made:
from data import *
from db import *


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# route to set up new user
@app.route('/setUpUser', methods=['GET', 'POST'])
def setUpUser():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        hashed = db.encrypt_pass(post_data)
        user_created = db.insert(post_data, hashed)
        return jsonify('5')

# Route to login in new user
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

# Route to build the map 
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


@app.route('/getTopFiveData', methods=['GET', 'POST'])
def getTopFiveData():
    if request.method == 'POST':
        data = ExamineCSV()
        post_data = request.get_json()
        state = post_data['payload']['state']
        state_data = data.get_data_by_state_for_drilldown(state)
        return jsonify(state_data)


@app.route('/getDecadeDrillDown', methods=['GET', 'POST'])
def getDecadeDrillDown():
    if request.method == 'POST':
        data = ExamineCSV()
        post_data = request.get_json()
        decade = post_data['payload']['decade']
        decade_data = data.get_data_by_decade_for_drilldown(decade)
        return jsonify(decade_data)


@app.route('/getAgeDrillDown', methods=['GET', 'POST'])
def getAgeDrillDown():
    if request.method == 'POST':
        data = ExamineCSV()
        post_data = request.get_json()
        age = post_data['payload']['age']
        age_data = data.get_data_by_age_for_drilldown(age)
        return jsonify(age_data)


@app.route('/getSexDrillDown', methods=['GET', 'POST'])
def getSexDrillDown():
    if request.method == 'POST':
        data = ExamineCSV()
        post_data = request.get_json()
        sex = post_data['payload']['sex']
        sex_data = data.get_data_by_sex_for_drilldown(sex)
        return jsonify(sex_data)
    
@app.route('/getMapDrillDown', methods=['GET', 'POST'])
def getMapDrillDown():
    if request.method == 'POST':
        data = ExamineCSV()
        post_data = request.get_json()
        state = post_data['payload']['state']
        state_data = data.get_data_by_state_for_drilldown(state)
        return jsonify(state_data)

if __name__ == '__main__':
    app.run(debug=True)
