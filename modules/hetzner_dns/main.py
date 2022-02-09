from hetzner_dns import hetzner_dns
def main():    
    hdns=hetzner_dns("records.json")
    hdns.update_v6("2112df",56)
    hdns.update_v4("1.1.1.1")

if __name__ == "__main__":
    main()