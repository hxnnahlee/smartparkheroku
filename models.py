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