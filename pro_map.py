
import folium
import pandas

data=pandas.read_csv("D:\\aa.csv" ,encoding = "cp1252")
print(data)
name=list(data["name"])
v=list(data["v"])
h=list(data["h"])
max_consomation=list(data["max_con"])
p=list(data["priority"])
print(name)
print(v)
print(h)
print(max_consomation)
print(p)
map=folium.Map(location=[36.204692, 1.260199],zoom_start=15)
fg=folium.FeatureGroup(name="my map")

for v,h,nm,mc in zip(v,h,name,max_consomation):
    fg.add_child(folium.Marker(location=[v,h],popup="<b>name  : </b>"+" poste " +str(nm)+"<br> <b>max_consomation : </b> "+str(mc)+" KW" ,icon=folium.Icon(color='green')))
    
map.add_child(fg)

map.save("map2.html")
