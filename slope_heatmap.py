import pandas as pd
import folium
from geopy import distance
from folium import plugins
from folium.plugins import HeatMap

# note: doesn't give nice result

def slope_heatmap_folium(coords):
    lats = pd.Series([p[0] for p in coords], name="lats")
    longs = pd.Series([p[1] for p in coords], name="longs")

    # get speed
    speedOfSegment = []
    for i in range(len(lats)-1):
        distanceOfSegment = distance.distance((lats[i], longs[i]), (lats[i + 1], longs[i +1])).meters
        durationOfSegment = coords[i + 1][2] - coords[i][2]
        speedOfSegment.append(distanceOfSegment / durationOfSegment.seconds / 1000 * 3600)

    df = pd.DataFrame({"lats": lats[1:], "longs": longs[1:], "speed": speedOfSegment})
    df = df[df["speed"] > 15]
    #print(df.head())

    m = folium.Map(
       location=[(min(df["lats"]) + max(df["lats"]))/2, (min(df["longs"]) + max(df["longs"]))/2],
       zoom_start=11.5,
       tiles='Stamen Terrain'
    )

    # title layer do get slopes on map
    tile_layer = folium.TileLayer(
        tiles='https://tiles.opensnowmap.org/pistes/{z}/{x}/{y}.png',
        attr='Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors & ODbL, &copy; <a href="https://www.opensnowmap.org/iframes/data.html">www.opensnowmap.org</a> <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
        name='ski pistes'
    ).add_to(m)

    # heatmap
    HeatMap(list(zip(df["lats"], df["longs"])), radius=12, min_opacity=0.5, max_zoom=15).add_to(m)

    m.save("slope_heatmap.html")
