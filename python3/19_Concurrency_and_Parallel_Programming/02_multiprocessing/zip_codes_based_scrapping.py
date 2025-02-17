"""
Purpose: scrap zip code based information from google maps
"""

import time
from multiprocessing.dummy import Pool

import requests
from datadiff import diff


def getzip(code):
    try:
        code = str(code)
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={code}"
        res = requests.get(url, timeout=60).json()["results"]
        if len(res) < 1:  # Re-try
            print("Retrying")
            return getzip(code)
        iszip = "postal_code" in res[0]["types"] and "United States" in str(
            res[0]["address_components"]
        )
    except Exception as e:
        print("In error", e)
        iszip = False
    return (code, iszip)


ziprange = range(94400, 94420)
print("Range is: " + str(len(ziprange)))

print("Using one thread")
start = time.time()
syncres = [getzip(c) for c in ziprange]
print("took " + str(time.time() - start))

print("Using multiple threads")
start = time.time()

# Magic
pool = Pool(10)
asyncres = pool.map(getzip, ziprange)
pool.close()
pool.join()
asyncres = sorted(asyncres)
# End of Magic

print("took " + str(time.time() - start))

# Make sure results are equal
d = diff(syncres, asyncres)
if len(d.diffs) > 0:
    print("diff is", d)

for r in asyncres:
    print("Zip code {} is {} US code".format(r[0], "valid" if r[1] else "invalid"))
