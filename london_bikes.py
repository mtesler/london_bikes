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
