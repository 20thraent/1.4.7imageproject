import PIL
import matplotlib.pyplot as plt 
import os.path  
import PIL.ImageDraw            

def round_corners_one_image(original_image,logo,color, wide):
	#BORDER
	original_image = PIL.Image.open(original_image).convert("RGBA")
	r,g,b = color
	width, height = original_image.size
	border = PIL.Image.new('RGBA', ((width + 2*wide), (height + 2*wide)), (r, g, b))
	back2 = border
	fore2 = original_image
	back2.paste(fore2,(wide,wide))
	#back2.show()
	#border.paste((original_image), (wide, wide))

	#LOGO
	background = back2
	foreground = PIL.Image.open(logo).convert("RGBA")
	background.paste(foreground,(0,0),foreground)
	background.show()
	
	#back2 = border
	#fore2 = test
	#.paste(background,(0,0),background)
	#border.show()

	#return border
	#return logo

def get_images(directory=None):
	
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

