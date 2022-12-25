from collections import OrderedDict
import random
import math

def split(string):
    table = {33:None, 34:None, 40:None, 41:None, 44:None, 45:None, 46:None, 47:None, 58:None, 59:None}
    string = string.translate(table)
    data = string.split()
    return data

words = {}
doc = []

def find_sim(query, doc):
    inter = [value for value in query if value in doc]
    num = len(inter)
    qu_mod = math.sqrt(len(query))
    doc_mod = math.sqrt(len(doc))
    den = qu_mod*doc_mod
    sim = num/den
    return sim

for i in range(1, 101):
    fp = open(str(i)+".txt", "r")
    line = fp.readline()
    doc.append(line)
    data = split(line)
    for word in data:
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 1

sort_words = OrderedDict(sorted(words.items(), key=lambda x: x[1]))
# print(words)
least_occ = {k: sort_words[k] for k in list(sort_words)[:20]}
most_occ = {k: sort_words[k] for k in list(sort_words)[-20:]}
rand_occ = {}
for i in range(20):
    a, b = random.choice(list(sort_words.items()))
    rand_occ[a] = b

# print(least_occ, "\n", most_occ, "\n", rand_occ)

for num in range(10):
    a = random.choice(list(least_occ.keys()))
    b = random.choice(list(most_occ.keys()))
    c = random.choice(list(rand_occ.keys()))
    que_list = []
    max_sim = 0
    for doc_num in range(len(doc)):
        docu = split(doc[doc_num])
        sim = find_sim([a, b, c], docu)
        que_list.append(sim)
        if max_sim < sim:
            max_sim = sim
            docnum = doc_num
    print(str([a, b, c]) + " is similar to " + str(docnum) + " document number\n" + str(doc[docnum]) + "\n")