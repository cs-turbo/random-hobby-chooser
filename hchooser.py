#-*- coding:utf-8 -*-

import os
import shutil
import random

HOBBIES_KEY = "/hobbies/"
TMP_KEY = "/tmp/"

rootpath = os.path.dirname(os.path.realpath(__file__))

hobbies = os.listdir(rootpath+HOBBIES_KEY)
hobbies_tmp = os.listdir(rootpath+TMP_KEY)

if len(hobbies_tmp) == 0:
	for hfile in hobbies:
		shutil.copyfile(rootpath+HOBBIES_KEY+hfile, rootpath+TMP_KEY+hfile)
		hobbies_tmp = os.listdir(rootpath+TMP_KEY)


choice = random.choice(hobbies_tmp)
choice_out = choice

if "." in choice_out:
	choice_out = choice_out.split(".")[0]

if "_" in choice_out:
	choice_out = choice_out.replace("_"," ")

print(choice_out.capitalize())

os.remove(rootpath+TMP_KEY+choice)

