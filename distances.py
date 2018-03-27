import json
import math
import sys

from haversine import haversine


class Airports(object):
    def __init__(self):
        """Load all the airports into memory"""
        airport_json = open("./alaska_airports.json", "r").read()
        self.alaska_airports = json.loads(airport_json)

    def get_airport_coords(self, airport_code):
        """Get the airport object from the list of airports and return coords"""
        airport = ([airport for airport in self.alaska_airports
                            if airport['LocationID'] == airport_code
                    ].pop()
                   )
        return(airport['Lat'], airport['Lon'])

    def get_all_distances(self, coords):
        """Create a dict of all distances to all Airports from coordinates."""

        distances = {}
        for airport in self.alaska_airports:
            distances[airport["LocationID"]] = Airports().get_distance(
                coords,
                self.get_airport_coords(airport['LocationID'])
            )
        return distances

    def get_distance(self, location1, location2):
        """ Return the distance between two coordinates."""
        return haversine(location1, location2)

    def get_closest_three_airports(self, coords):
        """Return the closest three airports"""
        airport_proximities = self.get_all_distances(coords)
        closest = sorted(airport_proximities, key=airport_proximities.get)
        return closest[:3]

if __name__ == "__main__":
    coords = sys.argv
    print(Airports().get_closest_three_airports(
            (float(coords[1]), float(coords[2]))
        )
    )
