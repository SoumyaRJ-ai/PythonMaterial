import urllib.error
import urllib.parse
import urllib.request

urls = ["http://google.com", "http://nytimes", "http://CNN.com"]

i = 0

while i < len(urls):
    htmlfile = urllib.request.urlopen(urls[i])
    htmltext = htmlfile.read()
    print((htmltext[0:100]))
    i += 1
