""" get_all_foursquare_checkins.py - Downloads all your foursquare check-ins

Download all of your foursquare check-ins into a JSON file that's easily
handled by Splunk Storm's foursquare sourcetype.

Your User ID can be found under settings on the foursquare site.
Your access token (aka oauth token) can be found by logging in and visiting:
  https://developer.foursquare.com/docs/explore
"""

__author__ = "Ed Hunsinger"
__copyright__ = "Copyright 2013"
__email__ = "edrabbit@edrabbit.com"
# TODO(ed): Make the user_id, output path, and access token parameters

import foursquare
import json

user_id_to_fetch = 'YOUR USER ID'
output_file_path = 'output.log'
access_token = 'YOUR UNIQUE ACCESS TOKEN'

client = foursquare.Foursquare(access_token=access_token)
outfile = open(output_file_path, 'w')
all = client.users.all_checkins(user_id_to_fetch)
for c in all:
    json.dump(c, outfile)
    outfile.write(',\n')
outfile.close()