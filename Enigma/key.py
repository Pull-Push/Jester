from pprint import pprint
import string
import random

def setKey(message, shift, seed1, seed2, seed3):
    counter = 0
    inputSet = [shift, seed1, seed2, seed3]
    dataSet = [[],[],[],[]]
    sortList = []
    sortDict = {0:{},1:{},2:{},3:{}}
    
    setUp = {0:{" ": ""},
    1:{" ": ""},
    2:{" ": ""},
    3:{" ": ""}}
    
    master = {}
    
    for j in setUp:
        for x in string.printable:
            setUp[j][x] = ""
    
    #! INSERT KEY SHIFTING HERE - AFTER EACH INPUT MESSAGE
    for y in range(len(inputSet)):
        random.seed(inputSet[y])
        for i in range(len(string.printable)):
            dataSet[y].append(random.random())

    for z in range(len(setUp)):
    #< Generate Random Numbers for each Letter
        for key, val in zip(setUp[z], dataSet[z]):
            setUp[z][key] = val
        marklist=sorted((value, key) for (key,value) in setUp[z].items())
        sortList.append(marklist)

    #< Turn List into Dictionary
    for i in range(len(sortList)):
        markDict=dict([(v,k) for v,k in sortList[i]])
        sortDict[i] = markDict

    #< Strip random numbers from Dictionary and merge dicts together
    for i in range(len(setUp)):
        comb = dict(zip(setUp[i].keys(), sortDict[i].values()))
        master[i] = comb

    return master
