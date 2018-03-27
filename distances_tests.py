import unittest

from distances import Airports


class AirportsTests(unittest.TestCase):

    def test_get_airport_coords(self):
        """  ADK is at (51.88358205555556, 176.64247991666667)"""
        self.assertEqual(
            Airports().get_airport_coords('ADK'),
            (51.88358205555556, 176.64247991666667)
        )

    def test_get_all_distances(self):
        """ Map of distances should be a dict"""
        self.assertEqual(
            Airports().get_all_distances(
                (51.88358205555556, 176.64247991666667)
            ).__class__,
            dict
        )

        """ Test that ADK is zero kilometers from ADK"""
        self.assertEqual(
            Airports().get_all_distances(
                (51.88358205555556, 176.64247991666667),
            )['ADK'],
            0
        )

    def test_get_distance(self):
        """ With the same coordinates, distance should be 0"""
        self.assertEqual(
            Airports().get_distance(
                (51.88358205555556, 176.64247991666667),
                (51.88358205555556, 176.64247991666667)
            ),
            0
        )

        """Z13 and KKI are 3.21... kilometers from each other"""
        self.assertEqual(
            Airports().get_distance(
                (60.91380972222222, 161.49332916666665),
                (60.90786472222222, 161.43507722222225)
            ),
            3.217715669975009
        )

    def test_get_closest_three_airports(self):
        """The closest 3 airports to (51.88358205555556, 176.64247991666667)
        are ADK, AKA.  Everything else is outside of 500 KM"""

        coords = (51.88358205555556, 176.64247991666667)
        self.assertEqual(
            Airports().get_closest_three_airports(coords),
            ['ADK', 'AKA']
        )


if __name__ == "__main__":
    unittest.main()
