#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint
import ckan_api

### Problems to fix:
##  Not putting packages in groups
##  Write function for updating existing package


def make_pkg(data_dict):

    # Use json module to dump the dictionary to a string for posting.
    data_string = urllib.quote(json.dumps(data_dict))

    # Use package_create function to create new dataset.
    request = urllib2.Request('http://ckan.codefornova.org/api/3/action/package_create')

    # Creating a dataset requires an authorization header.
    # Replace *** with API key
    request.add_header('Authorization', ckan_api.myapi)

    # Make HTTP request.
    response = urllib2.urlopen(request, data_string)
    assert response.code == 200

    # Use the json module to load CKAN's response into a dictionary.
    response_dict = json.loads(response.read())
    assert response_dict['success'] is True

    # create_data returns the created package as its result.
    create_package = response_dict['result']
    pprint.pprint(create_package)

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

ind2_5_dict = {
    'name': 'foreclosure',
    'title': 'Foreclosure',
    'group': 'Meeting Basic Needs',
    'notes': 'Number of foreclosures by type of Real Estate',
}

ind2_6_dict = {
    'name': 'food-stamps',
    'title': 'Food Stamps',
    'group': 'Meeting Basic Needs',
    'notes': 'Number of SNAP (formerly Food Stamp) participants',
}

ind2_7_dict = {
    'name': 'school-lunch',
    'title': 'School Lunch',
    'group': 'Meeting Basic Needs',
    'notes': 'Number of students eligible for free and reduced-price school lunch',
}

#make_pkg(ind2_1_dict)
#make_pkg(ind2_2_dict)
make_pkg(ind2_3_dict)
#make_pkg(ind2_4_dict)
make_pkg(ind2_5_dict)
make_pkg(ind2_6_dict)
make_pkg(ind2_7_dict)
