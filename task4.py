
import requests
import json

controller='devnetapi.cisco.com/sandbox/apic_em'


class Network: #get host
    template_name = "networkdevices.html"

    def getTicket(self):
        url = "https://" + controller + "/api/v1/ticket"
        payload = {"username": "devnetuser", "password": "Cisco123!"}
        header = {"content-type": "application/json"}
        response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
        r_json = response.json()
        ticket = r_json["response"]["serviceTicket"]
        return ticket


    def getNetworkcount(self,ticket):
        url = "https://" + controller + "/api/v1/network-device"
        header = {"content-type": "application/json", "X-Auth-Token": ticket}
        response = requests.get(url, headers=header, verify=False)
        r_json = response.json() #get all information of devices
        print("The counts of network devices is :")
        print(len(r_json['response']))#get the counts of devices

    def gethost(self, ticket):
        url = "https://" + controller + "/api/v1/host"
        header = {"content-type": "application/json", "X-Auth-Token": ticket}
        response = requests.get(url, headers=header, verify=False)
        r_json = response.json()
        
        for item in r_json['response']:
            print("the ip address of this host is %s " % item['hostIp'])
            print("the mac address of this host is %s " % item['hostMac'])
            

# create a object
a = Network()
ticket = a.getTicket()
a.gethost(ticket)
a.getNetworkcount(ticket)


