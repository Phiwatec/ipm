import requests
import os,json
import subprocess

class hetzner_dns:
    COMMAND="hdns"
    SYSTEM="--system"
    TOKEN="--token"
    CONFIGFILE="prefix.json"
    PREFIXFILE="old.prefix"
    UPDATE_RECORD="update_record"
    RECORD_ID="--record_id="
    
    def __init__(self, config_file):
        self.config_file = config_file
        self.config=json.loads(open(self.config_file, "r").read())

    def hasV4(self):
        return True
    

    def hasV6(self):
        return True

    def update_dns(self,id,prefix,suffix,domain,rec_type):
        subprocess.run(
            
                [self.COMMAND,
                self.SYSTEM,
                self.config["system"],
                self.TOKEN,
                self.config["token"],
                self.UPDATE_RECORD,
                self.config["zone"],
                self.RECORD_ID+id,
                domain,
                rec_type,
                prefix+suffix]
                )

    def update_v6(self,new_prefix,prefix_len):
        
        for record in self.config["records"]["ipv6"]:
            self.update_dns(record["record_id"],new_prefix,record["suffix"],record["domain"],"AAAA")
    
    def update_v4(self,new_ip):
        for record in self.config["records"]["ipv4"]:
            self.update_dns(record["record_id"],new_ip,"",record["domain"],"A")

if __name__ == "__main__":
    print("This is a library")
    exit(1)


