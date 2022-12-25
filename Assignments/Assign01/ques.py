import re
import collections
items = {}
data = []
plist = {}
pindex = {}
perindex = {}

def not_list(qry_list):
    base_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return list(set(base_list) - set(qry_list))

def and_lists(list1, list2):
    temp_list = [value for value in list1 if value in list2]
    return temp_list

def or_lists(list1, list2):
    temp_list = list1 + list2
    temp_list = set(temp_list)
    temp_list = sorted(temp_list)
    return temp_list

def permuterm_dict(plist):
    for key in plist.keys():
        pword = key+"$"
        for i in range(len(pword)):
            pword = pword[1:] + pword[0]
            pindex[pword] = key
    perindex = collections.OrderedDict(sorted(pindex.items()))
    return perindex

def list_merger(list1):
    list2 = []
    for i in range(list1):
        list2 = list2 + list1[i]
        list2 = set(list2)
        list2 = sorted(list2)
    return list2

def ishaving(string):
    for i in string:
        if i == "*":
            return True
    return False

def wildcard(ques_word):
    co = 0
    list1 = []
    list2 = []
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
                list1.append(plist[perindex[key]])
                print(perindex[key], plist[perindex[key]])
        list2 = list_merger(list1)
        return list2
    elif co == 2:
        if ques_word[0] == "*" and ques_word[-2:-1] == "*":
            ques_word = ques_word[1:] + ques_word[0]
            ques_word = ques_word[0:-3]
            ques_len = len(ques_word)
            for key in perindex.keys():
                if ques_word == key[0:ques_len]:
                    list1.append(plist[perindex[key]])
                    print(perindex[key], plist[perindex[key]])
            list2 = list_merger(list1)
            return list2
        else:
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
            list3 = []
            temp_list = and_lists(list1, list2)
            for temp in range(len(temp_list)):
                temp_list[temp] = str(temp_list[temp])
                list3.append(plist[temp_list[temp]])
                print(temp_list[temp], plist[temp_list[temp]])
            list3 = list_merger(list3)
            return list3
    else:
        print("Only upto two stars are being done!\n")

for i in range(1, 11):
    j = str(i)
    fp = open(j+".txt", 'r')
    line = fp.readline()
    data.append(re.split('\W+', line))
    fp.close()
    # print(data, len(data), len(data[i-1]))

    for k in range(len(data[i-1])):
        data[i - 1][k] = data[i - 1][k].casefold()
        if data[i-1][k] is not "":
            if data[i-1][k] in items.keys():
                items[data[i-1][k]].append(i-1)
            else:
                items[data[i-1][k]] = [i-1, ]

for key in items.keys():
    plist[key] = set(items[key])
    plist[key] = sorted(plist[key])

perindex = permuterm_dict(plist)

len_query = 0
type = 0
while(True):
    query = input("Enter your query with AND OR NOT:    ")
    query = query.casefold()
    words = query.split()
    if len(words) == 2:
        if words[0].casefold() == "not":
            word1, len_query = words[1], 2
            break
    elif len(words) == 3:
        if words[1].casefold() == "and" or words[1].casefold() == "or":
            word1, word2, len_query = words[0], words[2], 3
            break
    elif len(words) == 4:
        if (words[0].casefold() == "not") and (words[2].casefold() == "and" or words[2].casefold() == "or"):
            word1, word2, len_query, type = words[1], words[3], 4, 1
            break
        elif (words[2].casefold() == "not") and (words[1].casefold() == "and" or words[1].casefold() == "or"):
            word1, word2, len_query, type = words[0], words[3], 4, 2
            break
    elif len(words) == 5:
        if (words[0].casefold() == "not") and (words[2].casefold() == "and" or words[2].casefold() == "or") and (words[3].casefold() == "not"):
            word1, word2, len_query = words[1], words[4], 5
            break
    print("You have written a wrong query")

wcard1 = False
wcard2 = False

if (len_query == 2):
    wcard1 = ishaving(word1)
    for key in plist.keys():
        if wcard1 == True:
            list1 = wildcard(word1)
        else:
            if key.casefold() == word1.casefold():
                list1 = plist[key]
        print(list1, "\n")
        answer_list = not_list(list1)
else:
    wcard1 = ishaving(word1)
    wcard2 = ishaving(word2)
    for key in plist.keys():
        if wcard1 == True and wcard2 == True:
            list1 = wildcard(word1)
            list2 = wildcard(word2)
        if wcard1 == True:
            list1 = wildcard(word1)
            if key.casefold() == word2.casefold():
                list2 = plist[key]
        if wcard2 == True:
            if key.casefold() == word1.casefold():
                list1 = plist[key]
            list2 = wildcard(word2)
        else:
            if key.casefold() == word1.casefold():
                list1 = plist[key]
            if key.casefold() == word2.casefold():
                list2 = plist[key]
    print(list1, "\n",list2, "\n")
    if len_query == 3:
        if words[1].casefold() == "and":
            answer_list = and_lists(list1, list2)
        else:
            answer_list = or_lists(list1, list2)
    elif len_query == 4:
        if type == 1:
            if words[2].casefold() == "and":
                list1 = not_list(list1)
                answer_list = and_lists(list1, list2)
            else:
                list1 = not_list(list1)
                answer_list = or_lists(list1, list2)
        else:
            if words[1].casefold() == "and":
                list2 = not_list(list2)
                answer_list = and_lists(list1, list2)
            else:
                list2 = not_list(list2)
                answer_list = or_lists(list1, list2)
    else:
        if words[1].casefold() == "and":
            list1 = not_list(list1)
            list2 = not_list(list2)
            answer_list = and_lists(list1, list2)
        else:
            list1 = not_list(list1)
            list2 = not_list(list2)
            answer_list = or_lists(list1, list2)

print(answer_list)
