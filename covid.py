import http.client

from prettytable import PrettyTable
import json

conn = http.client.HTTPSConnection("corona-virus-world-and-india-data.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "Your RAPID API KEY",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

conn.request("GET", "/api_india", headers=headers)

res = conn.getresponse()
data = res.read()

mydata=json.loads(data.decode("utf-8"))
#print(list(mydata))
my_state_key=list(mydata['state_wise'])

myheading=PrettyTable(['State Name','Active Cases','Confirmed Cases','Total Deaths'])
for s in my_state_key:
    st=s
    act=mydata['state_wise'][s]['active']
    cnf=mydata['state_wise'][s]['confirmed']
    dth=mydata['state_wise'][s]['deaths']
    myheading.add_row([st,act,cnf,dth])
print(myheading)

