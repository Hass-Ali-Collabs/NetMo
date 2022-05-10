import folium

m = folium.Map(location=[52.37613757431285, 4.927801674596649], zoom_start=3)
m.save('map.html')

# folium.Marker([52.376111375557294, 4.927876776449689],
# 	popup="<h1>hello</h1>",tooltip = "the location name",
# 	icon=folium.Icon(icon = 'heart',icon_color='red')).add_to(m)

# Import the pandas library
import pandas as pd

# Make a data frame with dots to show on the map
data = pd.DataFrame({
   'lon':[-58, 2, 145, 30.32, -4.03, -73.57, 36.82, -38.5],
   'lat':[-34, 49, -38, 59.93, 5.33, 45.52, -1.29, -12.97],
   'name':['Buenos Aires', 'Paris', 'melbourne', 'St Petersbourg', 'Abidjan', 'Montreal', 'Nairobi', 'Salvador'],
   'value':[10, 12, 40, 70, 23, 43, 100, 43]
}, dtype=str)

# add marker one by one on the map
for i in range(0,len(data)):
   folium.Marker(
      location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
      popup=data.iloc[i]['name'],
   ).add_to(m)
   m.save('map.html')