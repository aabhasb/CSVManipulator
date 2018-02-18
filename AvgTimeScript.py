from dateutil import parser
from datetime import datetime
 
diff = []
timeSplit = []
file = open("time.txt","r")
for i in 350:
    timeStamps = (file.readline().split("@"))[1]
    timeSplit = timeStamps.split(":")
    diff = diff.append(timeSplit[2]*1000)
    
   
