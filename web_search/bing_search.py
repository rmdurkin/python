import urllib
import urllib2
import simplejson as json

def main():
    query = "python pandas"
    print(json.dumps(bing_search(query, 'Web'), sort_keys=True, indent=4 * ' '))

def bing_search(query, search_type):
    #search_type: Web, Image, News, Video
    key= '6CyL26NNsHE69WAFDwT2Awj7e7Y918EKV9OJS+KXDVQ'
    query = urllib.quote(query)
    # create credential for authentication
    user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
    credentials = (':%s' % key).encode('base64')[:-1]
    auth = 'Basic %s' % credentials
    url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/'+search_type+'?Query=%27'+query+'%27&$top=5&$format=json'
    request = urllib2.Request(url)
    request.add_header('Authorization', auth)
    request.add_header('User-Agent', user_agent)
    request_opener = urllib2.build_opener()
    response = request_opener.open(request)
    results = json.load(response)
    return results

if __name__ == "__main__":
    main()