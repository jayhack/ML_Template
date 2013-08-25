#!/usr/bin/python
# ---------------------------------------------------------- #
# File: ML_Template.py
# --------------------
# main class for ML applications
#
#
#
#
# ---------------------------------------------------------- #

#----- Standard -----
import os
import sys
import pickle 
import math

#----- My Files -----
from common_utilities import *	# printing functions


class ML_Template:

	#--- Filenames ---
	data_directory 			= os.path.join (os.getcwd(), 'data')
	classifiers_directory 	= os.path.join (os.getcwd(), 'classifiers')	 
	filenames = {}		

	#--- Data ---
	examples = []		# list of all examples



	# Function: constructor 
	# ---------------------
	# loads data for you
	def __init__ (self, filenames=None, load_from_text_file=True):

		self.filenames = filenames

		### Step 1: print out a welcome message introducing the app ###
		print_welcome (self.__class__.__name__, 'Jay Hack', 'Summer 2013')

		### Step 2: load in the data ###
		if load_from_text_file:
			load_data (filenames['data_input'])



























