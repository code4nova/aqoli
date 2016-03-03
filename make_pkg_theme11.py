#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import json
import pprint
import ckan_api
from make_pkg import make_pkg


ind11_1 = {
    "name" : "median-household-income",
    "title" : "Median Household Income",
    "groups" : [{"name" : "employment-opportunities"}],
    "notes" : "Source: 2000 Decennial Census, 2005-2010 1-Year ACS Samples",
}

ind11_2 = {
    "name" : "workforce",
    "title" : "Workforce",
    "groups" : [{"name" : "employment-opportunities"}],
    "notes" : "Indicator: % population over 16 in workforce (same as labor force participation). Source: 2005-2010 1-Year ACS Samples",
}

ind11_3 = {
    "name" : "poverty",
    "title" : "Poverty",
    "groups" : [{"name" : "employment-opportunities"}],
    "notes" : "Indicator: % population below poverty level. Source: 2000 Decennial Census, 2005-2010 1-Year ACS Samples",
}

ind11_4 = {
    "name" : "graduation",
    "title" : "On-Time Graduation",
    "groups" : [{"name" : "employment-opportunities"}],
    "notes" : "Indicator: ACPS High School Graduation Rate. Source: Alexandria City Public Schools",
}
ind11_5 = {
    "name" : "unemployment",
    "title" : "Unemployment",
    "groups" : [{"name" : "employment-opportunities"}],
    "notes" : "Indicator: Unemployment at local level. Source: Bureau of Labor Statistics",
}

ind11_6 = {
    "name" : "hs-diploma",
    "title" : "High School Diploma",
    "groups" : [{"name" : "employment-opportunities"}],
    "notes" : "Indicator: % adults aged 25 and older with a high school diploma or GED. Source: 2000 Decennial Census, 2005-2010 1-Year ACS Samples",
}

ind11_7 = {
    "name" : "retail-occupancy",
    "title" : "Retail Occupancy",
    "groups" : [{"name" : "employment-opportunities"}],
    "notes" : "Indicator:  % Retail Occupancy. Source: Alexandria Economic Development Partnership. Contact: Christina Mindrup Robinson, Alexandria Economic Development Partnership, Mindrup@alexecon.org",
}

make_pkg(ind11_1)
make_pkg(ind11_2)
make_pkg(ind11_3)
make_pkg(ind11_4)
make_pkg(ind11_5)
make_pkg(ind11_6)
make_pkg(ind11_7)