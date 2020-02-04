import json

parsedData = 0
fileData = 0

def parseFile(inputFile):
    #Default to test.json
    fileLoc = inputFile
    
    try:
        #Open file and load content as json
        #fileLoc = "./responses/response.F.json"
        fileLoc = open(fileLoc, "r")
        global fileData
        fileData = json.loads(fileLoc.read())        
        fileLoc.close()
        return dumpJson()
        
    except Exception as err:
        print("Error in parse file:")
        print(err)


def parseRequest(inputResponse):
    global fileData
    fileData = json.loads(inputResponse)
    return dumpJson()

def dumpJson():
    prevAnnual = len(fileData["timeSeries"]["annualDilutedEPS"]) - 1
    
    parsedData = json.dumps({
            #Year to Year EPS growth
            "EPSgrowthYoY": [
                fileData["timeSeries"]["annualDilutedEPS"][prevAnnual]["reportedValue"]["raw"],
                fileData["timeSeries"]["annualDilutedEPS"][prevAnnual-1]["reportedValue"]["raw"]
                ],
            
            #Dividend Payout Ratio
            "DividendRate": fileData["summaryDetail"]["dividendRate"]["raw"],
            "DividendPayout": fileData["cashflowStatementHistory"]["cashflowStatements"][0]["dividendsPaid"]["raw"],
            
            #EBITDA
            "AnnualEBITDA:": fileData["timeSeries"]["annualEbitda"][prevAnnual]["reportedValue"]["raw"],
            
            #Capitalization Rate
            "OperatingIncome": fileData["timeSeries"]["annualOperatingIncome"][prevAnnual]["reportedValue"]["raw"],
            "PreMarketPrice": fileData["price"]["preMarketPrice"]["raw"]
    })    
    
    return parsedData
    