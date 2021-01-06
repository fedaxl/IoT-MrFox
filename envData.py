#!/usr/bin/python3

from urllib.request import urlopen
import  json
import  time
from sense_hat import SenseHat

WRITE_API_KEY='LX24RSBOHE6C83AB'

baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY

sense = SenseHat()

def writeData(temp,hum,press):
    # Sending the data to thingspeak in the query string
    conn = urlopen(baseURL + '&field1=%s&field2=%s&field3=%s' % (temp,hum,press))
    print(conn.read())
    # Closing the connection
    conn.close()

while True:
    temp=round(sense.get_temperature(),2)
    hum=round(sense.get_humidity(),2)
    press=round(sense.get_pressure(),2)
    writeData(temp,hum,press)
    time.sleep(60)




