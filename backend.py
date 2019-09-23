#from flaskext.mysql import MySQL
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Spot
migrate = Migrate(app, db)


    
# root
@app.route("/")
def index():
    """
    this is a root dir of my server
    :return: str
    """
    return "SMARTPARK!!!!!"

# GET
@app.route('/spots/<spot>', methods = ['GET'])
def spot_taken(spot):
#   cursor = conn.cursor()
    """
    :param spot number:
    :return: 0 if not taken, 1 if taken
    connect to mysql, query the spot,
    return the taken value
    """

    return spot

    #for now we only have 1 table alumnimemorial, in the future when we have more garages it will not be hardcoded into sqlquery 
#    cursor.execute('select taken from alumnimemorial where ID = ' +spot)
#    conn.commit()
#    val = cursor.fetchone()
#    cursor.close()


@app.route('/spots', methods = ['POST'])
def post_spot():

    #We can use this to parse, update database
    to_string = request.data.decode("utf-8")
    print(to_string + "Post data")

    return to_string

#if __name__ == "__main__":
#    app.run()
#testing purposes

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

## server on http://0.0.0.0:5000/
## visible across the network
## BaseUrl for Android http://<your ip address>:5000/spots/<spots>
