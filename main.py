import toAlpha
import webbrowser
try:
    from tabulate import tabulate
except:
    print("Error: Tabulate install required")

def printTable():
    listSymbol = []
    listDiv = []
    with open("symbol.txt", "r") as ticker:
        for line in ticker:
            lineHolder = line[:-1]
            listSymbol.append(lineHolder)


    labelHead = [
        "Symbol",
        "Dividend"
    ]

    for x in listSymbol:
        currentSymbol = toAlpha.requestSon(x)
        currentDiv = toAlpha.parseDiv(currentSymbol)
        listDiv.append(currentDiv)

    toPrint = []

    for x in range(0,len(listSymbol)):
        newtable = [listSymbol[x], listDiv[x]]
        toPrint.append(newtable)
    print(tabulate(toPrint, headers= labelHead, numalign="left"))
    return


def main():
    printTable()
    tickerSym = input("Enter a ticker:: ")
    secURL = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=%s&type=10-k&dateb=&owner=exclude&count=40" % tickerSym
    webbrowser.get('google-chrome').open_new_tab(secURL)

    return 0

if __name__ == "__main__":
    main()

