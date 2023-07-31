from flask_app import app, SocketIO
from flask import render_template, request, redirect, session, url_for, jsonify
from pprint import pprint
import string
import random

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json() # retrieve the data sent from JavaScript
    # process the data using Python code
    print(data)
    return jsonify() # return the result to JavaScript



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


def encodeMess(message,shift = 1 ,seed1 = 1,seed2 = 1,seed3 = 1):
    secret = setKey(message,shift,seed1, seed2, seed3)
    #< Encrypt Message
    #<loop through each clear character
    output = message
    for i in range(len(secret)):
        print("running encryption level", i)
        temp = ""
        for x in output:
            for key, val in secret[i].items():
                if x == key:
                    temp += val
        output = temp
        global encrypted
        encrypted  = output
        print("encrypt level ",i," complete....", output )
    return encrypted

def decodeMess(encoded, shift, s1, s2, s3):
    secret = setKey(encoded,shift,s1, s2, s3)
    output = encoded
    for i in range(len(secret)-1, -1, -1):
        print("running decryption level", i)
        temp = ""
        for x in output:
            for key, val in secret[i].items():
                if x == val:
                    temp += key
        output = temp
        print("decrypt level ",i," complete....", output )
    return output