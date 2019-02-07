#!/usr/bin/env python3
import sys
import os
os.execl("/usr/bin/python3.5", "python3.5", *sys.argv)
print(sys.version)
print(sys.executable)
from app import app as application