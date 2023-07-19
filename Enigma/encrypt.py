from pprint import pprint

from key import setKey

#!--------------------------------------------------------------

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


#!--------------------------------------------------------------
encodeMess("Wiskey Wednesday",1,1,1,1)

pprint("the encoded message is " + encrypted)

#!--------------------------------------------------------------