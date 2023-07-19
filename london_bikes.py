import pandas as pd
import zipfile
import kaggle

# download dataset from Kaggle using the Kaggle API
# kaggle datasets download -d hmavrodiev/london-bike-sharing-dataset

# extract the file from the downloaded zip file
zipfile_name = 'london-bike-sharing-dataset.zip'
with zipfile.ZipFile(zipfile_name, 'r') as file:
    file.extractall()

# read in the csv file as a pandas dataframe
bikes = pd.read_csv('london_merged.csv')

# explore the data
bikes.info()

# specyfying the column names that I want to use
new_col_dict = {
    'timestamp': 'time',
    'cnt': 'count',
    't1': 'temp_real_C',
    't2': 'temp_feels_like_C',
    'hum': 'humidity_percent',
    'wind_speed': 'wind_speed_kph',
    'weather_code': 'weather',
    'is_holiday': 'is_holiday',
    'is_weekend': 'is_weekend',
    'season': 'season'
}

# rename the columns to the specified column names
bikes.rename(new_col_dict, axis=1, inplace=True)

# change the humidity values to percentage (i.e. a value between 0 and 1)
bikes.humidity_percent = bikes.humidity_percent / 100

# create a season dictionary to map the column values to the actual written values
season_dict = {
    '0.0': 'spring',
    '1.0': 'summer',
    '2.0': 'autumn',
    '3.0': 'winter'
}

# create a weather dictionary to map the column values to the actual written values
weather_dict = {
    '1.0': 'Clear',
    '2.0': 'Scattered clouds',
    '3.0': 'Broken clouds',
    '4.0': 'Cloudy',
    '7.0': 'Rain',
    '10.0': 'Rain with thunderstorm',
    '26.0': 'Snowfall'
}

# change the seasons column data type to string
bikes.season = bikes.season.astype('str')

# map the seasons column values to the actual written seasons
bikes.season = bikes.season.map(season_dict)

# change the weather column data type to string
bikes.weather = bikes.weather.astype('str')

# map the weather column values to the actual writter weaters
bikes.weather = bikes.weather.map(weather_dict)
