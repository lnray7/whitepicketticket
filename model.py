from datetime import datetime
from db.sqa import db, connect_to_db

class Citation(db.Model):
    """A citation"""
    __tablename__ = "parking_citations"
    __table_args__ = {"extend_existing": True}

    citation_no = db.Column(db.Text, primary_key=True)
    citation_issued_at = db.Column(db.Text)
    violation_code = db.Column(db.Text)
    violation_desc = db.Column(db.Text)
    citation_location = db.Column(db.Text)
    fine_amount = db.Column(db.Float)
    date_added = db.Column(db.Date)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    def toDictionary(self):
        return {
            "citation_no": self.citation_no,
            "citation_issued_at": self.citation_issued_at,
            "violation_code": self.violation_code,
            "citation_location": self.citation_location,
            "fine_amount": self.fine_amount,
            "date_added": self.date_added,
            "lat": self.lat,
            "lon": self.lon
        }


class Meter(db.Model):
    """A meter"""
    __tablename__ = "parking_meters"
    __table_args__ = {"extend_existing": True}

    post_id = db.Column(db.Text, primary_key=True)
    ms_pay_station_id = db.Column(db.Text)
    ms_space_num = db.Column(db.Integer)
    sensor_flag = db.Column(db.Text)
    is_on_street = db.Column(db.Boolean)
    offstreet_id = db.Column(db.Integer)
    jurisdiction = db.Column(db.Text)
    active_meter_flag = db.Column(db.Text)
    reason_code = db.Column(db.Text)
    is_smart_meter = db.Column(db.Boolean)
    is_multi_space = db.Column(db.Boolean)
    cap_color = db.Column(db.Text)
    old_rate_area = db.Column(db.Text)
    street_id = db.Column(db.Text)
    street_name = db.Column(db.Text)
    lon = db.Column(db.Float)
    lat = db.Column(db.Float)
    comments = db.Column(db.Text)
    collection_route = db.Column(db.Text)
    collection_subroute = db.Column(db.Text)
    pmr_route = db.Column(db.Text)
    nfc_key = db.Column(db.Text)
    spt_code = db.Column(db.Text)

    def toDictionary(self):
        return {
            "post_id": self.post_id,
            "ms_pay_station_id": self.ms_pay_station_id,
            "ms_space_num": self.ms_space_num,
            "sensor_flag": self.sensor_flag,
            "is_on_street": self.is_on_street,
            "offstreet_id": self.offstreet_id,
            "jurisdiction": self.jurisdiction,
            "active_meter_flag": self.active_meter_flag,
            "reason_code": self.reason_code,
            "is_smart_meter": self.is_smart_meter,
            "is_multi_space": self.is_multi_space,
            "cap_color": self.cap_color,
            "old_rate_area": self.old_rate_area,
            "street_id": self.street_id,
            "street_name": self.street_name,
            "lon": self.lon,
            "lat": self.lat,
            "comments": self.comments,
            "collection_route": self.collection_route,
            "collection_subroute": self.collection_subroute,
            "pmr_route": self.pmr_route,
            "nfc_key": self.nfc_key,
            "spt_code": self.spt_code
        }



#class User(db.Model):
   # __tablename__ = 'users'

   # id = db.Column(db.Integer, primary_key=True)
   # name = db.Column(db.String(50))
   # email = db.Column(db.String(50))
   # password = db.Column(db.String(50))

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    db.create_all()