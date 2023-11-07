import json

myinfo = {
  "server1": {
    "IBM": {
      "datacenter": "Pakistan",
      "env": {
        "PR": "192.168.1.6",
        "DR": "192.168.1.5"
      }
    }
  }
}
print(myinfo)

mypath="user_details.json"
with open(mypath,'w') as df:
    json.dump(myinfo,df,indent=4)
