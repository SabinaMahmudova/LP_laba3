import requests
import datetime as dt
data = requests.get('https://api.meetup.com/2/open_events?&sign=true&photo-host=public&lat=48.836452&topic=css&city=Paris&category=34&lon=2.413619&radius=10&page=20&time=,1w&key=3e31d77116b6f1f1a5b2c201a2b298')
data_all = data.json()
file=open("events.html", "w+", encoding='utf-8')
file.write("<style type='text/css'> body{background-color: rgb(132, 255, 132); font-family:Arial; font-size:16px;} h3{display:inline; font-style:italic;} div{margin-bottom:10px;}</style>")
file.write("<h2 style='text-align:center;'>"+"Events in topic IT from "+str(dt.date.today())+" to "+str(dt.date.today()+dt.timedelta(days=7))+"</h2>")
i =1
for item in data_all['results']:
  time=dt.datetime.fromtimestamp(int(str(item['time'])[0:10]))
  file.write("<div>" + "<h3>" +str(i)+ ". name of Occasion: " + "</h3>" + str((item['group'])['name'])+"</div>")
  file.write("<div>"+"<h3>" + "Time: " + "</h3>" + str(time)+"</div>")
  file.write("<div>" + "<h3>" + "Address: " + "</h3>" + str((item['venue'])['address_1'])+"</div>")
  try:
    file.write("<div>" + "<h3>" + "Discription : " + "</h3>" + str(item['description'])+"</div>" )
  except:pass
  file.write("<div style='margin-bottom:60px;'>"+ "<h3>" +"Organizator: " + "<h3>" + str((item['group'])['who'])+"</div>")
  i = i+1
file.close()
