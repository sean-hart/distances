import unittest

from distances import Distances

class DistancesTests(unittest.TestCase):
    # def test_distance(self):
    #     assertEqual(aero.distance(2,2), )
    #     assertEqual(aero.distance(2,2).__class__, int)

    def test_get_coords(self):
        self.assertEqual(
            Distances().get_coords('ADK'),
            (51.88358205555556, 176.64247991666667)
        )


if __name__ == "__main__":
    unittest.main()
