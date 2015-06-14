#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint
import ckan_api

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