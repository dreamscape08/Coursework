# imports
import panel as pn
pn.extension('plotly')
import plotly.express as px
import pandas as pd
import hvplot.pandas
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from dotenv import load_dotenv
import warnings
warnings.filterwarnings('ignore')


# Read the Mapbox API key
load_dotenv()
map_box_api = os.getenv("mapbox")



# Read the census data into a Pandas DataFrame
file_path = Path("Data/sfo_neighborhoods_census_data.csv")
sfo_data = pd.read_csv(file_path, index_col="year")
sfo_data.info()


# Calculate the mean number of housing units per year (hint: use groupby)
# Refresh on Pandas.Series Attributes(https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html) 
units_per_year=sfo_data.groupby(sfo_data.index).mean()
peryearsold=units_per_year['housing_units']


# Save the dataframe as a csv file
peryearsold.to_csv('peryearsold.csv',header=True)


# Use the Pandas plot function to plot the average housing units per year.
peryearsold.plot.bar(
                      ylim=(370000,385000)
                    , title='Housing Units in San Fransisco from 10\'-16\''
                    , ylabel= "Units Sold"
                    , xlabel='Year'
                    , rot=0
                    , grid=False
                    , figsize=(5,5)
                )
#--------BONUS--------#                   
#units_per_year=sfo_data.groupby(sfo_data.index).mean().std().min().max()
#peryearsold=units_per_year['housing_units']


# Calculate the average sale price per square foot and average gross rent
avghousingdf=units_per_year.drop(columns='housing_units')



# Create two line charts, one to plot the average sale price per square foot and another for average montly rent
saleplot=avghousingdf['sale_price_sqr_foot'].plot.line(
                     title='Yearly Price per Sqft Average'
                    , ylabel='Price per SqFt'
                    , xlabel='Year'
                    , rot=0
                    , lw=2
                    , grid=True
                    , figsize=(5,5)
                    , xlim=(2010,2016))


rentplot=avghousingdf['gross_rent'].plot.line(title='Monthly Gross Rent Average'
                    , ylabel='Price per Month'
                    , xlabel='Year'
                    , rot=0
                    , grid=True
                    , lw=2
                    , figsize=(5,5)
                    , color='r'
                    , xlim=(2010,2016))


# Group by year and neighborhood and then create a new dataframe of the mean values
yearly_neighborhood=sfo_data.groupby(['year','neighborhood']).mean().drop(columns='housing_units').dropna()


# Use hvplot to create an interactive line chart of the average price per sqft.
# The plot should have a dropdown selector for the neighborhood
yearly_neighborhood.hvplot.line(
      y='sale_price_sqr_foot'
    , x='year'
    , subplots=False
    , groupby=['neighborhood']
    , ylim=(0,2500)
    , dynamic=False
    , height=500
    , hover_cols='one')



# Use hvplot to create an interactive line chart of the average monthly rent.
# The plot should have a dropdown selector for the neighborhood
yearly_neighborhood.hvplot.line(
      y='gross_rent'
    , x='year'
    , subplots=False    
    , groupby=['neighborhood']
    , ylim=(0,5000)
    , xlim=(2010,2017)
    , dynamic=False
    , height=500
    , hover_cols='one')


# Getting the data from the top 10 expensive neighborhoods to own
top10owned=yearly_neighborhood.groupby('neighborhood').mean().sort_values('sale_price_sqr_foot',ascending=False).head(10).drop(columns='gross_rent')
top10owned


# Plotting the data from the top 10 expensive neighborhoods
top10owned.hvplot(kind='bar',color='blue',rot=90,title='Top 10 Expensive Neighborhoods in SFO',ylabel='Avg. Sale Price Per Sqft',x='neighborhood',ylim=(600,900))


# Fetch the previously generated DataFrame that was grouped by year and neighborhood
# Plotting the data from the top 10 expensive neighborhoodsin
top10yearly = sfo_data[sfo_data["neighborhood"].isin(top10owned.index)].drop(columns='housing_units')
top10yearly.hvplot(kind='bar',color='blue',rot=90,title='Top 10 Expensive Neighborhoods in SFO',ylabel='Sale/Rent ',x='year',y=(['sale_price_sqr_foot','gross_rent']),groupby='neighborhood',dynamic=False)


# Load neighborhoods coordinates data
data=pd.read_csv('Data/neighborhoods_coordinates.csv',index_col='Neighborhood')


# Calculate the mean values for each neighborhood
plotdata=sfo_data.groupby(['neighborhood']).mean()


# Join the average values with the neighborhood locations
plotdata=pd.concat([plotdata,data],axis='columns',join='outer').dropna().reset_index()


# Set the Mapbox API
px.set_mapbox_access_token(map_box_api)
# Create a scatter mapbox to analyze neighborhood info
map_box = px.scatter_mapbox(
    plotdata,
    lat="Lat",
    lon="Lon",
    size="gross_rent",
    color="index",
    zoom=10)
map_box.update_layout(
    mapbox_style="streets")
map_box.show()


# Fetch the data from all expensive neighborhoods per year.
top10yearlyfull = sfo_data[sfo_data["neighborhood"].isin(top10owned.index)].groupby('neighborhood').mean().reset_index().round(2)


# Parallel Categories Plot
px.parallel_coordinates(top10yearlyfull,color='gross_rent', width = 1000, height = 500)


# Parallel Coordinates Plot
px.parallel_categories(top10yearlyfull,color='sale_price_sqr_foot',)


# Sunburst Plot
sunburstdata=top10yearly.reset_index()
px.sunburst(sunburstdata
            , path=['year','neighborhood']
            , values='sale_price_sqr_foot'
            , color='gross_rent'
            , color_continuous_scale='RdBu')















