# Hawaii Climate Analysis
This project displays earthquakes recorded by the USGS over the past week on and interactive map.

#### Technology
* Python
* Pandas
* Matplotlib
* Flask
* SQLAlchemy
* Jupyter Notebook

## Step 1 - Climate Analysis and Exploration


### Precipitation Analysis
* Use Pandas to print the summary statistics for the precipitation data.

  ![precipitation](Images/precipitation.png)



### Station Analysis

    ![station-histogram](Images/station-histogram.png)

- - -

## Step 2 - Climate App

* Use Flask to create your routes.

### Routes

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the most active station for the last year of data.
  
  * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.


### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

* Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.
    ![stations](Images/station-histogram.png)

### Temperature Analysis II

* Plot the min, avg, and max temperature from your previous query as a bar chart.
    ![Describe](Images/describe.png)

  * Use the average temperature as the bar height.

  * Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

    ![temperature](Images/temperature.png)

### Daily Rainfall Average


  ![daily-normals](Images/daily-normals.png)
