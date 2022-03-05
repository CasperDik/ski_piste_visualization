import pandas as pd
import folium

def slope_plot_folium(coords):
    lats = pd.Series([p[0] for p in coords], name="lats")
    longs = pd.Series([p[1] for p in coords], name="longs")

    m = folium.Map(
       location=[(min(lats) + max(lats))/2, (min(longs) + max(longs))/2],
       zoom_start=11.5,
       tiles='Stamen Terrain'
    )

    # title layer do get slopes on map
    tile_layer = folium.TileLayer(
        tiles='https://tiles.opensnowmap.org/pistes/{z}/{x}/{y}.png',
        attr='Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors & ODbL, &copy; <a href="https://www.opensnowmap.org/iframes/data.html">www.opensnowmap.org</a> <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
        name='ski pistes'
    ).add_to(m)

    # plot the lines using coordinates
    folium.PolyLine([zip(lats, longs)], color="white", weight=5, opacity=0.8).add_to(m)

    m.save("slope_visualization.html")
