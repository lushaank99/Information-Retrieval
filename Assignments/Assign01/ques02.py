import re
import collections
items = {}
data = []
plist = {}
pindex = {}
perindex = {}

# This question gives answer to a single wildcard query of * with atmost 2 *'s in query
# Eg: s*t*n

for i in range(1, 11):
    j = str(i)
    fp = open(j+".txt", 'r')
    line = fp.readline()
    data.append(re.split('\W+', line))
    fp.close()
    for k in range(len(data[i-1])):
        data[i-1][k] = data[i-1][k].casefold()
        if data[i-1][k] is not "":
            if data[i-1][k] in items.keys():
                items[data[i-1][k]].append(i-1)
            else:
                items[data[i-1][k]] = [i-1, ]

for key in items.keys():
    plist[key] = set(items[key])
    plist[key] = sorted(plist[key])

# print(items, "\n", plist)

def same_entities(list1, list2):
    temp_list = [value for value in list1 if value in list2]
    return temp_list

def permuterm_dict(plist):
    for key in plist.keys():
        pword = key+"$"
        for i in range(len(pword)):
            pword = pword[1:] + pword[0]
            pindex[pword] = key
    perindex = collections.OrderedDict(sorted(pindex.items()))
    return perindex

def wildcard(ques_word):
    co = 0
    for c in ques_word:
        if c == "*":
            co += 1
    if co == 1:
        for i in range(len(ques_word)):
            if ques_word[-1:] == "*":
                break
            else:
                ques_word = ques_word[-1:] + ques_word[:-1]
        ques_word = ques_word[:-1]
        ques_len = len(ques_word)
        # print(type(ques_word))
        for key in perindex.keys():
            if ques_word == key[0:ques_len]:
                print(perindex[key], plist[perindex[key]])
    elif co == 2:
        if ques_word[0] == "*" and ques_word[-2:-1] == "*":
            ques_word = ques_word[1:] + ques_word[0]
            ques_word = ques_word[0:-3]
            ques_len = len(ques_word)
            for key in perindex.keys():
                if ques_word == key[0:ques_len]:
                    print(perindex[key], plist[perindex[key]])
        else:
            list1 = []
            list2 = []
            word1, word2 = ques_word, ques_word
            for i in range(len(word1)):
                if word1[-1:] == "*":
                    break
                else:
                    word1 = word1[-1:] + word1[:-1]
            ques_len = 0
            for c in word1:
                if c == "*":
                    break
                ques_len += 1
            word1 = word1[:ques_len]
            for key in perindex.keys():
                if word1 == key[0:ques_len]:
                    list1.append(perindex[key])

            for i in range(len(word2)):
                if word2[-1:] == "*":
                    break
                else:
                    word2 = word2[1:] + word2[0]
            ques_len = 0
            for c in word2:
                if c == "*":
                    break
                ques_len += 1
            word2 = word2[:ques_len]
            for key in perindex.keys():
                if word2 == key[0:ques_len]:
                    list2.append(perindex[key])

            temp_list = same_entities(list1, list2)
            for temp in range(len(temp_list)):
                temp_list[temp] = str(temp_list[temp])
                print(temp_list[temp], plist[temp_list[temp]])
    else:
        print("Only upto two stars are being done!\n")


query = input("Enter a wildcard word with a * for starters  ")
ques_word = query + "$"
ques_word = ques_word.casefold()

perindex = permuterm_dict(plist)
wildcard(ques_word)