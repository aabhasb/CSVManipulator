import csv
from dateutil import parser
from datetime import datetime

files = ['device_info']
suffix = '.csv'
 
for file in files:
    userIDs = []
    pcIDs = []
    dates = []
    activities = []
    with open(''.join([file,suffix])) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            userIDs.append(row[2])
            pcIDs.append(row[3])
            dates.append(row[1])
            activities.append(row[4])
        
    convertedIDs = []
    for userID in userIDs[1:]:
        convertedID = ''.join([(str(ord(x)) if x.isalpha() else x) for x in list((userID.split("/"))[1])])
        convertedIDs.append(convertedID)
    
    convertedPCIDs = []
    for pcID in pcIDs[1:]:
        convertedPCIDs.append(pcID.split("-")[1])
    
    convertedDates = []
    for date in dates[1:]:
        dt = parser.parse(date)
        convertedDates.append(int(dt.timestamp())-18000)
    
    activityDict = {"Connect":1,"Disconnect":0}
    i = 2
    for activity in activities[1:]:
        if activity not in activityDict:
            activityDict[activity] =i
            i=i+1
      
    with open(''.join([file,'Mod',suffix]), 'w', newline='') as outCSV:
        outCSVWriter = csv.writer(outCSV)
        #Remove the below line if you dont want the column headers
        outCSVWriter.writerow(["Date","UserID","PC-ID","Activity"])
        for date, uID, pc, activity in zip(convertedDates, convertedIDs, convertedPCIDs, activities[1:]):
            outCSVWriter.writerow([date, uID, pc, activityDict.get(activity)])
               
