import requests,json
from modules.hetzner_dns.hetzner_dns import hetzner_dns
CONFIGFILE="settings.conf"
IP_CONFIG_FILE="current_ip.json"
PREFIX_LEN=64
locations=[]
hdns=hetzner_dns("hetzner_records.json")

locations.append(hdns)


def getPrefix(ip):
    ip=ip.split(":")
    ret_ip=""
    for i in range(0,4):
        ret_ip+=ip[i]+':'
    return ret_ip



def updatePrefixFile(new_prefix,new_ip):
    data = {       
                'old_ip' : new_ip,
                'old_prefix' : new_prefix,
            }

    ip_config_file_handler.seek(0)
    ip_config_file_handler.write(json.dumps(data))

def getNewIP():
    r = requests.get(config["ip4_url"])
    if r.status_code != 200 :
        exit("ERROR: Can't get IP adress please check internet connection")
    if ":" in r.text :
        exit("ERROR: Got IPv6 adress: Make shure you have IPv4 internet access")
    return r.text
    
def getNewPrefix():
    # Get current IP
    r = requests.get(config["ip6_url"])
    #Check if request was okay and adress is IPv6
    if r.status_code != 200 :
        exit("ERROR: Can't get IP adress please check internet connection")
    if "." in r.text :
        exit("ERROR: Got IPv4 adress: Make shure you have IPv6 internet access")
    #function for seperating the prefix part from the host part
    return getPrefix(r.text)


def updateV4(new_ip):
    for location in locations:
        if (location.hasV4()):
            location.update_v4(new_ip)
    
def updateV6(new_prefix,prefix_len):
    for location in locations:
        if (location.hasV6()):
            location.update_v6(new_prefix,prefix_len)


def main():
    config=json.loads(open(CONFIGFILE, "r").read())
    ip_config_file_handler=open(IP_CONFIG_FILE, "r+")
    ip_config=json.loads(ip_config_file_handler.read())

    #Get prefix from own IP adress
    new_prefix=getNewPrefix()
    new_ip=getNewIP()
    old_prefix=ip_config["old_prefix"]
    old_ip=ip_config["old_ip"]
    if (new_prefix == old_prefix):
        print("IPv6 didn't change")
    else:
        print("Got new prefix:  "+new_prefix+"\nUpdating all references\n")
        updateV6(new_prefix,PREFIX_LEN)

    if (new_ip == old_ip):
        print("IPv4 didn't change")
    else:
        print("Got new ip:  " + new_ip + "\n Updating all references\n")
        updateV4(new_ip)

    
    updatePrefixFile(new_prefix,new_ip)


if __name__ == "__main__":
    main()
