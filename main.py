from extract_gpx import load_data
from slope_visualization import slope_plot_folium
import itertools
from slope_heatmap import slope_heatmap_folium

def execute():
    # load all data files
    coords = []
    for i in range(1, 7):
        coords.append(load_data("data/dag_" + str(i) + ".gpx"))

    # returns nested lists, now convert to 1 single list
    merged_coords = list(itertools.chain(*coords))

    # plot in folium
    #slope_plot_folium(merged_coords)

    # plot heatmap
    slope_heatmap_folium(merged_coords)

if __name__ == "__main__":
    execute()


