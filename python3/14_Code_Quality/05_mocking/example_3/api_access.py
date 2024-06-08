import requests


def api():
    response = requests.get("https://www.google.com/", timeout=60)
    return response.status_code
