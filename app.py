#Import dependencies

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

import datetime as dt
import pandas as pd
from flask import Flask, jsonify

# Setup database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup
app = Flask(__name__)

# Flask Routes

@app.route("/")
def index():
    #Available Api's
    return (f"Available Routes:<br/><hr>"
        f"<a href='/api/v0.1/precipitation'>Precipitation<br/>"
        f"<a href='/api/v0.1/stations'>Available Stations<br/>"
        f"<a href='/api/v0.1/tobs'>Temperature at the time of observation<br/>"
        f"<a href='/api/v0.1/start'>Start date temperature<br/>"
        f"<a href='/api/v0.1/start-end'>End date temperature<br/>")

@app.route("/api/v0.1/precipitation")
def precipitation():
    # Link to db
    session = Session(engine)

    # Entry of the last date
    date_eof = session.query(Measurement.date).order_by(
        Measurement.date.desc()).first()
    # A year before last entry
    previous_year = datetime.strptime(date_eof[0], '%Y-%m-%d') - dt.timedelta(days=365)

    # Precipitation query for the last year
    precip_last_year = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > previous_year).all()

    # Store results in dictionary
    precipitation_dict = []
    for date, prcp in precip_last_year:
        row = {}
        row['date'] = date
        row['prcp'] = prcp
        precipitation_dict.append(row)
    
    # Return dictionary as JSON
    return jsonify(precipitation_dict)

@app.route("/api/v0.1/stations")
def stations():
    # Link to db
    session = Session(engine)

    # Query all stations
    results = session.query(Station.station, Station.name).all()

    # Store results in dictionary
    all_stations = []
    for station, name in results:
        row = {}
        row['station'] = station
        row['name'] = name
        all_stations.append(row)

    return jsonify(all_stations)

#@app.route("/api/v0.1/tobs")
#@app.route("/api/v0.1/start")
#@app.route("/api/v0.1/start-end")

if __name__ == '__main__':
    app.run(debug=True)
