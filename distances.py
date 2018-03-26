import json
import math

from haversine import haversine


class Distances(object):
    def __init__(self):
        airport_json = open("./alaska_airports.json", "r").read()
        self.alaska_airports = json.loads(airport_json)

    def toRadians(self, degrees):
        return degrees * math.pi / 180

    def distance(self, location1, location2):
        return haversine(location1, location2)

    def get_coords(self, airport_code):
        lat = float()
        lon = float()

        for airport in self.alaska_airports:
            if airport['LocationID'] == airport_code:
                lat = airport['Lat']
                lon = airport['Lon']

        print("{}, {}".format(lat,lon))
        return(lat, lon)


Distances().get_coords('ADK')
# coords = Distances(get_coords('AQY'))
