import PIL
import matplotlib.pyplot as plt 
import os.path  
import PIL.ImageDraw            

def round_corners_one_image(original_image,logo,color, wide):
	#BORDER
	original_image = PIL.Image.open(original_image).convert("RGBA") #open image as PIL object
	r,g,b = color #border color chosen by user
	width, height = original_image.size
	border = PIL.Image.new('RGBA', ((width + 2*wide), (height + 2*wide)), (r, g, b))
	back2 = border
	fore2 = original_image
	back2.paste(fore2,(wide,wide))
	#LOGO
	background = back2
	foreground = PIL.Image.open(logo).convert("RGBA")
	sbox = foreground.getbbox() #gets image size with transparency
	mbox = background.getbbox() #gets image size with transparency 
	boxx = (mbox[2] - sbox[2]) #background width minus foreground width 
	boxy = (mbox[3] - sbox[3]) #foreground height minus background height

	background.paste(foreground,(boxx-10,boxy-10),foreground)
	return background

def get_images(directory=None):
	
	if directory == None:
		directory = os.getcwd() # Use working directory if unspecified
		
	image_list = [] # Initialize aggregaotrs
	file_list = []
	
	directory_list = os.listdir(directory) # Get list of files
	for entry in directory_list:
		absolute_filename = os.path.join(directory, entry)
		try:
			image = absolute_filename
			file_list += [entry]
			image_list += [image]
		except OSError:
			pass # do nothing with errors tying to open non-images
	def filepass(directory):
		image_list.remove(directory+"\mask.py") #removes mask python file from image list to avoid error
		image_list.remove(directory+"\Thumbs.db") #removes file from image list to avoid error
		if (directory+"\/readme.md") in image_list:
			image_list.remove(directory+"\/readme.md") #removes file from image list to avoid error
	filepass(directory)
	return image_list, file_list



def round_corners_of_all_images(logo,color,wide):
	""" Saves a modfied version of each image in directory.
	
	Uses current directory if no directory is specified. 
	Places images in subdirectory 'modified', creating it if it does not exist.
	New image files are of type PNG and have transparent rounded corners.
	"""
	directory = None
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
		new_image = round_corners_one_image(curr_image,logo,color, wide) 
		
		# Save the altered image, suing PNG to retain transparency
		new_image_filename = os.path.join(new_directory, filename + '.png')
		new_image.save(new_image_filename)

