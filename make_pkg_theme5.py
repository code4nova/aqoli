#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import json
import pprint
import ckan_api
from make_pkg import make_pkg


ind5_1 = {
    "name" : "walk-work",
    "title" : "Percent of Residents Walking to Work",
    "groups" : [{"name" : "built-environment"}],
    "notes" : "Indicator: % of residents walking to work. Source: ACS, 2005-2010, 1-year samples",
}

ind5_2 = {
    "name" : "bike-work",
    "title" : "Percent of Residents Biking to Work",
    "groups" : [{"name" : "built-environment"}],
    "notes" : "Indicator: % of residents walking/biking to work. Source: ACS, 2005-2010, 1-year samples",
}

ind5_3 = {
    "name" : "tree-canopy",
    "title" : "Percent Tree Canopy Coverage",
    "groups" : [{"name" : "built-environment"}],
    "notes" : "Indicator: % tree canopy coverage. Source: Virginia Department of Health, Health Profile, Alexandria City, 2000-2009",
}

ind5_4 = {
    "name" : "shared-use-paths",
    "title" : "Shared Use Paths",
    "groups" : [{"name" : "built-environment"}],
    "notes" : "Indicator: Total miles of designated shared-use paths and bike lanes relative to total street miles (Revised from Strategic Plan Indicator). Source: Carrie Sanders, City of Alexandria ",
}

ind5_6 = {
    "name" : "public-transport",
    "title" : "Percent of Residents Taking Public Transport to Work",
    "groups" : [{"name" : "built-environment"}],
    "notes" : "Indicator: % residents who take public transportation to work. Source: ACS 1-Year Sample, Selected Economic Characteristics (DP03)",
}

make_pkg(ind5_1)
make_pkg(ind5_2)
make_pkg(ind5_3)
make_pkg(ind5_4)
make_pkg(ind5_6)