import unittest

from test import get_country_city

class test(unittest.TestCase):
    def test_format(self):
        a=get_country_city('india','delhi')
        self.assertEqual(a,'delhi,india')

if __name__=='__main__':
    unittest.main()