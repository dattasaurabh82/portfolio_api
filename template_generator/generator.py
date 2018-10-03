import os
import json
import sys, getopt

# edit as per needs, it's based on my old portfolio structure. 
portfolio_elements = ["portfolio", "about", "blogs", "imgs_from_galleries", "resume", "waste_of_time", "works"]
portfolio = {}
aboutme = {}


# Change these according to your volume
number_of_exhibitons = 3 
number_of_talks = 3
number_of_teachings = 3
number_of_blogs = 5
number_of_works = 20



exhibition_struct = {
	"date": 2018,
	"project_name": " please fill in",
	"exhibition_name": "please fill in",
	"links":{
		"project_link": "please fill in",
		"exhibiton_link": "please fill in"
	},
	"collaborator": {
		"name": "please fill in",
		"link": "please fill in"
	}
}

talks_struct = {
	"Year": 2018, 
	"About": "please fill in", 
	"Name": "please fill in", 
	"Country": "please fill in"
}

contact_struct = {
	"mail": "please fill in",
	"mobile": "please fill in",
	"wechat:": "please fill in",
	"whatsapp:": "please fill in",
	"mastoden:": "please fill in",
	"twitter": "@please_fill_in",	
	"github": "www.github.com/please_fill_in",
	"public_key": ["please fill in"]
}

teachings_struct = "University/conference, city, country"

resume = {}
resume_struct = {
	"LinkedIn": "Please input your linkedin Link",
	"link": "Please fill in the link of the hosted pdf"
}

blogs = {}
blogs_struct = "Please fill in the link of a blog"

works = []
works_struct = {
	"Your project name": {
		"year": 2018,
		"month": "June",
		"video_link": " please fill in accordingly",
		"images": [
			"image1 link", 
			"image1 link", 
			"image1 link", 
			".."
		],
		"acknowledgement_text": "please be humble",
		"Hardware": [
			"Arduino", 
			"raspberry pi",
			 ".."
		],
		"Software": [ 
			"processing", 
			"python", 
			"shell scripts",
			"unity",
			"javascript", 
			".."
		],
		"tags": [
			"KinematicInstallation", 
			"Projection", 
			"Politics", 
			".."
		],
		"text": "please fill in accordingly"
	}
}

gallery_images = []
number_of_images = 10
gallery_images_structure = {
	"year": 2018,
	"month": "June",
	"image_link": "please fill in accordingly",
	"place_of_exhibition": "please fill in accordingly",
	"work": "please fill in project name",
	"work_link": "please fill in project link",
	"photographer": "please be respectful",
	"other_acknowledgement": "if you have any"
}



def makedir(intended_dir):
  try:
    os.makedirs(intended_dir)
  except OSError:
    pass

# def createJSONfilesInDirectories(_data_obj, )
def create_JSON_file(_file, obj):
	try:
		outfile = open(_file + "/" + _file + '.json', "w")
		outfile.write(json.dumps(obj, indent=4, sort_keys=True))
		outfile.close()
	except OSError:
		print("Couldn't write.. :(")
    	pass





def createAllDirs(_list_of_dirs):
	for _dirs in _list_of_dirs:
		# makedir("../public/"+_dirs)
		 makedir(_dirs)

def populate_portfolio_JSON(_dirs):
	for _dir in _dirs:
		portfolio[_dir] = "/"+_dir+".json"
	# print(portfolio)
	create_JSON_file(_dirs[0], portfolio)


def createAboutMeAPIStructure(_number_of_exhibitons, _number_of_talks, _number_of_teachings, _contact_struct):
	aboutme["text"] = "hjfgdhjfg"

	aboutme["exhibitions"] = []
	for x in range(_number_of_exhibitons):
		aboutme["exhibitions"].append(exhibition_struct)
	
	aboutme["talks"] = []
	for x in range(_number_of_talks):
		aboutme["talks"].append(talks_struct)

	aboutme["teachings"] = []
	for x in range(_number_of_teachings):
		aboutme["teachings"].append(teachings_struct)

	aboutme["contact"] = _contact_struct

	return aboutme

def populate_aboutme_JSON(_file_name, _number_of_exhibitons, _number_of_talks, _number_of_teachings, _contact_struct):
	createAboutMeAPIStructure(_number_of_exhibitons, _number_of_talks, _number_of_teachings, _contact_struct)
	create_JSON_file(_file_name, aboutme)

def populate_resume_JSON(_file_name):
	resume = resume_struct
	create_JSON_file(_file_name, resume)


def createBlogsStructure(_number_of_blogs):
	blogs["links"] = []
	for x in range(_number_of_blogs):
		blogs["links"].append(blogs_struct)
	return blogs

def populate_blogs_JSON(_file_name, _number_of_blogs):
	createBlogsStructure(_number_of_blogs)
	create_JSON_file(_file_name, blogs)


def createWorksAPIStructure(_number_of_works):
	for x in range(_number_of_works):
		works.append(works_struct)
	# print(works)
	return works

def populate_works_JSON(_file_name, _number_of_works):
	createWorksAPIStructure(_number_of_works)
	create_JSON_file(_file_name, works)


def createGalleryImagesAPIStructure(_number_of_images):
	for x in range(_number_of_images):
		gallery_images.append(gallery_images_structure)

	return gallery_images

def populate_gallery_images_JSON(_file_name, _number_of_images):
	createGalleryImagesAPIStructure(_number_of_images)
	create_JSON_file(_file_name, gallery_images)



if __name__ == "__main__":
	createAllDirs(portfolio_elements)
	populate_portfolio_JSON(portfolio_elements)
	populate_aboutme_JSON(portfolio_elements[1], number_of_exhibitons, number_of_talks, number_of_teachings, contact_struct)
	populate_resume_JSON(portfolio_elements[4])
	populate_blogs_JSON(portfolio_elements[2], number_of_blogs)
	populate_works_JSON(portfolio_elements[6], number_of_works)
	populate_gallery_images_JSON(portfolio_elements[3], number_of_images)
