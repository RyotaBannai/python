"""
 any useful reusable library can be this subdirectry.
 but these are rarely used in main application.
"""

import sys, os, pathlib
import pprint

class D(object):
	def __init__(self):
		print('class D')
	
	@staticmethod #(e.g. C.f()) or on an instance (e.g. C().f())
	def mySum(a, b):
		return sum([a, b])

