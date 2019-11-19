#from flaskext.mysql import MySQL
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import datetime
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Spot, TimestampChange, Average
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


# POST
@app.route('/spotstest', methods = ['POST'])
def test_post():
    to_string = request.data.decode("utf-8")
    print(to_string + " in test")

    try:
        timestamp = TimestampChange(
            spot_detail_id = "2210",
            spot_id = "221",
            timestamp = "11/18/2019, 16:21:54",
            state = "0"
        )
        exists = TimestampChange.query.filter_by(spot_detail_id=spot_detail_id).first()
        if exists is not None:
            exists.taken = spot_taken

        else:
            db.session.add(timestamp)
        db.session.commit()

        return "i think this worked"
    except Exception as e:
        return(str(e))

    return to_string

# POST
@app.route('/spots', methods = ['POST'])
def post_spot():

    #We can use this to parse, update database
    to_string = request.data.decode("utf-8")
    print(to_string)

    #Request in this format: spot_id taken
    tokens = to_string.split(" ")
    spot_id = tokens[0]
    taken = tokens[1] 

    try:

        spot=Spot(
            spot_id=spot_id,
            taken=taken
        )
        exists = Spot.query.filter_by(spot_id=spot_id).first()

        if exists is not None:

            # Update timestamp table
            #if exists.taken != taken



            # Set taken to taken if spot with that ID exists
            exists.taken = taken
        else:
            db.session.add(spot)
        db.session.commit()
        #return "Spot updated. spot id={}".format(spot.spot_id)
        return "Spot updated. spot id= "+spot_id+" taken= "+taken
        #return jsonify(spot.serialize())
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
