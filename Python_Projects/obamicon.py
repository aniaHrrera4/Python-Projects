# skeleton code for obamicon 
from PIL import Image
# =============================================================== 
# define colors as variables so we can recall them later: 


dark_blue = (0, 51, 76) 
red = (217, 26, 33) 
light_blue = (112, 150, 158) 
yellow = (252, 227, 166)

# =============================================================== 
# define a function that obama-fies the image. 
# this function will take your images' pixel list as a parameter. 
# for each pixel in your image's pixel list, "obama-fy" it by 
# creating a new RGB value (dark blue, red, light blue, or yellow) 
# based on the intensity of that pixel. return a pixel list 
# containing the RGB values of the obamafied picture. 
width,height= im.size
print(data)
data_list=list(data)

def obamafy(image_data):
	obamafied_pixel_list=[] # BEHAVIOR UNDEFINED 
	for i in pixel_list:
		red=i[0]
		green=i[1]
		blue=i[2] 
		total=red+green+blue
		if total<182:
			obamafied_pixel_list.append(dark_blue)
		elif total<364:
			obamafied_pixel_list.append(red)
		elif total<546
			obamafied_pixel_list.append(light_blue)
		else:
			obamafied_pixel_list.append(yellow)

# =============================================================== 
# ask the user for the image name and open the image 
# ===============================================================
my_image= Image.open("space.jpg") # UNDEFINED
# =============================================================== 
# convert the image into a list of pixel RGB values 
# =============================================================== 

# UNDEFINED
# =============================================================== 
# obamafy your image by calling your function 
# =============================================================== 
obamafied_pixels = obamafy(image_data)
# =============================================================== 
# create a new image and copy the new obama-fied pixel list into the image 
# =============================================================== 
obamafied_image = Image.new # UNDEFINED
# =============================================================== 
# finally, show and save the image 
# ===============================================================