# 01-12-10 7:51
# 01-12-10 13:17
# 01-12-10 18:02
# 01/13/2010 08:09:48
# 01/13/2010 13:35:27
# 01/13/2010 17:57:52
from dateutil import parser
from datetime import datetime

dt = parser.parse("01/13/2010 20:57:52")
print(int(dt.timestamp()))