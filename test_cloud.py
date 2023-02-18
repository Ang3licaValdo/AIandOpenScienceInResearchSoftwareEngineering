import unittest
import cloud

class TestCloud(unittest.TestCase):
    def test_verifyXML(self):
        result = cloud.verifyXML('test.xl')
        self.assertEqual(result, 1, 'Not an XML file')

if __name__ == '__main__':
    unittest.main()