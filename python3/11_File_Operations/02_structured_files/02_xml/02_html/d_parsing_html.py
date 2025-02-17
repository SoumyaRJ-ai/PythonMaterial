#!/usr/bin/python
"""
Purpose: Parsing html using lxml
"""
from io import StringIO

import lxml.etree
from lxml import etree

# Feeding RAW XML for Serialisation
html = etree.XML(
    "<html><head>Head of HTML</head><title>I am the title!</title><body>Here is the body</body></html>"
)
print(etree.tostring(html, pretty_print=True).decode("utf-8"))


html = etree.XML(
    "<html><head>Head of HTML</head><title>I am the title!</title><body>Here is the body</body></html>"
)
print(etree.tostring(html, pretty_print=True, xml_declaration=True).decode("utf-8"))


# The parse() function can be used to parse from files and file-like objects
title = StringIO("<title>Title Here</title>")
tree = etree.parse(title, parser=lxml.etree.XMLParser(resolve_entities=False))
print(etree.tostring(tree).decode("utf-8"))


# The fromstring() function can be used to parse Strings:
title = "<title>Title Here</title>"
root = etree.fromstring(title, parser=lxml.etree.XMLParser(resolve_entities=False))
print(root.tag)
print(etree.tostring(root).decode("utf-8"))


# The fromstring() function can be used to write XML literals directly into the source:
title = etree.XML("<title>Title Here</title>")
print(title.tag)
print(etree.tostring(title).decode("utf-8"))
