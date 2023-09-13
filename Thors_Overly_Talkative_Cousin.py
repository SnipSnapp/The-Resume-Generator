from scapy.all import *
#ALWAYS RUN IN PROD
Cool_guy_mac = Ether(src='FF:FF:FF:FF:FF:FF', dst= 'FF:FF:FF:FF:FF:FF')/IP(src='0.0.0.0',dst='0.0.0.0',ttl=250)/ICMP()
while True:
  sendp(Cool_guy_mac)
