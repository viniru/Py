import folium
map = folium.Map(location = [30,0],zoom_start=6,tiles="Mapbox Bright")
fg = folium.FeatureGroup(name='may map')

for coordinates in [[1,3],[4,6]]:
    fg.add_child(folium.Marker(location = coordinates , popup="hi, kadle" , icon = folium.Icon(color = 'green')))
map.add_child(fg)
#map.add_child(folium.Marker(location = [38.2,-99.1] , popup="hi, kadle" , icon = folium.Icon(color = 'green')))  just another way
map.save("map.html")
