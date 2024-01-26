"""CRUD operations"""
from model import db, Citation, Meter

def get_citations():
    """Return all citations"""
    return Citation.query.all()

def get_citation_by_location(citation_location):
    """Return a citation by location"""
    return Citation.query.get(citation_location)

def get_citation_by_date(date_added):
    """Return a citation by date"""
    return Citation.query.get(date_added)

def get_meter():
    """Return all meters"""
    return Meter.query.all()

def get_meter_by_location(lat, lon):
    """Return meter by location"""
    # meter_location = meter_location(lat=lat, lon=lon)
    
    # return meter_location

