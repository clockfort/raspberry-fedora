#!/usr/bin/python
from bs4 import BeautifulSoup
import sys

def packageList(groupname):
        return bs.find('id', text=groupname).parent.packagelist.stripped_strings

handle = open('comps/comps-f17.xml.in', 'r')
xml = handle.read()
bs = BeautifulSoup(xml, "xml")

packages = set()
for group in sys.argv[1:]:
	packages |= set(packageList(group))

print packages
