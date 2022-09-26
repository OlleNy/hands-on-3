import md
import sys, unittest
import pathlib as pl

md.run_md(md)

class MdTests(unittest.TestCase):

    def assertIsFile(self, path):
        def test(self):
            path = pl.Path("cu.traj")
            self.assertIsFile(path)


