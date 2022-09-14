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

#choose which columns to merge 
sparcs_small = sparcs[['Zip_Code_3_digits','Gender','Length_of_Stay','Total_Costs']]
print(sparcs_small.sample(10).to_markdown())
neighborhoodatlas_small = neighborhoodatlas[['ZIPID']]
print(neighborhoodatlas_small.sample(10).to_markdown())

#combine into one dataset
combined_df = combined_df = sparcs_small.merge(neighborhoodatlas_small, how='left', left_on='Zip_Code_3_digits', right_on='ZIPID')
combined_df = combined_df.drop(columns=['ZIPID'])
combined_df.columns

combined_df_nodups = combined_df.drop_duplicates(subset=['Zip_Code_3_digits'])
combined_df.head

#save to new csv
combined_df.to_csv('combined.csv')

