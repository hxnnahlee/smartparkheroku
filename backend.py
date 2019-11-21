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
        #json = jsonify(spot_info.serialize())
        print(spot_info.taken)
        if spot_info.taken == "1" or spot_info.taken == 1:
            print("in taken")
            now = datetime.datetime.now()
            exists = TimestampChange.query.filter_by(spot_detail_id=spot+"1").first()
            as_date = datetime.datetime.strptime(exists.timestamp, '%m/%d/%Y, %H:%M:%S')

            difference = now - as_date
            difference = difference.seconds / 60
            print("differencE:")

            print(difference)
            aver = Average.query.limit(15).all()
            sum = 0
            count = 0
            for i in aver:
                sum = sum + i.time_parked
                count = count + 1
            avg = sum/count
            print(avg)
            perc = (difference*100)/avg
            print(perc)
            return str(perc)
        else:
             return "0"
        #return "spot: " + spot + " will add taken from DB"
    except Exception as e:
        return(str(e))
    

    #for now we only have 1 table alumnimemorial, in the future when we have more garages it will not be hardcoded into sqlquery 


# POST
# Test route used to see if the DB was working
@app.route('/spotstest', methods = ['POST'])
def test_post():
    to_string = request.data.decode("utf-8")
    print(to_string + " in test")

    try:
        timestamp = TimestampChange(
            spot_detail_id = "2211",
            spot_id = "221",
            timestamp = "11/19/2019, 11:31:54",
            state = "0"
        )
        exists = TimestampChange.query.filter_by(spot_detail_id="2210").first()
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

    to_string = request.data.decode("utf-8")

    # Body of POST is in this format: spot_id taken
    tokens = to_string.split(" ")
    spot_id = tokens[0]
    taken = tokens[1] 
    print(tokens)
    if len(tokens) == 3:
        median = tokens[2]
        if median is not None:
            print("median: ")
            print(median)

    # Time to string, we'll store the date as a string in our DB
    now = datetime.datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    try:
        print("spot id")
        print(spot_id)
        print("taken")
        print(taken)
        spot=Spot(
            spot_id=spot_id,
            taken=taken
        )
        exists = Spot.query.filter_by(spot_id=spot_id).first()
        # Check case if the spot with that ID already exists in the database 
        if exists is not None:
 
            taken = int(taken)
            # Change in state, update timestamp
            if exists.taken != taken:
                taken = str(taken)
                print("Change in state")
                exists.taken = taken
                timestamp = TimestampChange(
                    spot_detail_id = spot_id+taken,
                    spot_id = spot_id,
                    timestamp = date_time,
                    state = taken
                )

                timeExists = TimestampChange.query.filter_by(spot_detail_id=timestamp.spot_detail_id).first()
            
                if timeExists is not None:
                    timeExists.timestamp = date_time
                else:
                    db.session.add(timestamp)
                db.session.commit()

                # If 1/0 statements here -- TO DO
                if taken == "0":
                    print("update average")
                    time = TimestampChange.query.filter_by(spot_detail_id=timestamp.spot_id+"1").first()
                    as_date = datetime.datetime.strptime(time.timestamp, '%m/%d/%Y, %H:%M:%S')
                    difference = now - as_date 
                    difference = difference.seconds / 60
   
                    hist = Average(
                        time_parked = difference,
                        timestamp = date_time,
                        spot_id=spot_id
                    )
                    db.session.add(hist)
                    db.session.commit()
                    

            # Set taken to taken if spot with that ID exists
            taken = str(taken)

            exists.taken = taken

        # If spot does not already exist, create in the database
        else:
            db.session.add(spot)
        db.session.commit()
        return "Spot updated. spot id= "+spot_id+" taken= "+taken
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
