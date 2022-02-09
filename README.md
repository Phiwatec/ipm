# Software to update A and AAAA records
## Software for Updating records because of changing IPs and Prefixes
This allows you to automatically update local records.  
There are already two DNS Providers available.  
More providers might follow. This can also be used to update specific firewall rules using the opnsense API.  

## Requirements
This software requires the following python modules:  
- requests

The hetzner module requires [hdns](https://github.com/lanbugs/hdns_cli) to be installed and set up on the system


## Usage
Fill in the config files as shown in the sample config files.  
Then just run the Software with python3 main.py  
I recommend using cron to execute this programm regularly ( i.e. every five minutes) using cron.  
The software will check if it needs to update any records and will only do so if needed.  


