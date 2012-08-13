#!/usr/bin/env python
from bs4 import BeautifulSoup
import sys

def packageList(groupname):
        return (filter( (lambda x: x.string == groupname), bs.findAll('id')))[0].parent.packagelist.stripped_strings

handle = open('comps/comps-f17.xml.in', 'r')
xml = handle.read()
bs = BeautifulSoup(xml, "xml")

packages = set()
for group in sys.argv[1:]:
	packages |= set(packageList(group))

print packages
