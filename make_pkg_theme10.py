#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import json
import pprint
import ckan_api
from make_pkg import make_pkg


ind10_1 = {
    "name" : "air-quality",
    "title" : "Air Quality",
    "groups" : [{"name" : "cleanliness-and-beautification"}],
    "notes" : "Indicator: Number of “Air Quality Action” days per year. Source: Environmental Quality Commission",
}

ind10_2 = {
    "name" : "environmental-health",
    "title" : "Environmental Health",
    "groups" : [{"name" : "cleanliness-and-beautification"}],
    "notes" : "Indicator: Number of complaints to Environmental Health regarding perceived environmental hazards (mold, radon, toxic exposures, etc.) or pests (bedbugs, mosquitoes, ticks etc.). Source: Alexandria Health Department",
}

ind10_3 = {
    "name" : "recycling",
    "title" : "Recycling",
    "groups" : [{"name" : "cleanliness-and-beautification"}],
    "notes" : "Indicator: % of solid waste recycled. Source: Environmental Quality Commission",
}

make_pkg(ind10_1)
make_pkg(ind10_2)
make_pkg(ind10_3)