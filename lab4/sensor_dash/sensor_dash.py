# sensor_dash/sensore_dash.py
from flask import Flask, render_template, g, request, redirect

import os
from sqlite3 import dbapi2 as sqlite3
##Own custom files
from dbhandler import connect_db, get_db, init_db


##### APP SETUP #####
app = Flask(__name__)


    
##### DB SETUP #####
db_name = 'sensor_dash.db'


##DATABASE STUFF##
# Setup the database credentials
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, db_name),
    DEBUG=True,
    #SECRET_KEY=b'<SOME HEXADECIMAL SECRET KEY>',
    USERNAME='admin',
    PASSWORD='pass'
))    
    
# Command to create the database via command line
# You call it from command line: flask initdb
@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')

# Close the database when the request ends
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

         
        
        
##### ROUTES #####
@app.route('/') #main dashboard
def dashboard_view():
    return render_template('lab3_page.html') #change to dashboard

@app.route('/temp_humidity')
def temp_hum_view():
    return render_template('temp_hum_sensor.html')

@app.route('/light')
def light_view():
    return render_template('light_sensor.html')

@app.route('/sound')
def sound_view():
    return render_template('sound_sensor.html')



