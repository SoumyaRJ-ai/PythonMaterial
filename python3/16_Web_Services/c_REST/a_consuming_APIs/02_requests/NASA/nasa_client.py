# -*- coding: utf-8 -*-
from pprint import pprint

import requests

# TO get API key, sign-up at https://api.nasa.gov/index.html#apply-for-an-api-key
NASA_API_KEY = "jdm0WrfEUq3rfZnUP8XYhvAU7QEnG7SUNY1lmiHP"

# NASA API documentation: https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf

API_ROOT = "https://images-api.nasa.gov"

# API End-points
SEARCH_ENDPOINT = "/search"
ASSET_ENDPOINT = "/asset/{nasa_id}"
METADATA_ENDPOINT = "/metadata/{nasa_id}"
CAPTIONS_ENDPOINT = "/captions/{nasa_id}"
ALBUM_ENDPOINT = "/album/{album_name}"


request_params = {
    "q": "apollo 11",
    "description": "moon landing",
    "media_type": "image",
}

URL = API_ROOT + SEARCH_ENDPOINT
response = requests.get(URL, params=request_params, timeout=60)
# pprint(response.json())
with open("nasa_search_response.json", "w") as f:
    f.write(response.text)
    f.close()

# media details
URL = API_ROOT + ASSET_ENDPOINT.format(nasa_id="as11-40-5874")
response = requests.get(URL, timeout=60)
pprint(response.json())
response_data = response.json()

image_urls = [response_data.get("collection").get("href")]
for each in response_data.get("collection").get("items"):
    image_urls.append(each.get("href"))

for each_image_url in image_urls:
    response_image = requests.get(each_image_url, timeout=60)
    image_name = each_image_url.split("/")[-1]
    if response.headers["content-type"] == "application/json":
        with open(f"{image_name}", "wb") as g:
            g.write(response_image.content)
            g.close()

# image of day: https://api.nasa.gov/planetary/apod?api_key=jdm0WrfEUq3rfZnUP8XYhvAU7QEnG7SUNY1lmiHP

# Ref: https://www.blog.pythonlibrary.org/2019/04/18/creating-a-gui-application-for-nasas-api-with-wxpython/
