import re

string = "SATISFACTION years of  life, many, many life. Life. Many"


def count_word(text):
    filter_list = re.split('[ ,#.:()`~*/+_="!?\n]+', text.lower())

    dic = {}
    for word in reversed(filter_list):
        dic[word] = dic.get(word, 0) + 1
    return max(dic, key=dic.get)


print(count_word(string))
