import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            

def round_corners_one_image(original_image,logo,color, wide):
	""" Rounds the corner of a PIL.Image
	
	original_image must be a PIL.Image
	Returns a new PIL.Image with rounded corners, where
	0 < percent_of_side < 1
	is the corner radius as a portion of the shorter dimension of original_image
	"""
	r,g,b = color
	width, height = original_image.size
	border = PIL.Image.new('RGBA', ((width + 2*wide), (height + 2*wide)), (r, g, b))
	border.paste((original_image), (wide, wide))
	logo.paste(original_image,(0,0),mask=logo)
	return border
	return logo

def get_images(directory=None):
	""" Returns PIL.Image objects for all the images in directory.
	
	If directory is not specified, uses current directory.
	Returns a 2-tuple containing 
	a list with a  PIL.Image object for each image file in root_directory, and
	a list with a string filename for each image file in root_directory
	"""
	
	if directory == None:
		directory = os.getcwd() # Use working directory if unspecified
		
	image_list = [] # Initialize aggregaotrs
	file_list = []
	
	directory_list = os.listdir(directory) # Get list of files
	for entry in directory_list:
		absolute_filename = os.path.join(directory, entry)
		try:
			image = PIL.Image.open(absolute_filename)
			file_list += [entry]
			image_list += [image]
		except IOError:
			pass # do nothing with errors tying to open non-images
	return image_list, file_list



def round_corners_of_all_images(logo,color, wide, directory=None):
	""" Saves a modfied version of each image in directory.
	
	Uses current directory if no directory is specified. 
	Places images in subdirectory 'modified', creating it if it does not exist.
	New image files are of type PNG and have transparent rounded corners.
	"""
	
	if directory == None:
		directory = os.getcwd() # Use working directory if unspecified
		
	# Create a new directory 'modified'
	new_directory = os.path.join(directory, 'modified')
	try:
		os.mkdir(new_directory)
	except OSError:
		pass # if the directory already exists, proceed  
	
	# Load all the images
	image_list, file_list = get_images(directory)  

	# Go through the images and save modified versions
	for n in range(len(image_list)):
		# Parse the filename
		print(n)
		filename, filetype = os.path.splitext(file_list[n])
		
		# Round the corners with default percent of radius
		curr_image = image_list[n]
		new_image = round_corners_one_image(curr_image,logo,color,wide) 
		
		# Save the altered image, suing PNG to retain transparency
		new_image_filename = os.path.join(new_directory, filename + '.png')
		new_image.save(new_image_filename)

