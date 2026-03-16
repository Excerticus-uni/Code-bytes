import json
#import xmltodict


# Display XML
with open('books.xml', 'r') as xml_file:
    xml_content = xml_file.read()
    print(xml_content)


# Display JSON
with open('books.json', 'r') as json_file:
    data = json.load(json_file)
    #print(json.dumps(data, indent=4)