import urllib2
import simplejson as json

url = ('https://ajax.googleapis.com/ajax/services/search/web'
       '?v=1.0&q=Python%20pandas&userip=50.42.26.89')

request = urllib2.Request(url, None, {'Referer': "robertdurkin.com"})
response = urllib2.urlopen(request)

# Process the JSON string.
results = json.load(response)

print(json.dumps(results, sort_keys=True, indent=4 * ' '))