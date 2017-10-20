import requests
import json

controller='devnetapi.cisco.com/sandbox/apic_em'
url = "https://" + controller + "/api/v1/ticket"
payload = {"username":"devnetuser","password":"Cisco123!"}
header = {"content-type": "application/json"}
response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)
r_json=response.json()
print(r_json)
ticket = r_json["response"]["serviceTicket"]

# URL for Host REST API call to get list of exisitng hosts on the network.
url = "https://" + controller + "/api/v1/host"
header = {"content-type": "application/json", "X-Auth-Token":ticket}
response = requests.get(url, headers=header, verify=False)
print ("Hosts = ")
print (json.dumps(response.json(), indent=4, separators=(',', ': ')))
r_resp=response.json()
print(r_resp["response"][0]["hostIp"])
