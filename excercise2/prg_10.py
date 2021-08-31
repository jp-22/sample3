d1 = {'a':1,'b':2,'c':3}

def checkKey(dict, key):
    if key in dict:
        print("Present ")
        print("value =", dict[key])
    else:
        print("Not present")



checkKey(d1,'c')