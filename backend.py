#from flaskext.mysql import MySQL
from flask import Flask, request, jsonify
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
    """
    :param spot number:
    :return: 0 if not taken, 1 if taken
    connect to mysql, query the spot,
    return the taken value
    """
    try:
        spot_info=Spot.query.filter_by(spot_id=spot).first()
        return jsonify(spot_info.serialize())
        #return "spot: " + spot + " will add taken from DB"
    except Exception as e:
        return(str(e))
    

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

    #Request in this format: spot_id taken
    tokens = to_string.split(" ")
    spot_id = tokens[0]
    taken = tokens[1]

    try:
        spot=Spot(
            spot_id=spot_id,
            taken=taken
        )
        db.session.add(spot)
        db.session.commit()
        return "Spot updated. spot id={}".format(spot.spot_id)
        return jsonify(spot.serialize())
    except Exception as e:
        return(str(e))



    return to_string

#if __name__ == "__main__":
#    app.run()
#testing purposes

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

## server on http://0.0.0.0:5000/
## visible across the network
## BaseUrl for Android http://<your ip address>:5000/spots/<spots>
