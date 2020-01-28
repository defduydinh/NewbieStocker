#import necessary libraries
import pandas as pd
import json
import webbrowser as wb
import yfinance as yf
import datetime
from pandas_datareader import data as pdr

#import addition .py files
import getAPI_key
import fetchResponse

json_content = {}

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
        #fetch response for ticker from Rapid API
        API_response = fetchResponse.fetchStockData(ticker, API_key)
        
        #Determine response
        if(API_response != None):
            global json_content
            json_content = API_response
            
            
        else:
            print("Rapid API response: None")
            
            
    except Exception as err:
        #Catch and output error
        print("Error: ")
        print(err)
        
