import json
import requests
import os
import datetime
import calendar

def requestSon(symbol):
    webURL = "https://www.alphavantage.co/query"
    promptArg = {
        "function" : "TIME_SERIES_MONTHLY_ADJUSTED",
        "outputsize" : "compact",
        "datetype" : "json",
        "symbol" : symbol,
        "apikey" : "D65DITJ3FELD2PR7",
    }

    toAlpha = requests.get(webURL, promptArg)
    test = json.loads(toAlpha.text)

    #sonFile = open(str(symbol + ".txt"), "w+")
    #sonFile.write(toAlpha.text)
    
    return test

def parseDiv(package):
    temp = 0
    try:
        for x in package["Monthly Adjusted Time Series"]:
            temp += 1
            divPayout = package["Monthly Adjusted Time Series"][str(x)]["7. dividend amount"]
            if(temp == 11):
                print("Failed to find annual dividend")
                break
            elif(divPayout != "0.0000"):
                annualPay = float(divPayout) * 4
                return annualPay
    except:
        print(str(EnvironmentError) + " occured, maybe requesting too much from server. Retry later.")
        pass

    return
