#import necessary libraries
import pandas as pd
import json
import webbrowser as wb
import yfinance as yf
import datetime
import os
import shutil
from pandas_datareader import data as pdr

#import addition .py files
import getAPI_key
import fetchResponse
import parseData


if __name__ == "__main__":
    try:
        #get API key
        API_key = ""
        #check for API key presence
        if(getAPI_key.verifyKey() < 0):
            getAPI_key.verifyKey()
        else:
            API_key = getAPI_key.verifyKey()
            
        #get ticker symbol
        ticker = input("Enter Ticker:: ")
        fileName = "response." + ticker + ".json"
        
        #Check if request been made before
        try:
            responseLoc = "./responses/" + fileName
            file = open(responseLoc, "r")
            print("File " + fileName + " exist, will not request from server.")
            
            file.close()
            
        except IOError as err:
            #fetch response for ticker from Rapid API
            print(ticker + " never requested, will request now.")
            API_response = fetchResponse.fetchStockData(ticker, API_key)
        
            #Determine response
            if(API_response != None):
                #global json_content
                json_content = API_response
                
                #write response to file and move to /responses folder
                try:
                    fileResponse = open(fileName, "w")
                    fileResponse.write(str(json_content))
                    fileResponse.close()
                    
                    shutil.move(("./" + fileName), "./responses/")
                except Exception as err:
                    print("Write file response errored.")
                    print(err)
                
            else:
                print("Rapid API response: " + str(API_response))
            
            
    except Exception as err:
        #Catch and output error
        print("Main encountered error: ")
        print(err)
        
