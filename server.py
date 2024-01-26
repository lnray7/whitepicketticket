from flask import Flask, render_template, request, flash, session, redirect, jsonify
import crud
import db.sqa as sqa
from jinja2 import StrictUndefined
from model import Citation, Meter
import googlemaps
#from google.oauth2 import id_token
#from google.auth.transport import requests

app = Flask(__name__)
app.secret_key = "777"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """View homepage"""

    # get meters
    meters = Meter.query.limit(10).all()

    return render_template("homepage.html", meters=meters)

@app.route('/api/parking_data')
def parking_data():
    address = request.args['address']

    client = googlemaps.Client(key='AIzaSyBdPYyaT-s6ha5WXv8rEBalylzXx2iPEUk')

    coords = client.geocode(address)
    print(coords)
    lat = coords[0]["geometry"]["location"]["lat"]
    lon = coords[0]["geometry"]["location"]["lng"]
    
    citations = bool(request.args['citations'])
    meters = bool(request.args['meters'])

    max_lat = lat + 0.0012
    min_lat = lat - 0.0012
    max_lon = lon + 0.0084
    min_lon = lon - 0.0084

    response_data = {"search_coords": {"lat": lat, "lon": lon}}

    if citations:
        within_range = Citation.query.filter(
            Citation.lat>min_lat, 
            Citation.lat<max_lat,
            Citation.lon>min_lon,
            Citation.lon<max_lon
        ).all()

        response_data['citations'] = [citation.toDictionary() for citation in within_range]
    
    if meters:
        within_range = Meter.query.filter(
            Meter.lat>min_lat, 
            Meter.lat<max_lat,
            Meter.lon>min_lon,
            Meter.lon<max_lon
        ).all()
        print(within_range)
        # response_data['meters'] = [meter.toDictionary() for meter in within_range]
        min_difference = None 
        min_meter = None
        for meter in within_range:
            lat_difference = abs(lat - meter.lat)
            lon_difference = abs(lon - meter.lon)
            difference = lat_difference + lon_difference
            if min_difference is None or difference < min_difference:
                min_difference = difference
                min_meter = meter
        if min_meter is not None:
            response_data['min_meter'] = min_meter.toDictionary()
    return jsonify(response_data)


#@app.route('/google-login', methods=['POST'])
#def google_login():
    #token = request.form['token']
    #try:
        #idinfo = id_token.verify_oauth2_token(token, requests.Request())
    
        #name = idinfo['name']
        #email = idinfo['email']
        #picture = idinfo['picture']
        #save user to database

        #session['user_email'] = email
        #return redirect('/')
   # except ValueError:
        #return redirect('/login')

def address_to_coords():
    client = googlemaps.Client(key='YOUR_API_KEY')
    coords = client.reverse_geocode((LAT, LNG))



if __name__ == '__main__':
    sqa.connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5001)
    #sqa.connect_to_db(app)
