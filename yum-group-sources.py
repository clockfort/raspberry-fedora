#!/usr/bin/env python3
from bs4 import BeautifulSoup
import sys
import subprocess
from subprocess import (CalledProcessError, check_call)
import os
import os.path

def packageList(groupname):
        return bs.find('id', text=groupname).parent.packagelist.stripped_strings

def exist(directory):
	if( not os.path.exists(directory) ):
		os.mkdir(directory)

with open('comps/comps-f17.xml.in') as xml:
    bs = BeautifulSoup(xml, "xml")

packages = set()
for group in sys.argv[1:]:
	packages |= set(packageList(group))

for package in packages:
	try:
		print("Downloading "+package+" SRPM...   ",end='')
		exist("SRPMs")
		subprocess.check_call("yumdownloader --destdir=SRPMs/ --source "+package, shell=True, stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
		print("[ "+'\033[92m'+"OK"+'\033[0m'+" ]")

	except CalledProcessError:
		print("[ "+'\033[93m'+"FAILED"+'\033[0m'+" ]")

