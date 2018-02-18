import csv


files = ['2009-12','2010-Jan','2010-Feb','2010-Mar','2010-Apr','2010-May','2010-Jun',
         '2010-Jul','2010-Aug','2010-Sep','2010-Oct','2010-Nov','2010-Dec','2011-Jan',
         '2011-Feb','2011-Mar','2011-Apr','2011-May']
suffix = '.csv'
 
for file in files:
    userIDs = []
    roles = []
    with open(''.join([file,suffix])) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            userIDs.append(row[1])
            roles.append(row[4])
    
    
    convertedIDs = []
    for userID in userIDs[1:]:
        convertedID = ''.join([(str(ord(x)) if x.isalpha() else x) for x in list(userID)])
        convertedIDs.append(convertedID)
    
    roleDict = {"Administrative Assistant":0,"Administrative Staff":1,"Director":2,
                "Engineer":3,"Foreman":4,"IT Admin":5,
                "Janitor":6,"Loading Dock":7,"Of Council":8,
                "Project Manager":9,"Security":10,"Senior Manger":11,
                "Technician":12,"Tradesman":13,"VP":14}
    i = 15
    for role in roles[1:]:
        if role not in roleDict:
            roleDict[role] =i
            i=i+1
    print(roleDict)
    
    with open(''.join([file,'Mod',suffix]), 'w', newline='') as outCSV:
        outCSVWriter = csv.writer(outCSV)
        #Remove the below line if you dont want the column headers
        outCSVWriter.writerow(["UserID","Role"])
        for uID, role in zip(convertedIDs, roles[1:]):
            outCSVWriter.writerow([uID,roleDict.get(role)])
             
