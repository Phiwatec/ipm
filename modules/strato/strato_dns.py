import requests
import os,json
import subprocess

class strato_dns:
    
    
    def __init__(self, config_file):
        self.config_file = config_file
        self.config=json.loads(open(self.config_file, "r").read())

    def hasV4(self):
        return True
    

    def hasV6(self):
        return True

    def update_dns(self,prefix,suffix,domain):
        url='https://' + self.config["user"] +':' + self.config["password"] + '@' +self.config["system"] + domain + '&myip=' + prefix +suffix
        print(url)
        #r=requests.get(url)


    def update_v6(self,new_prefix,prefix_len):
        
        for record in self.config["records"]["ipv6"]:
            self.update_dns(new_prefix,record["suffix"],record["domain"])
    
    def update_v4(self,new_ip):
        for record in self.config["records"]["ipv4"]:
            self.update_dns(new_ip,"",record["domain"])


if __name__ == "__main__":
    print("This is a library")
    exit(1)


