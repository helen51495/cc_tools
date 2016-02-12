""" 
Takes json input and converts it to a dat file in the same folder.

"""
import cc_json_utils
import sys
import cc_data
import cc_dat_utils

if len(sys.argv)==3:
	print("Starting conversion...")
	# get json file
	input_json_file = sys.argv[1]
	# get dat file name
	output_dat_file = sys.argv[2]

	print("Now taking data from " +input_json_file + " and converting it into a playable CC level.")

	#Make a CCdatafile; change name to output dat file name?
	cc_data_file = cc_json_utils.make_cc_data_from_json(input_json_file)

	# Make a dat file from the cc_data
	cc_dat_utils.write_cc_data_to_dat(cc_data_file, output_dat_file)

	print("The dat file has been created as "+ output_dat_file)
	print("Conversion complete!")

else:
	print("Unknown command line options. Please try again.")