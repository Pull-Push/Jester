from pprint import pprint
from key import setKey
from encrypt import encrypted

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



pprint("the decoded message is " + decodeMess(encrypted,1,1,1,1))

