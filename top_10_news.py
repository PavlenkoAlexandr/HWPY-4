import json
import xml.etree.ElementTree as ET

def top_10_words(str_):
    words_list = str_.split()
    words_dict = dict()
    for word in words_list:
        if len(word) > 6:
            words_dict[word] = words_list.count(word)
    descriptions_sorted = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
    return descriptions_sorted[:10]

with open('newsafr.json', encoding='utf-8') as f:
    json_data = json.load(f)

descriptions = json_data['rss']['channel']['items']
json_descriptions = str()

for description in descriptions:
    json_descriptions += str(description['description']).lower()
    json_descriptions.replace('[', '')
    json_descriptions.replace(']', '')

print(top_10_words(json_descriptions))


parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()

items = root.findall('channel/item')
xml_descriptions = str()
for item in items:
    xml_descriptions += item.find('description').text.lower()

print(top_10_words(xml_descriptions))
