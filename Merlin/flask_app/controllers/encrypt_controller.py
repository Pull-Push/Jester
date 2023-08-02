from flask_app import app, SocketIO
from flask import render_template, request, redirect, session, url_for, jsonify
from pprint import pprint
import string
import random


@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json() # retrieve the data sent from JavaScript
    # process the data using Python code
    global seckey
    seckey = setKey(data['key']['shift'],data['key']['seed1'],data['key']['seed2'],data['key']['seed3'])
    clear = data['key']['message']
    # pprint(setKey(data['key']['shift'],data['key']['seed1'],data['key']['seed2'],data['key']['seed3']))
    secmes = encodeMess(clear)
    return jsonify(secmes) # return the result to JavaScript

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json() # retrieve the data sent from JavaScript
    # process the data using Python code
    global seckey
    seckey = setKey(data['key']['shift'],data['key']['seed1'],data['key']['seed2'],data['key']['seed3'])
    code = data['key']['message']
    # pprint(setKey(data['key']['shift'],data['key']['seed1'],data['key']['seed2'],data['key']['seed3']))
    clemes = decodeMess(code)
    return jsonify(clemes) # return the result to JavaScript

def setKey(shift, seed1, seed2, seed3):
    inputSet = [shift, seed1, seed2, seed3]
    dataSet = [[],[],[],[]]
    sortList = []
    sortDict = {0:{},1:{},2:{},3:{}}
    
    alpha = string.digits + string.ascii_letters + string.punctuation

    setUp = {0:{" ": ""},
    1:{" ": ""},
    2:{" ": ""},
    3:{" ": ""}}
    
    master = {}
    
    for j in setUp:
        for x in alpha:
            setUp[j][x] = ""

    #todo for j in setUp:
        #todo for x in string.printable:
            #todo setUp[j][x] = ""

    #! INSERT KEY SHIFTING HERE - AFTER EACH INPUT MESSAGE
    for y in range(len(inputSet)):
        random.seed(inputSet[y])
        for i in range(len(alpha)+1):
            dataSet[y].append(random.random())
    
    #todo for y in range(len(inputSet)):
    #todo     random.seed(inputSet[y])
    # todo    for i in range(len(string.printable)):
    #todo         dataSet[y].append(random.random())
    #todo pprint(dataSet)

    for z in range(len(setUp)):
    #< Generate Random Numbers for each Letter
        for key, val in zip(setUp[z], dataSet[z]):
            setUp[z][key] = val
        marklist=sorted((value, key) for (key,value) in setUp[z].items())
        sortList.append(marklist) #< TURNS INTO A LIST OF LISTS

    #< Turn List into Dictionary
    for i in range(len(sortList)):
        markDict=dict([(v,k) for v,k in sortList[i]])
        sortDict[i] = markDict #< TURNS INTO A DICTIONARY OF DICTIONARIES


    #< Strip random numbers from Dictionary and merge dicts together
    for i in range(len(setUp)):
        comb = dict(zip(setUp[i].keys(), sortDict[i].values()))
        master[i] = comb #< MERGED DICTIONARY OF DICTIONARIES

    print('Encry complete')

    return master

def encodeMess(message):
    secret = seckey
    # pprint(secret)
    #< Encrypt Message
    #<loop through each clear character
    output = message
    for i in range(len(secret)):
        #print("running encryption level", i)
        temp = ""
        for x in output:
            for key, val in secret[i].items():
                if x == key:
                    temp += val
        output = temp
        global encrypted
        encrypted  = output
        #print("encrypt level ",i," complete....", output )
    return encrypted

def decodeMess(encoded):
    secret = seckey
    output = encoded
    for i in range(len(secret)-1, -1, -1):
        #print("running decryption level", i)
        temp = ""
        for x in output:
            for key, val in secret[i].items():
                if x == val:
                    temp += key
        output = temp
        #print("decrypt level ",i," complete....", output )
    return output