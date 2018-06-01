import urllib.request
import urllib.parse
import urllib
import re
import simplejson


def search(SEARCH):
    if "https://www.youtube.com/watch?v=" in SEARCH:
        return str(SEARCH)
    else:
        query_string = urllib.parse.urlencode({"search_query" : str(SEARCH)})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        print("Best Result: " + "http://www.youtube.com/watch?v=" + search_results[0])
        return str("http://www.youtube.com/watch?v=" + search_results[0])

def getResults(SEARCH):
    if "https://www.youtube.com/watch?v=" in SEARCH:
        return str(SEARCH)
    else:
        query_string = urllib.parse.urlencode({"search_query" : str(SEARCH)})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        print(search_results[0:5])
        for c in search_results[0:5]:
            id = str(c)
            url = 'http://gdata.youtube.com/feeds/api/videos/%s?alt=json&v=2' % id

            print(str(url))
        return search_results[0:5]


















