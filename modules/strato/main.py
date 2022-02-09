from strato_dns import strato_dns

strato= strato_dns("records.json")

strato.update_v4("1.2.3.4")
strato.update_v6("12:cd:23:", 64)