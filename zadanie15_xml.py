import xml.dom.minidom

DOM = xml.dom.minidom
doc = DOM.parse(open("xml_test.xml"))
x = doc.getElementsByTagName("hint")[0]
x.tagName = "note"
print(x.toxml("utf-8"))

plik = open('results.xml', 'w').write(str(x.toxml("utf-8")))
