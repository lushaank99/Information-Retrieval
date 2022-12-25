import math

def split(string):
    table = {44: None}
    string = string.translate(table)
    data = string.split()
    return data

def jaccard_score(qry, doc):
    data1 = split(qry)
    data2 = split(doc)
    inter = [value for value in data1 if value in data2]
    uni = list(set(data1) | set(data2))
    jacc = len(inter)/len(uni)
    return jacc

def log_termweight(qry, doc):
    data1 = split(qry)
    data2 = split(doc)
    tw = 0
    for item1 in data1:
        c = 0
        for item2 in data2:
            if item1 == item2:
                c += 1
        if c != 0:
            tw += 1 + math.log(c, 10)
    return tw


q1 = "information on cars"
q2 = "information on cars"
q3 = "red cars and red trucks"

d1 = "all you've ever wanted to know about cars"
d2 = "information on trucks, information on planes, information on trains"
d3 = "cops stop red cars more often"

js1 = jaccard_score(q1, d1)
js2 = jaccard_score(q2, d2)
js3 = jaccard_score(q3, d3)

print(js1, js2, js3, "\n")

tw1 = log_termweight(q1, d1)
tw2 = log_termweight(q2, d2)
tw3 = log_termweight(q3, d3)

print(tw1, tw2, tw3, "\n")