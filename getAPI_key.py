import os

def getKey():
    #Open file and read key from api_key.txt
    #return API key to caller
    try:
        keyFile = open("api_key.txt", "r")
        API_key = keyFile.read()
        keyFile.close
        return API_key
    except Exception as err:
        print("Error:")
        pritn(err)


def writeKey(key):
    #Open and write key provided by user.
    try:
        keyFile = open("api_key.txt", "w")
        keyFile.write(key)
        keyFile.close
    except Exception as err:
        print("Error:")
        print(err)
    
    
#get API key from file
def verifyKey():
    #Initiate a check for API key
    #If key does not exist, request from user | writeKey(key)
    #Else open file and read key | getKey()
    key = ""
    if(os.stat("api_key.txt").st_size == 0):
        key = input("Enter API key:: ")
        writeKey(key)
        return -1
    else:
        return getKey()