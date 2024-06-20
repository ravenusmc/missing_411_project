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
        requested_data_container = {}
        data = EXAMINECSV()
        post_data = request.get_json()
        genres = post_data['selectedGenres']
        year = 1996
        merged_df = data.get_average_game_ratings_by_year_and_selected_genres(genres)
        year_and_critic_ratings = data.build_data_from_merged_df(genres, merged_df)
    return jsonify(year_and_critic_ratings)



if __name__ == '__main__':
    app.run(debug=True)
