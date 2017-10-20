# Simple Example of calling REST API from Python
# This is all that is required to call a REST API from python

# * THIS SAMPLE APPLICATION AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY
# * OF ANY KIND BY CISCO, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED
# * TO THE IMPLIED WARRANTIES OF MERCHANTABILITY FITNESS FOR A PARTICULAR
# * PURPOSE, NONINFRINGEMENT, SATISFACTORY QUALITY OR ARISING FROM A COURSE OF
# * DEALING, LAW, USAGE, OR TRADE PRACTICE. CISCO TAKES NO RESPONSIBILITY
# * REGARDING ITS USAGE IN AN APPLICATION, AND IT IS PRESENTED ONLY AS AN
# * EXAMPLE. THE SAMPLE CODE HAS NOT BEEN THOROUGHLY TESTED AND IS PROVIDED AS AN
# * EXAMPLE ONLY, THEREFORE CISCO DOES NOT GUARANTEE OR MAKE ANY REPRESENTATIONS
# * REGARDING ITS RELIABILITY, SERVICEABILITY, OR FUNCTION. IN NO EVENT DOES
# * CISCO WARRANT THAT THE SOFTWARE IS ERROR FREE OR THAT CUSTOMER WILL BE ABLE
# * TO OPERATE THE SOFTWARE WITHOUT PROBLEMS OR INTERRUPTIONS. NOR DOES CISCO
# * WARRANT THAT THE SOFTWARE OR ANY EQUIPMENT ON WHICH THE SOFTWARE IS USED WILL
# * BE FREE OF VULNERABILITY TO INTRUSION OR ATTACK. THIS SAMPLE APPLICATION IS
# * NOT SUPPORTED BY CISCO IN ANY MANNER. CISCO DOES NOT ASSUME ANY LIABILITY
# * ARISING FROM THE USE OF THE APPLICATION. FURTHERMORE, IN NO EVENT SHALL CISCO
# * OR ITS SUPPLIERS BE LIABLE FOR ANY INCIDENTAL OR CONSEQUENTIAL DAMAGES, LOST
# * PROFITS, OR LOST DATA, OR ANY OTHER INDIRECT DAMAGES EVEN IF CISCO OR ITS
# * SUPPLIERS HAVE BEEN INFORMED OF THE POSSIBILITY THEREOF.-->


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

