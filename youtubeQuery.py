import urllib.request
import urllib.parse
import urllib
import re
import lxml
from lxml import etree

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
    results_return = []
    if "https://www.youtube.com/watch?v=" in SEARCH:
        return str(SEARCH)
    else:
        query_string = urllib.parse.urlencode({"search_query" : str(SEARCH)})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        for c in search_results[0:5]:
            id = str(c)
            youtube = etree.HTML(urllib.request.urlopen("http://www.youtube.com/watch?v=" + (str(id))).read())
            video_title = youtube.xpath("//span[@id='eow-title']/@title")
            print(str(''.join(video_title)))
            results_return.append((str(''.join(video_title))))

    return(results_return[0:5])



















