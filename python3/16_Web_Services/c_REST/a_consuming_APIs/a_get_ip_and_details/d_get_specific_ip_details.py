#!/usr/bin/python
"""
Purpose: Get IP details of specifc given IP address

    https://ipapi.co/api/{#location-of-a-specific-ip}/{# output format}
"""
import os
import urllib.request


def print_n_write_response(ip_address, output_format):
    url = "https://ipapi.co/{ip}/{format}/".format(ip=ip_address, format=output_format)

    connection = urllib.request.urlopen(url)
    data = connection.read()
    write_response_to_file(data, output_format)
    print(data.decode("utf-8"))


def write_response_to_file(data, extension_name):
    dirname = os.path.splitext(os.path.relpath(__file__))[0]
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    with open(dirname + os.sep + "response." + extension_name, "wb") as f:
        f.write(data)
        f.close()


if __name__ == "__main__":
    print("-" * 20)
    print("JSON response")
    print_n_write_response("24.61.88.57", "json")
    print()

    print("-" * 20)
    print("JSONP response")
    print_n_write_response("24.61.88.57", "jsonp")
    print()

    print("-" * 20)
    print("XML response")
    print_n_write_response("24.61.88.57", "xml")
    print()

    print("-" * 20)
    print("CSV response")
    print_n_write_response("24.61.88.57", "csv")
    print()

    print("-" * 20)
    print("YAML response")
    print_n_write_response("24.61.88.57", "yaml")
    print()
