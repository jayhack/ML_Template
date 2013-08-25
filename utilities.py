# ---------------------------------------------------------- #
# File: utilities.py
# -------------------------
# functions that serve as utilities for printing out menus, etc
#
#
#
#
# ---------------------------------------------------------- #


# Function: print_welcome
# -----------------------
# prints out a welcome message
def print_welcome (app_name, author, publish_date):

	label_width = 70

	app_name_string =  "####################[ --- " + app_name + " --- ]"
	publish_string = "####################[ - by " + author + ", " + publish_date + " - ]"

	app_name_string += (label_width - len(app_name_string)) * '#'
	publish_string += (label_width - len(publish_string)) * '#'

	print '#' * label_width
	print app_name_string
	print publish_string
	print '#' * label_width
	print '\n'


# Function: print_status
# ----------------------
# prints out a status message 
def print_status (stage, status):
	
	print "-----> " + stage + ": " + status

# Function: print_message
# -----------------------
# prints the specified message in a unique format
def print_message (message):

	print "-" * len(message)
	print message
	print "-" * len(message)
	print "\n"


# Function: print_error
# ---------------------
# prints an error and exits 
def print_error (top_string, bottom_string):
	print "Error: " + top_string
	print "---------------------"
	print bottom_string
	exit ()

