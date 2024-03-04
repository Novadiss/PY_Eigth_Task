import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()
# print(root.tag)
# print(root.attrib)
# print(root.text)
# print(root.tail)
# print(root.attrib['version'])
# print(root.attrib['encoding'])
# print(root.attrib['standoff'])
news_xml = root.findall('channel/item')
words_list = []
for news in news_xml:
  description = news.find('description').text
  for w in description.split():
    if len(w) > 6:
      words_list.append(w)

duplicate_words = {}
for word in words_list:
    if word in duplicate_words:
      duplicate_words[word] += 1
    else:
      duplicate_words[word] = 1

sorted_words = sorted(duplicate_words.items(), key=lambda x: x[1], reverse=True)
for word in sorted_words[:10]:
  print(word[0], word[1])