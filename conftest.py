# conftest.py
import sys
from os.path import dirname as d
from os.path import abspath, join

root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)
sys.path.append(join(root_dir, "tests/data"))
sys.path.append(join(root_dir, "tests/gmprocess"))
