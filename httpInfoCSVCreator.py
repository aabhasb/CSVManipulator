import csv
from dateutil import parser
from datetime import datetime

files = ['http_info']
suffix = '.csv'
 
for file in files:
    userIDs = []
    pcIDs = []
    dates = []
    sites = []
    
    with open(''.join([file,suffix])) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            userIDs.append(row[2])
            pcIDs.append(row[3])
            dates.append(row[1])
            sites.append(row[4])
        
    siteDict = {}
    i = 0;
    
    with open(''.join([file,'Mod',suffix]), 'w', newline='') as outCSV:
        outCSVWriter = csv.writer(outCSV)
        for date, uID, pc, site in zip(dates, userIDs, pcIDs,sites ):
            convertedUID = ''.join([(str(ord(x)) if x.isalpha() else x) for x in list((uID.split("/"))[1])])
            convertedPCID = pc.split("-")[1]
            dt = parser.parse(date)
            convertedDate = int(dt.timestamp()) - 18000
            
            if site not in siteDict:
                siteDict[site] = i
                i = i+1
            
            outCSVWriter.writerow([convertedDate, convertedUID, convertedPCID, siteDict.get(site)])
    print(siteDict)