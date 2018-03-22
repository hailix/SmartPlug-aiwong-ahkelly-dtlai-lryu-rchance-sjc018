# sensor_dash/sensore_dash.py
from flask import Flask, render_template, g, request, redirect, jsonify

import os
from sqlite3 import dbapi2 as sqlite3
##Own custom files
# from dbhandler import connect_db, get_db, init_db


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
# Connect to the DB
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

# Wrap the helper function so we only open the DB once
def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

# Create the database (we do this via command line!!!)
def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

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
    #return render_template('lab3_page.html') #change to dashboard
    db = get_db()
    cur = db.execute('SELECT * from DHT')
    info = cur.fetchall()
    return render_template('temp_hum_sensor.html', entries=info)

@app.route('/temp_humidity', methods=["GET"])
def temp_hum_view():
    # db = get_db()
    # cur = db.execute('SELECT * from DHT')
    # info = cur.fetchall()
    return render_template('temp_hum_sensor.html')#, entries=info)

# @app.route('/sensor/<name>', methods=["GET"])
# def getDataRoute(name):
#     db = get_db()
#     cur = db.execute("SELECT * from "+name)
#     info = cur.fetchall()
#     print(info[0])
#     #print(info)
#     output = []

#     # NEED JSON OF COUNT # OF ELEMENTS
#     '''if(name == 'MCP'):
#       for value in range(count):
#         output.append( jsonify(voltage = info[0][value]))
#     '''
#     return jsonify(voltage=info[0][0])
'''
@app.route('/sound')
def sound_view():
    db = get_db()
    cur = db.execute('SELECT * from SS')
    info = cur.fetchall()
    # if len(info) == 0:
    #     raise NameError("wrongSize")
    return render_template('sound_sensor.html', entries=info)
'''
@app.route('/sensor/<sensor>', methods=["GET"])
def getData(sensor):
    output=[]
    db = get_db()
    cur=db.execute("SELECT * from " +sensor)
    info = cur.fetchall()

    tmp=0

    c = request.args['count']

    print(c)
    for item in info:
        while (tmp<int(c)):
                if (sensor == 'MCP'):
                    sensorDict = {
                            'voltage':item[0]}
                    #output.append(jsonify(sensorDict))
                    tmp=tmp+1
                if (sensor== 'DHT'):
                    sensorDict = {
                            'celsius':item[0],
                            'fahrenheit':item[1],
                            'humidity':item[2]}
                    #tmpj = jsonify(celsius=item[0], fahrenheit=item[1], humiditty=item[2])
                    #output.append(tmpj)
                    output.append(sensorDict)
                    #output.append(jsonify(celsius=item[0], fahrenheit=item[1],  humidity=item[2]))
                    tmp=tmp+1
                if (sensor=='SS'):
                    sensorDict = {
                            'gate':item[0],
                            'envelope':item[1],
                            'audio':item[2]}
                    output.append(sensorDict)
                    tmp=tmp+1
    return jsonify(tmp=output)


