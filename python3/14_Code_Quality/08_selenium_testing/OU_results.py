#!/usr/bin/python
"""
Purpose: TO get the  OU examination results

http://www.osmania.ac.in/res07/20180472.jsp

Hall ticket numbers
	160314732001, 160314732005
"""

from pprint import pprint

import requests

response = requests.post("http://www.osmania.ac.in/res07/20180472.jsp", timeout=60)

print(response.text)
