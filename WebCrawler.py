import urllib.request
import lxml.html

def getLinks(url,depth):
    print("Fetching links from " + url + "[" + str(depth) + "]")
    if(depth==0):
        return []
    else:
        try:
            connection = urllib.request.urlopen(url)
            dom =  lxml.html.fromstring(connection.read())
            # direct links
            links = dom.xpath('//a/@href')
        except:
            return []

        # collect the links from the links
        for url in links:
            links.extend(getLinks(url,depth-1))
        
        return links

print(getLinks("http://hp.lise-meitner-gymnasium.de",2))