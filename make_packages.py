#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint
import ckan_api
from make_pkg import make_pkg

#homeless_dict = {
#	"name" : "homeless",
#	"title" : "Number of Homeless Persons",
#	"notes" : "Number of homeless persons, in shelter and out of shelter",
#	"author" : "Sources: Alexandria Homeless Services Coordinating Committee (HSCC); 2011 Count of Homeless Persons in Metropolitan Washington http://www.mwcog.org/uploads/pub-documents/p15eXlo20110512131909.pdf",
#    "url" : "http://www.mwcog.org/uploads/pub-documents/p15eXlo20110512131909.pdf",
#    "groups" : "meeting_basic_needs",
#}

#ind2_1_dict = {
#    "name" : "median-costs",
#    "title" : "Median Owner Costs",
#    "group" : "Meeting Basic Needs",
#    "notes" : "Median owner costs as percent of income past 12 months",
#}

ind2_3_dict = {
    "name" : "affordable-housing",
    "title" : "Affordable Housing Availability",
    "group" : "Meeting Basic Needs",
    "notes" : "Number of housing units available for households earning below 50 or 60 percent of median income",
}

ind2_4_dict = {
    "name" : "median-gross-rent",
    "title" : "Median Rent",
    "group" : "Meeting Basic Needs",
    "notes" : "Median gross rent",
}

ind2_5_dict = {
    "name" : "foreclosure-by-type",
    "title" : "Foreclosure",
    "group" : "Meeting Basic Needs",
    "notes" : "Number of foreclosures by type of Real Estate",
}

ind2_6_dict = {
    "name" : "snap",
    "title" : "Food Stamps",
    "group" : "Meeting Basic Needs",
    "notes" : "Number of SNAP (formerly Food Stamp) participants",
}

ind2_7_dict = {
    "name" : "school-lunch-elig",
    "title" : "School Lunch",
    "group" : "Meeting Basic Needs",
    "notes" : "Number of students eligible for free and reduced-price school lunch",
}

#make_pkg(ind2_1_dict)
make_pkg(ind2_3_dict)
make_pkg(ind2_4_dict)
make_pkg(ind2_5_dict)
make_pkg(ind2_6_dict)
make_pkg(ind2_7_dict)