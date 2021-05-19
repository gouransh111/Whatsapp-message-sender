import pywhatkit
import csv
from datetime import datetime
time = datetime.now()
with open("C://Users//user//Desktop//wt1.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        time = datetime.now()
        pywhatkit.sendwhatmsg(f"+91-{row[1]}","Hello ",time.hour,time.minute+1,5)
