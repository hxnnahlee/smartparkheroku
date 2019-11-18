from backend import db
from sqlalchemy.dialects.postgresql import JSON


class Spot(db.Model):
    __tablename__ = 'spots'

    spot_id = db.Column(db.Integer, primary_key=True)
    taken = db.Column(db.Integer)

    def __init__(self, spot_id, taken):
        self.spot_id = spot_id
        self.taken = taken

    def __repr__(self):
        return '<id {}'.format(self.id)

    def serialize(self):
        return {
            'spot id': self.spot_id,
            'taken': self.taken
        }

class TimestampChange(db.Model):
    __tablename__ = 'timestampchange'

    spot_detail_id = db.Column(db.Integer,primary_key=True)
    spot_id = db.Column(db.Integer)
    timestamp = db.Column(db.String())
    state = db.Column(db.Integer)

    def __init__(self, spot_detail_id, spot_id, timestamp, state):
        self.spot_detail_id = spot_detail_id
        self.spot_id = spot_id
        self.timestamp = timestamp
        self.state = state

    def __repr__(self):
        return '<id {}'.format(self.id)

    def serialize(self):
        return {
            'spot detail id': self.spot_detail_id,
            'spot id': self.spot_id,
            'timestamp': self.timestamp,
            'state': self.state
        }

class Average(db.Model):
    __tablename__ = 'average'

    avg = db.Column(db.Float, primary_key=True)

    def __init__(self, avg):
        self.avg = avg

    def __repr__(self):
        return '<id {}'.format(self.id)
    
    def serialize(self):
        return {
            'average': self.avg
        }


