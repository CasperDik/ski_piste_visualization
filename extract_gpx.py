import pandas as pd
import gpxpy.gpx

def load_data(filename):
    # read gpx file
    gpx_file = open(filename, 'r')
    gpx = gpxpy.parse(gpx_file)

    # initiate empty list to store points
    points = []

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                # append latitude, longitude and time as a list to the list points
                points.append([point.latitude, point.longitude, point.time])

    return points