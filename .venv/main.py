import json

with open("newsafr.json", encoding="utf-8") as f:
    json_data = json.load(f)

news_list = json_data["rss"]["channel"]["items"]
words_list = []
for news in news_list:
    words = news["description"].split(" ")
    for word in words:
        if len(word) > 6:
            words_list.append(word)

duplicate_words = {}
for word in words_list:
    if word in duplicate_words:
        duplicate_words[word] += 1
    else:
        duplicate_words[word] = 1

sorted_words = sorted(duplicate_words.items(), key=lambda x: x[1], reverse=True)
for word in sorted_words[:10]:
    print(word[0], word[1])