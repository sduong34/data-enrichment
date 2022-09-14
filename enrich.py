 #import packages
import pandas as pd
import numpy as np
import tabulate

#load datasets
sparcs = pd.read_csv('SPARCS.csv')
neighborhoodatlas = pd.read_csv('NY_2015_ADI_9 Digit Zip Code_v3.1.csv')

#read column names
sparcs.columns
neighborhoodatlas.columns

#clean up column names 
sparcs.columns = sparcs.columns.str.replace('[^A-Za-z0-9]+', '_')
neighborhoodatlas.columns = neighborhoodatlas.columns.str.replace('[^A-Za-z0-9]+', '_')

#view types 
sparcs.dtypes
neighborhoodatlas.dtypes
