# Import libraries
import os.path
from os import path
import pandas as pd
import folium

state_geo = os.path.join(os.path.curdir, 'us-states.json')
state_exposure = os.path.join(os.path.curdir, 'US_GAEN_STATUS.csv')
state_data = pd.read_csv(state_exposure)
 
# Initialize the map:
m = folium.Map(location=[37, -102], zoom_start=5)
 
# Add the color for the chloropleth:
folium.Choropleth(
 geo_data=state_geo,
 name='choropleth',
 data=state_data,
 columns=['State', 'ExposureState'],
 key_on='feature.id',
 fill_color='YlGn',
 fill_opacity=0.7,
 line_opacity=0.2,
 legend_name='Exposure Notifications Status (%)',
).add_to(m)
 
# Save to html
m.save('GAEN_Exposure_Notificaton_US_States.html')
