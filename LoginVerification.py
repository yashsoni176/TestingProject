import unittest

def login(username, password):
    if username == "admin" and password == "12345":
        return True
    else:
        return False

class LoginVerification(unittest.TestCase):
    def test_case_login(self):
        result = login("admin","12345")
        self.assertTrue(result)

if __name__ =="__main__":
    unittest.main
