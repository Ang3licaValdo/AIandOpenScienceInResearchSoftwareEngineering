import unittest
import link

f = open ('test_links.txt','a')

doi_all = ['https://doi.org/10.1038/s41598-019-56927-5','https://doi.org/10.1038/s41598-019-56927-5']
list_of_words = []

class TestLink(unittest.TestCase):
    def test_findingDOI(self):
        result = link.findingDOI(doi_all, list_of_words,f)                             
        self.assertEqual(result, 'All DOI links added', 'Not all DOI links added')

if __name__ == '__main__':
    unittest.main()
    f.close()