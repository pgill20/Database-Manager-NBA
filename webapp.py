from flask import Flask, render_template
from flask import request, redirect, url_for
from db_connector import connect_to_database, execute_query

# Please not that repeated steps will only be explained once and 
# the same description carries over to the preceding occurance of that same code

#Creates the web application
webapp = Flask(__name__)

# The Homepage contains links for viewing Teams, Players, 
# Head Coaches, Trainers, Stadiums and Players-Trainers relationships
@webapp.route('/')
def root():
    """The root directory for the entire website"""

    return render_template('index.html')

# Leads to the Teams page where all Teams are displayed, updated, deleted and 
# new ones can be created
@webapp.route('/teams')
def teams():
    """Views all the Teams and ability to add a new team"""

    # Connects to the OSU database by callnig a method from db_connector.py file
    db_connection = connect_to_database()

    # Executing query from the database to view the specified attributes
    query = "SELECT team_id, team_name, total_fines, salary_available, best_player FROM Teams;"

    # Fetching all the data from the query and adding it to a variable while being connected 
    # to the database first
    result = execute_query(db_connection, query).fetchall()

    # Calling the html file that needs all the resulting informating from the 
    # previous fetch function
    return render_template('teams.html', rows=result)

# Leads to the Add Teams page where new Teams can be created
@webapp.route('/add_team', methods=['POST','GET'])
def add_team():
    db_connection = connect_to_database()

    # If the underlying method is GET then this gets executed and displays current data
    if request.method == 'GET':
        query = 'SELECT player_id, last_name from Players;'
        result = execute_query(db_connection, query).fetchall()
        return render_template('add_team.html', players=result)
    
    # If the underlying method is POST then this gets executed and 
    # leads to a form that is used to add data to the Trainer table
    elif request.method == 'POST':

        # References the from element and links to a variable
        team_name = request.form['team_name']
        total_fines = request.form['total_fines']
        salary_available = request.form['salary_available'] 
        best_player = request.form['best_player']
        query = 'INSERT INTO Teams (team_name, total_fines, salary_available, best_player) VALUES (%s,%s,%s,%s);'

        # All the variable data is collected to be passed onto the /teams page
        data = (team_name, total_fines, salary_available, best_player)
        execute_query(db_connection, query, data)
        return redirect('/teams')

# Leads to the Update Teams page where the team chosen based on the id, can be updated 
@webapp.route('/update_team/<int:id>', methods=['POST','GET'])
def update_team(id):
    db_connection = connect_to_database()

    if request.method == 'GET':

        # THe following query is used to get the one row of data where the input id matches 
        # that of the data in the database
        team_query = 'SELECT team_id, team_name, total_fines, salary_available, best_player FROM Teams WHERE team_id = %s'  % (id)
        team_result = execute_query(db_connection, team_query).fetchone()

        # Results in an error if the input id is not found
        if team_result == None:
            return "No such team found!"

        players_query = 'SELECT player_id, last_name from Players'
        players_results = execute_query(db_connection, players_query).fetchall()

        print('Returning')
        return render_template('update_team.html', players = players_results, team = team_result)

    elif request.method == 'POST':
        print('The POST request')
        team_id = request.form['team_id']
        team_name = request.form['team_name']
        total_fines = request.form['total_fines']
        salary_available = request.form['salary_available']
        best_player = request.form['best_player']

        # Teams table is updated based on the new or updated input data from the user
        query = "UPDATE Teams SET team_name = %s, total_fines = %s, salary_available = %s, best_player = %s WHERE team_id = %s"
        data = (team_name, total_fines, salary_available, best_player, team_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/teams')

# Leads to the Delete Teams page where the team chosen based on the id, can be deleted 
@webapp.route('/delete_team/<int:id>')
def delete_team(id):
    db_connection = connect_to_database()
    query = "DELETE FROM Teams WHERE team_id = '%s';"
    data = (id,)
    execute_query(db_connection, query, data)

    # Redirects to the Teams page where all the Teams are displated
    return redirect(url_for('teams', success="Success!"))

# Leads to the Players page where all Players are displayed, deleted and 
# new ones can be created
@webapp.route('/players')
def players():
    db_connection = connect_to_database()
    query = "SELECT player_id, first_name, last_name, speciality, team, salary, height, weight, birthday, primary_position, secondary_position, fg, ft, ppg, rpg, apg, spg, bpg, tpg FROM Players;"
    result = execute_query(db_connection, query).fetchall()
    return render_template('players.html', rows=result)

# Leads to the Add Players page where new Players can be created
@webapp.route('/add_player', methods=['POST','GET'])
def add_player():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'SELECT team_id, team_name from Teams;'
        result = execute_query(db_connection, query).fetchall()
        return render_template('add_player.html', teams=result)
    
    elif request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        speciality = request.form['speciality']
        team = request.form['team']
        salary = request.form['salary']
        height = request.form['height']
        weight = request.form['weight']
        birthday = request.form['birthday']
        primary_position = request.form['primary_position']
        secondary_position = request.form['secondary_position']
        fg = request.form['fg']
        ft = request.form['ft']
        ppg = request.form['ppg']
        rpg = request.form['rpg']
        apg = request.form['apg']
        spg = request.form['spg']
        bpg = request.form['bpg']
        tpg = request.form['tpg']
        query = "INSERT INTO Players (first_name, last_name, speciality, team, salary, height, weight, birthday, primary_position, secondary_position, fg, ft, ppg, rpg, apg, spg, bpg, tpg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        data = (first_name, last_name, speciality, team, salary, height, weight, birthday, primary_position, secondary_position, fg, ft, ppg, rpg, apg, spg, bpg, tpg)
        execute_query(db_connection, query, data)
        return redirect('/players')

# Leads to the Delete Playeres page where the player chosen based on the id, can be deleted 
@webapp.route('/delete_player/<int:id>')
def delete_player(id):
    db_connection = connect_to_database()
    query = "DELETE FROM Players WHERE player_id = '%s';"
    data = (id,)
    execute_query(db_connection, query, data)
    return redirect(url_for('players', success="Success!"))

# Leads to the Coaches page where all Coaches are displayed and 
# new ones can be created
@webapp.route('/coaches')
def coaches():
    db_connection = connect_to_database()
    query = "SELECT coach_id, first_name, last_name, team FROM Head_Coaches;"
    result = execute_query(db_connection, query).fetchall()
    return render_template('coaches.html', rows=result)

# Leads to the Add Coaches page where new Head Coaches can be created
@webapp.route('/add_coach', methods=['POST','GET'])
def add_coach():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'SELECT team_id, team_name from Teams;'
        result = execute_query(db_connection, query).fetchall()
        return render_template('add_coach.html', teams=result)
    
    elif request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        team = request.form['team']
        query = 'INSERT INTO Head_Coaches (first_name, last_name, team) VALUES (%s,%s,%s);'
        data = (first_name, last_name, team)
        execute_query(db_connection, query, data)
        return redirect('/coaches')

# Leads to the Trainers page where all Trainers are displayed and 
# new ones can be created
@webapp.route('/trainers')
def trainers():
    db_connection = connect_to_database()
    query = "SELECT trainer_id, first_name, last_name, speciality FROM Trainers;"
    result = execute_query(db_connection, query).fetchall()
    return render_template('trainers.html', rows=result)

# Leads to the Add Trainers page where new Trainers can be created
@webapp.route('/add_trainer', methods=['POST','GET'])
def add_trainer():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'SELECT team_id, team_name from Teams;'
        result = execute_query(db_connection, query).fetchall()
        return render_template('add_trainer.html')
    
    elif request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        speciality = request.form['speciality']
        query = 'INSERT INTO Trainers (first_name, last_name, speciality) VALUES (%s,%s,%s);'
        data = (first_name, last_name, speciality)
        execute_query(db_connection, query, data)
        return redirect('/trainers')

# Leads to the Stadiums page where all Stadiums are displayed and 
# new ones can be created
@webapp.route('/stadiums')
def stadiums():
    db_connection = connect_to_database()
    query = "SELECT stadium_id, stadium_name, city, team, state FROM Stadiums;"
    result = execute_query(db_connection, query).fetchall()
    return render_template('stadiums.html', rows=result)

# Leads to the Add Stadiums page where new Stadiums can be created
@webapp.route('/add_stadium', methods=['POST','GET'])
def add_stadium():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'SELECT team_id, team_name from Teams;'
        result = execute_query(db_connection, query).fetchall()
        return render_template('add_stadium.html', teams=result)
    
    elif request.method == 'POST':
        stadium_name = request.form['stadium_name']
        team = request.form['team']
        state = request.form['state']
        city = request.form['city']
        query = 'INSERT INTO Stadiums (stadium_name, city, team, state) VALUES (%s,%s,%s,%s);'
        data = (stadium_name, city, team, state)
        execute_query(db_connection, query, data)
        return redirect('/stadiums')

# This page is used to search for stadiums based on the input state by the user and is accessed by the 
# user from the /stadiums main page
@webapp.route('/show_stadiums', methods=['POST'])
def show_stadiums():
    db_connection = connect_to_database()

    # Only displays the stadium info where the input state name is equal to that of the in the database
    query = 'SELECT stadium_id, stadium_name, city, team, state FROM Stadiums WHERE state = %s; '
    data = (request.form['show_state'],)
    results = execute_query(db_connection, query, data).fetchall()
    return render_template('show_stadiums.html', show_stadiums=results)

# Leads to the Players-Trainers page where all Players-Trainers relationships are displayed based 
# on their respective last names, new relationships can be created and existing relationships 
# can be deleted 
@webapp.route('/players_trainers')
def players_trainers():
    db_connection = connect_to_database()
    query = 'SELECT player_rel_id, player_last_name, trainer_rel_id, trainer_last_name FROM Players_Trainers;'
    result = execute_query(db_connection, query).fetchall()
    return render_template('players_trainers.html', rows=result)

# Leads to the Add Players-Trainers page where new Players-Trainers can be created
@webapp.route('/add_players_trainers', methods=['POST','GET'])
def add_players_trainers():
    db_connection = connect_to_database()
    if request.method == 'GET':
        print('This is GET')

        # Two queries are created this time to get a dropdown of all the Players and Trainers 
        # currently present in the database
        query1 = 'SELECT player_id, last_name from Players;'
        query2 = 'SELECT trainer_id, last_name from Trainers;'
        result1 = execute_query(db_connection, query1).fetchall()
        result2 = execute_query(db_connection, query2).fetchall()
        return render_template('add_players_trainers.html', players=result1, trainers=result2)
    
    if request.method == 'POST':
        print('This is POST')
        player_id = request.form['player_id']
        trainer_id = request.form['trainer_id']

        # Only executing the query where the id for both player and trainer are already existing in the database
        query = '''INSERT INTO Players_Trainers (player_rel_id, player_last_name, trainer_rel_id, trainer_last_name) 
        VALUES (%s, (SELECT last_name FROM Players WHERE player_id=%s), %s, (SELECT last_name FROM Trainers WHERE trainer_id=%s));'''
        data = (player_id, player_id, trainer_id, trainer_id)
        execute_query(db_connection, query, data)
        return redirect('/players_trainers')

# Deleted Players-Trainers relationship from the button accessed on the /players_trainers page
@webapp.route('/delete_players_trainers/<int:player_id>/<int:trainer_id>')
def delete_players_trainers(player_id, trainer_id):
    db_connection = connect_to_database()

    # Only executing the query where the id for both player and trainer are already existing in the database
    query = "DELETE FROM Players_Trainers WHERE player_rel_id = '%s' AND trainer_rel_id = '%s';"
    data = (player_id, trainer_id)
    print(data)
    execute_query(db_connection, query, data)
    return redirect(url_for('players_trainers', success="Success!"))
