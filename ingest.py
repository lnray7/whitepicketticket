import csv
from flask_sqlalchemy import SQLAlchemy
from model import Citation, Meter
import db.sqa as sqa
from server import app
from datetime import datetime
NOW = datetime.now()
format_datetime = "%m/%d/%Y %I:%M:%S %p"


def safe_int(v):
    return None if v is None else int(v)


def handle_parse(filename, parse_func):
    results = []
    with open(filename) as f:
        reader = csv.DictReader(f)
        for base_row in reader:
            row = { k: None if base_row[k] in ['', '-'] else base_row[k] for k in base_row }
            parsed = parse_func(row)
            if parsed is not None:
                results.append(parsed)
    return results


def parse_citations(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        i = 0
        citations = []
        for base_row in reader:
            i+=1
            row = { k: None if base_row[k] in ['', '-'] else base_row[k] for k in base_row }
            if row['geom'] is None:
                continue
            datetime_string = base_row["Citation Issued DateTime"]
            row_datetime = datetime.strptime(datetime_string, format_datetime)
            date_difference = NOW - row_datetime
            if date_difference.days >= 365:
                print(datetime_string, date_difference)
                continue
            coords = row['geom']\
                .replace('POINT (', '')\
                .replace(')', '')\
                .split(' ')
            parsed = {
                'citation_no': row['Citation Number'],
                'citation_issued_at': row['Citation Issued DateTime'],
                'violation_code': row['Violation'],
                'violation_desc': row['Violation Description'],
                'citation_location': row['Citation Location'],
                'fine_amount': row['Fine Amount'],
                'date_added': row['Date Added'],
                'lat': float(coords[1]),
                'lon': float(coords[0])
            }
            citations.append(parsed)
            if len(citations) == 1000:
                print("inserting")
                sqa.run_in_session(lambda session: bulk_insert(session, Citation, citations))
                citations = []
        print("inserting")
        sqa.run_in_session(lambda session: bulk_insert(session, Citation, citations))

def bulk_insert(session, c,m):
    session.bulk_insert_mappings(c, m)
    session.commit()

    # return 

def parse_meters(row):
    return {
        'post_id': row['POST_ID'],
        'ms_pay_station_id': row['MS_PAY_STATION_ID'],
        'ms_space_num': safe_int(row['MS_SPACE_NUM']),
        'sensor_flag': row['SENSOR_FLAG'],
        'is_on_street': row['ON_OFFSTREET_TYPE'] == 'ON',
        'offstreet_id': safe_int(row['OSP_ID']),
        'jurisdiction': row['JURISDICTION'],
        'active_meter_flag': row['ACTIVE_METER_FLAG'],
        'reason_code': row['REASON_CODE'],
        'is_smart_meter': row['SMART_METER_FLAG'] == 'Y',
        'is_multi_space': None if row['METER_TYPE'] == '-' else row['METER_TYPE'] == 'MM',
        'cap_color': row['CAP_COLOR'],
        'old_rate_area': row['OLD_RATE_AREA'],
        'street_id': safe_int(row['STREET_ID']),
        'street_name': row['STREET_NAME'],
        'street_num': safe_int(row['STREET_NUM']),
        'lon': float(row['LONGITUDE']),
        'lat': float(row['LATITUDE']),
        'comments': row['COMMENTS'],
        'collection_route': row['COLLECTION_ROUTE'],
        'collection_subroute': row['COLLECTION_SUBROUTE'],
        'pmr_route': row['PMR_ROUTE'],
        'nfc_key': row['NFC_KEY'],
        'spt_code': row['SPT_CODE']
    }

def ingest_citations(citations, session):
    print(f"inserting {len(citations)} citations")
    session.bulk_insert_mappings(Citation, citations)
    session.commit()

def ingest_meters(meters, session):
    print(f"inserting {len(meters)} meters")
    session.bulk_insert_mappings(Meter, meters)
    session.commit()

def main():
    sqa.connect_to_db(app)
    meters = handle_parse('db/meters.csv', parse_meters)
    sqa.run_in_session(lambda session: ingest_meters(meters, session))
    #citations = handle_parse('db/citations.csv', parse_citations)
    #parse_citations('db/citations.csv')
    # sqa.run_in_session(lambda session: ingest_citations(citations, session))


if __name__ == '__main__':
    main()
