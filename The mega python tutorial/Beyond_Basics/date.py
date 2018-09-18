from datetime import datetime
date1 = datetime.now()
date2 = datetime(2018, 1, 21)
date3 = datetime.strptime("2018-12-12","%Y-%m-%d")   //convert string to datetime
print(date3.strftime("%Y"))             //get string from time
