import requests


def fetchStockData(ticker, API_key):
    
    #Prep parameters to pass to server
    financial_API_URL = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail"
    financial_API_query = {"region":"US","lang":"en","symbol": ticker}
    financial_API_headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': API_key,
        "Content-Type": "application/json"
    }
    
    #Request from RapidAPI server
    #Query Yahoo-finance.
    response = requests.get("GET", financial_API_URL,
                            headers= financial_API_headers,
                            params= financial_API_query)
    
    if(response.status_code == 200):
        #Return content of response
        return response.json
    else:
        #Return error code from server
        return "Failed to communicate with X-RapidAPI. Status response: " + str(response.status_code)