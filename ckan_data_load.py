#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint
import ckan_api

# Put the details of the dataset we're going to create into a dict.

dataset_dict = {
	'name': 'data2',
	'notes': 'Some more stuff',
}

# Use json module to dump the dictionary to a string for posting.
data_string = urllib.quote(json.dumps(dataset_dict))

# Use package_create function to create new dataset.
request = urllib2.Request(
    'http://ckan.codefornova.org/api/action/package_create'
)

# Creating a dataset requires an authorization header.
# Replace *** with API key
request.add_header('authorization', ckan_api.myapi)

# Make HTTP request.
response = urllib2.urlopen(request, data_string)
assert response.code == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())
assert response_dict['success'] is True

# package_create returns the created package as its result.
create_package = response_dict['result']
pprint.pprint(create_package)
