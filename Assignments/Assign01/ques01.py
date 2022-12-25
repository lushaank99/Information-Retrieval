import re
items = {}
data = []
plist = {}

# This question gives the use of 'and' 'or' 'not' operations with query
# Eg: not a and not the

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

# print(items, "\n", plist)
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
list1 = []
list2 = []
print (word1, "\n", word2)
if (len_query == 2):
    for key in plist.keys():
        if key.casefold() == word1.casefold():
            list1 = plist[key]
            print(list1, "\n")
            answer_list = not_list(list1)
else:
    for key in plist.keys():
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