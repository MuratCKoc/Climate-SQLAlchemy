#Import dependencies
from flask import Flask, jsonify
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

import datetime as dt
import pandas as pd

# Setup database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

session = Session(engine)

last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

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
        f"<a href='/api/v0.1/start/end'>End date temperature<br/>")

@app.route("/api/v0.1/precipitation")
def precipitation():
    return('ASDASDASD')

@app.route("/api")
def apis():
    return(f"asd")

#@app.route("/api/v0.1/stations")

if __name__ == '__main__':
    app.run(debug=True)
