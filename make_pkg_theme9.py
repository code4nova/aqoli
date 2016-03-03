#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import json
import pprint
import ckan_api
from make_pkg import make_pkg


ind9_1 = {
    "name" : "fruits-and-vegetables",
    "title" : "Fruits and Vegetables",
    "groups" : [{"name" : "food-and-nutrition"}],
    "notes" : "Indicator: % adults who report eating 5 or more fruits/vegetables a day. Source: BRFSS",
}

ind9_3 = {
    "name" : "wic",
    "title" : "WIC Program Participation",
    "groups" : [{"name" : "food-and-nutrition"}],
    "notes" : "Indicator: % residents who access WIC program. Source: Virginia Department of Health http://www.vahealth.org/DCN/Reports/UI/Pages/DSReports.aspx",
}

ind9_4 = {
    "name" : "foodborne-illness-complaints",
    "title" : "Foodborne Illness Complaints",
    "groups" : [{"name" : "food-and-nutrition"}],
    "notes" : "Indicator: Average # of major deficiencies per food safety evaluation of food establishments in the city. Source: Alexandria Health Department",
}

make_pkg(ind9_1)
make_pkg(ind9_3)
make_pkg(ind9_4)