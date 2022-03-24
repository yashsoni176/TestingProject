import unittest

def check(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"

class EvenorOddApp(unittest.TestCase):

    def test_case_evencase_check(self):
        x = 10
        result = check(x)
        self.assertEqual("even", result)

    def test_case_oddcase_check(self):
        x = 11
        result = check(x)
        self.assertNotEqual("even", result)

if __name__ =="__main__":
    unittest.main