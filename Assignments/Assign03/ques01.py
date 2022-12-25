import random
import numpy as np
from scipy import spatial

def split(string):
    table = {33:None, 34:None, 40:None, 41:None, 44:None, 45:None, 46:None, 47:None, 58:None, 59:None}
    string = string.translate(table)
    data = string.split()
    return data

def divide(list, num):
    for n in range(len(list)):
        list[n] = list[n]/num
    return list

def get_key(words, list):
    for key, value in words.items():
        if np.array_equal(list, value):
            return key
    return "None"


words = {}
doc = []
for i in range(1, 5):
    fp = open(str(i)+".txt", "r")
    line = fp.readline()
    doc.append(line)
    data = split(line)
    for word in data:
        snum = 0
        if word in words.keys():
            continue
        string = list(word)
        for num in range(len(string)):
            snum += ord(string[num])
        random.seed(snum)
        rnum = []
        for num in range(51):
            rnum.append(random.randrange(0, 1023, 1))
        ins_val = 0
        for num in range(1024):
            if num == 0:
                if num in rnum:
                    words[word] = [-1, ]
                    ins_val = 1
                else:
                    words[word] = [0, ]
                continue

            if num in rnum:
                if ins_val == 0:
                    ins_val = 1
                    words[word].append(-1)
                else:
                    ins_val = 0
                    words[word].append(1)
            else:
                words[word].append(0)

for i in range(1, 5):
    fp = open(str(i) + ".txt", "r")
    line = fp.readline()
    doc.append(line)
    data = split(line)
    for word in data:
        index = int(data.index(word))
        te_list = []
        if data.index(word) == 0:
            te_list = np.add(words[word], divide(words[data[index + 1]], 2))
            words[word] = np.add(te_list, divide(words[data[index + 2]], 4))
        elif data.index(word) == 1:
            te_list = np.add(words[word], divide(words[data[index + 1]], 2))
            te_list = np.add(te_list, divide(words[data[index - 1]], 2))
            words[word] = np.add(te_list, divide(words[data[index + 2]], 4))
        elif data.index(word) == (len(data) - 1):
            te_list = np.add(words[word], divide(words[data[index - 1]], 2))
            words[word] = np.add(te_list, divide(words[data[index - 2]], 4))
        elif data.index(word) == (len(data) - 2):
            te_list = np.add(words[word], divide(words[data[index + 1]], 2))
            te_list = np.add(te_list, divide(words[data[index - 1]], 2))
            words[word] = np.add(te_list, divide(words[data[index - 2]], 4))
        else:
            te_list = np.add(words[word], divide(words[data[index + 1]], 2))
            te_list = np.add(te_list, divide(words[data[index - 1]], 2))
            te_list = np.add(te_list, divide(words[data[index + 2]], 4))
            words[word] = np.add(te_list, divide(words[data[index - 2]], 4))

key_list = list(words.keys())
val_list = list(words.values())
for each_word in words.values():
    each_word = each_word.tolist()
    key1 = get_key(words, each_word)
    cos_val = {}
    results = {}
    final_list = []
    for word in words.values():
        word = word.tolist()
        val = 1 - spatial.distance.cosine(word, each_word)
        key = get_key(words, word)
        if key == key1:
            continue
        cos_val[key] = val
        results = sorted(cos_val.items(), key=lambda x:x[1], reverse=True)[:10]
    for result in results:
        final_list.append(result[0])
    print(key1, final_list, "\n")

