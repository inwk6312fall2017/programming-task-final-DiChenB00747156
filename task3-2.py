#Create a Python dictionary of all access lists configured in the firewall
access_name=["transit_access","global_access","xcompany-lan_access_","management2_access_","sharedresource_access_","SomeProducts_access_","fw-management_access_","WirelessHotspot_access_","voicevlan_access_","WirelessClients_access_"]

def accesslist(filename):
    d = {}
    fin = open(filename)
    for line in fin:
        wordlist = line.strip()
        for item in access_name:
            if item in wordlist:
               d[item] = [line]
# The dictionary's key is the name of access list and value are all the lines in the access list intact.
    for key in d:
        print("access name: %s" % (key))
        print(d[key])

accesslist("running-config.cfg")
