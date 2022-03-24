import unittest

def cube_volume(x):
    return x*x*x

class CheckVolume(unittest.TestCase):
    def test_Volume(self):
        x = 5.55
        result = cube_volume(x)
        self.assertAlmostEqual(result, x*x*x )

if __name__ =="__main__":
    unittest.main
