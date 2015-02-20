#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint
import ckan_api

# Put the details of the dataset we're going to create into a dict.

group_dict1 = {
  'name': 'access-to-health-care',
  'title': 'Access to Health Care'
}

group_dict2 = {
  'name': 'basic-needs',
  'title': 'Basic Needs'
}

group_dict3 = {
  'name': 'built-environment',
  'title': 'Built Environment'
}

group_dict4 = {
  'name': 'cleanliness-and-beautification',
  'title': 'Cleanliness and Beautification'
}

group_dict5 = {
  'name': "crime-and-safety",
  'title': 'Crime and Safety'
}

group_dict6 = {
  'name': "diversity",
  'title': 'Diversity'
}

group_dict7 = {
  'name': "employment-opportunities",
  'title': 'Employment Opportunities'
}

group_dict8 = {
  'name': "food-and-nutrition",
  'title': 'Food and Nutrition'
}

group_dict9 = {
  'name': "mental-health",
  'title': 'Mental Health'
}

group_dict10 = {
  'name': "sense-of-community",
  'title': 'Sense of Community'
}

group_dict11 = {
  'name': "substance-abuse-prevention",
  'title': 'Substance Abuse Prevention'
}

groups_dict = ['group_dict1', 'group_dict2']

for i in range(len(groups_dict)):
    # Use json module to dump the dictionary to a string for posting.
    data_string = urllib.quote(json.dumps(i))

    # Use package_create function to create new dataset.
    request = urllib2.Request(
        'http://ckan.codefornova.org/api/action/group_create'
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

    # group_create returns the created group as its result.
    create_group = response_dict['result']
    pprint.pprint(create_group)
