import json

def calData(obj):
    EPSGrowth = obj["EPSgrowthYoY"][0] - obj["EPSgrowthYoY"][1]
    print(EPSGrowth)