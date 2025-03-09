from distutils.core import setup
import py2exe
import glob
import os
import re
import sqlite3
from pathlib import Path
from time import sleep
from random import randrange

setup(windows=['hackerscript.py'])