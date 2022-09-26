import md
import sys, unittest
import os

md.run_md()

class MdTests(unittest.TestCase):

    def test_calcenergy(self):
        path = "/Users/olle/Documents/TFYA99/project-hands-on/hands-on-3/cu.traj"
        isFile = os.path.isfile(path)
        self.assertTrue(isFile)

if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())



