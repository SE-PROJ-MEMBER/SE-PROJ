import hashlib



def encrypt(hash_string):
    hash_string = str(hash_string)
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


def decrypt(code):
    worddict_de = i()
    if code in worddict_de.keys():
        return worddict_de[code]
    


def add(value):
    worddict_ad = i()
    value = str(value)
    if encrypt(value) not in worddict_ad.keys():
        worddict_ad[encrypt(value)] = value
    o(worddict_ad)


def i():
    worddict = {}
    with open('source/worddict.txt', 'r') as f:
        for line in f.readlines():
            word = line.strip()
            word = str(word)
            if encrypt(word) not in worddict.keys():
                worddict[encrypt(word)] = word
    return worddict



def o(worddict_o): 
    with open('source/worddict.txt', 'w') as f:
        for value in worddict_o.values():
            f.write(value + '\n')

