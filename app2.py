
from datetime import date
import datetime
import requests, json
import time

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

class Ramadhan:
  today = date.today()
#  datemmdd = str('{}-{}'.format(today.month, today.day))
# data = requests.get(f"https://api.pray.zone/v2/times/day.json?city=lamongan&date=2022-{datemmdd}&timeformat=1").json()
  data2 = requests.get(f"https://api.myquran.com/v1/sholat/jadwal/1610/2022/{today.month}/{today.day}").json()
#  def __init__(self, shalat):
    
  @classmethod
  def timeShalat(cls, shalat):
    cls.shalatTime = shalat
    if cls.shalatTime == 'imsakT':
      cls.shalatTime = 'imsak'
      cls.today = cls.today + datetime.timedelta(days=1)
      cls.datemmdd = '{}-{}'.format(cls.today.month, cls.today.day)
      cls.data2 = requests.get(f"https://api.myquran.com/v1/sholat/jadwal/1610/2022/{cls.today.month}/{cls.today.day}").json()
    else: 
      pass
#      dataDate = cls.data["results"]["datetime"][0]["times"][cls.shalatTime]
    dataDate = cls.data2["data"]["jadwal"][cls.shalatTime]
    print(cls.today, end='\r\r')
    print('\n' + cls.shalatTime + ' : ' + dataDate)
    return dataDate
    
#  def getCity(self):
 #   getCity = self.data["results"]["location"]["city"]
if __name__ == "__main__":
 x = str(input('Which? (imsakT/imsak/maghrib) \n > '))
 Ramadhan.timeShalat(x)
 print('')
 time.sleep(2)

