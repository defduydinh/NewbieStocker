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
import parsingData
import calculateData


#Global variable holder
parsedData = 0

if __name__ == "__main__":
    try:
        #get API key
        API_key = ""
        #check for API key presence
        if(getAPI_key.verifyKey() == -1):
            getAPI_key.verifyKey()
        else:
            API_key = getAPI_key.verifyKey()
            
        #get ticker symbol
        ticker = input("Enter Ticker:: ")
        fileName = "response." + ticker + ".json"
        
        
        #Check if request been made before
        #If file exist, don't send request and parse existing JSON data in /response
        #Else file does not exist, send a request to server and move JSON data to /response, and parse JSON
        try:
            responseLoc = "./responses/" + fileName
            file = open(responseLoc, "r")
            print("File " + fileName + " exist, will not request from server.")
            
            #Send json file to parse and return a json
            parsedData = parsingData.parseFile(responseLoc)
            file.close()
            
        except IOError as err:
            #fetch response for ticker from Rapid API
            print(ticker + " never requested, will request now.")
            API_response = fetchResponse.fetchStockData(ticker, API_key)    #API_response contain JSON from server
        
            #Determine action to take when receive not NONE response
            if(API_response != None):
                json_content = API_response
                
                #write response to file and move to /responses folder
                try:
                    fileResponse = open(fileName, "w")
                    fileResponse.write(str(json_content))
                    fileResponse.close()
                    shutil.move(("./" + fileName), "./responses/")
                    
                    #Parse the data right after received.
                    parsedData = parsingData.parseRequest(json_content)
                    
                except Exception as err:
                    print("Write file response errored.")
                    print(err)
                
            else:   #Return error code returned by server
                print("Rapid API response: " + str(API_response))
            
            
    except Exception as err:
        #Catch and output error encountered in main
        print("Main encountered error: ")
        print(err)
    
    #Exit Fetching and parsing data
    calculateData.calData(parsedData)
    
    
