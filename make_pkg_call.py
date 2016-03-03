#!/usr/bin/env python
import urllib
import json
import pprint
import ckan_api
import upload_pkgs


#ind2_1_dict = {
#    'name': 'median-owner-costs',
#    'title': 'Median Owner Costs',
#    'group': 'Meeting Basic Needs',
#    'notes': 'Median owner costs as percent of income past 12 months',
#}

#ind2_2_dict = {
#    'name': 'homeless',
#    'title': 'Homeless',
#    'group': 'Meeting Basic Needs',
#    'notes': 'Number of homeless persons (in shelter and out of shelter)',
#}

ind2_3_dict = {
    'name': 'affordable-housing-availability',
    'title': 'Affordable Housing Availability',
    'group': 'Meeting Basic Needs',
    'notes': 'Number of housing units available for households earning below 50% or 60% of median income',
}

#ind2_4_dict = {
#    'name': 'median-rent',
#    'title': 'Median Rent',
#    'group': 'Meeting Basic Needs',
#    'notes': 'Median gross rent',
#}

#ind2_5_dict = {
#    'name': 'foreclosure',
#    'title': 'Foreclosure',
#    'group': 'Meeting Basic Needs',
#    'notes': 'Number of foreclosures by type of Real Estate',
#}

#ind2_6_dict = {
#    'name': 'food-stamps',
#    'title': 'Food Stamps',
#    'group': 'Meeting Basic Needs',
#    'notes': 'Number of SNAP (formerly Food Stamp) participants',
#}

#ind2_7_dict = {
#    'name': 'school-lunch',
#    'title': 'School Lunch',
#    'group': 'Meeting Basic Needs',
#    'notes': 'Number of students eligible for free and reduced-price school lunch',
#}

ind_test_dict = {
    'name': 'test-pkg',
    'title': 'test this!',
    'group': 'Built Environment',
    'notes': 'hope this works!!!',
}

upload_pkgs.make_pkg(ind_test_dict)

#make_pkg(ind2_1_dict)
#make_pkg(ind2_2_dict)
#make_pkg(ind2_3_dict)
#make_pkg(ind2_4_dict)
#make_pkg(ind2_5_dict)
#make_pkg(ind2_6_dict)
#make_pkg(ind2_7_dict)
