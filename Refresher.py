#####################################################
################   Function linking   ###############
#####################################################
# def funcA():
#     name = "Mohamed"
#     listing =["male", 28, "comsci"]
#     return name
#     return listing

# def funcB():
#     name = funcA()
#     print(name)

# funcB()

#####################################################
###################   OS Module   ###################
#####################################################
# import os
# os_help = dir(os)
# # for i in os_help:
# #     print (i)

# print(os.getcwd())
# print(os.listdir())
# #------------------------delete files
# os.remove("file")
# #------------------------Making Dir
# os.mkdir("one-piece")
# #------------------------Making Dirs within dir
# os.makedirs("one-piece/chap1")
# #------------------------join direc
# file_path = os.path.join(os.getcwd(),"text.txt")
# print(file_path)
# #------------------------grabbing file name only
# os.path.basename(....)
# #------------------------grabbing path only
# os.path.dirname(....)
# #------------------------split path from basename
# os.path.split(....)
# #------------------------split extention from path&basename
# os.path.splitext(....)
# #------------------------checking if exit or not
# os.path.exists(....)
# #------------------------checking if file or dir
# os.path.isdir(....)
# os.path.isfile(....)

#####################################################
##################   PIL Library   ##################
#####################################################
# from PIL import Image
# from io import BytesIO
# import requests

# r = requests.get(linkSrape)
# image = Image.open(BytesIO(r.content))
# image.save(pic_title + ".pdf")

#####################################################
###############     Natural Sort      ###############
#####################################################
# from natsort import natsorted
# natsorted(pdfs)

#####################################################
###############        PyPDF2         ###############
#####################################################
# import PyPDF2
# for i in (dir(PyPDF2.PdfFileReader.pageLayout())):
#     print(i)

# comic = PyPDF2.PdfFileMerger()
# for page in pdfs:
#     comic.append(page)

# comic.write("Comic1.pdf")
# comic.close()

#####################################################
###############     selenium          ###############
#####################################################
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
# driver.get(url_search)
# html = driver.page_source
# driver.quit()

#####################################################
###########     tqdm Progress Bar         ###########
#####################################################
# from tqdm import tqdm
# import time
# title = "One Piece Chapter 1"

# for i in tqdm(range(13), desc = title, leave = False):
#     time.sleep(0.5)

#####################################################
############     Del Selected Files      ############
#####################################################
# list_to_delete = [f for f in os.listdir(os.getcwd()) if "Page" in f]
# for h in list_to_delete:
#     os.remove(h)

#####################################################
############      lambda for sorting     ############
#####################################################
# title_array = sorted(title_array, key=lambda i:i["title"])

#####################################################
############                             ############
#####################################################

print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))