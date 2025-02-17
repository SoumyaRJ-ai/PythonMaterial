# /usr/bin/python3
"""
Purpose:
    Breaking News Notifications for every one minute
"""
from time import sleep

import pynotify
import requests
from scrapy.selector import HtmlXPathSelector


def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return


url = "http://www.thehindu.com/"
while True:
    r = requests.get(url, timeout=5)
    while r.status_code != 200:
        r = requests.get(url, timeout=5)

        response = r.text
        xxs = HtmlXPathSelector(text=response)
        news = "\n".join(
            xxs.select('//div[@class="breakingNews_list"]//h3/a/text()').extract()[:6]
        )
        sendmessage("Breaking News", news)
        sleep(10)
