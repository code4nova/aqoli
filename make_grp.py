#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint
import ckan_api

def make_grp(name,title):

    group_dict = {
        'name': name,
        'title': title
    }

    # Use json module to dump the dictionary to a string for posting.
    data_string = urllib.quote(json.dumps(group_dict))

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
    return create_group
    pprint.pprint(create_group)

make_grp('diversity','Diversity')
#make_grp('diverse_community','Diverse Community')
#make_grp('access_to_health_care','Access to Health Care')
#make_grp('built_environment','Built Environment')
#make_grp('cleanliness_and_beautification','Cleanliness and Beautification')
#make_grp('crime_and_safety','Crime and Safety')
#make_grp('employment_opportunities','Employment Opportunities')
#make_grp('food_and_nutrition','Food and Nutrition')
#make_grp('mental_health','Mental Health')
#make_grp('sense_of_community','Sense of Community')
#make_grp('substance_abuse_prevention','Substance Abuse Prevention')
#make_grp('meeting_basic_needs','Meeting Basic Needs')
<<<<<<< HEAD
make_grp('bananas', 'Bananas Rule!')
=======
>>>>>>> c6382b6e6f002cf577a0f7cf581eaf6e93a8e50c
