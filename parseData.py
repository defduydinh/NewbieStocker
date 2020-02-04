import json

parsedData = 0
fileData = 0

def parseFile(inputFile):
    #Default to test.json
    #fileLoc = inputFile
    
    try:
        #Open file and load content as json
        loc = "./responses/response.F.json"
        fileLoc = open(loc, "r")
        global fileData
        fileData = json.loads(fileLoc.read())        
        fileLoc.close()
        
    except Exception as err:
        print("Error in parse file:")
        print(err)


def parseRequest(inputResponse):
    global fileData
    fileData = json.loads(inputResponse)

def dumpJson():
    eps_temp = len(fileData["timeSeries"]["annualDilutedEPS"]) - 1
    
    parsedData = json.dumps({
            "DividendRate": fileData["summaryDetail"]["dividendRate"]["raw"],
            "EPSgrowthFinal": [
                fileData["timeSeries"]["annualDilutedEPS"][eps_temp]["reportedValue"]["raw"],
                fileData["timeSeries"]["annualDilutedEPS"][eps_temp-1]["reportedValue"]["raw"]
                ],
            "Depreciation": fileData["cashflowStatementHistory"]["cashflowStatements"][0]["depreciation"]["raw"],
            "DividendPayout": fileData["cashflowStatementHistory"]["cashflowStatements"][0][]
    })    
    
    print(parsedData)
    
parseFile("hi")
dumpJson()