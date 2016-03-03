import urllib2
import urllib
import json
import pprint
import ckan_api

def update_grp(name,description):

    group_dict = {
        "name" : name,
        "description" : description
    }

    # Use json module to dump the dictionary to a string for posting.
    data_string = urllib.quote(json.dumps(group_dict))

    # Use package_create function to create new dataset.
    request = urllib2.Request(
        'http://ckan.codefornova.org/api/action/group_update'
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

    # update_group returns the updated group as its result.
    update_group = response_dict['result']
    return update_group
    pprint.pprint(update_group)